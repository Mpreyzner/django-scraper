import bs4
import requests
from urllib.parse import urlparse
import unidecode
from langdetect import detect
from events.models import post_scraped
from .models import Post, Author


class PostScraper:
    url = 'https://teonite.com/blog'
    next_page_class = 'older-posts'
    timeout = 5

    def execute(self):
        print('PostScraper: Scraping started')
        parsed_url = urlparse(self.url)

        finished = False
        url = self.url
        while not finished:
            print("PostScraper processing: " + url)
            self.get_posts(url)
            next_page_html = self.get_elements_from_page(self.get_page_soup(url), self.next_page_class)
            if len(next_page_html) == 0:
                return
            next_page_path = next_page_html[0]['href']
            url = parsed_url.scheme + '://' + parsed_url.netloc + next_page_path

    def get_posts(self, url):
        title_class = 'post-title'
        parsed_url = urlparse(url)
        posts = self.get_elements_from_page(self.get_page_soup(url), title_class)

        for a in posts:
            title = a.text.strip()
            post_exists = Post.objects.filter(title=title).exists()
            if post_exists:
                continue

            post_url = a.find('a')['href']
            content, author = self.get_post_details(
                (parsed_url.scheme + '://' + parsed_url.netloc + post_url))  # use some function for url

            author_exists = Author.objects.filter(name=author).exists()
            if not author_exists:
                auth = Author(name=author, tokenized_name=unidecode.unidecode(author.lower().replace(" ", "")))
                # create custom constructor that will create tokenized_name from name
                auth.save()
            else:
                auth = Author.objects.get(name=author)

            language = detect(content)
            # print('Recognized language: ' + language + "for post:  " + title)
            post = Post(title=title, author=auth, content=content, language=language)
            post.save()

            post_scraped.emit(post)
        return posts

    def get_post_details(self, post_url):
        content_class = 'post-content'
        author_class = 'author-content'

        soup = self.get_page_soup(post_url)
        author_html = self.get_elements_from_page(soup, author_class)
        if len(author_html) == 0:
            raise Exception('html with author not found, searched for class:' + author_class + ' on page:' + post_url)
        author = author_html[0].find('h4').text.strip()

        content_html = self.get_elements_from_page(soup, content_class)
        if len(content_html) == 0:
            raise Exception(
                'html with post content not found, searched for class:' + content_class + ' on page:' + post_url)
        content = content_html[0].text.strip()

        return {'content': content, 'author': author}

    def get_elements_from_page(self, soup, css_class):
        return soup.select('.' + css_class)

    def get_page_soup(self, url):
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return bs4.BeautifulSoup(response.text, 'lxml')
