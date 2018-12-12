from .post_scraper import PostScraper


def scrape_blog():
    scraper = PostScraper()
    scraper.execute()
