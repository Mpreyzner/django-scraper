from django_cron import CronJobBase, Schedule
from .post_scraper import PostScraper


class ScraperCronJob(CronJobBase):
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.scraper.scraper_cron'

    def do(self):
        scraper = PostScraper()
        scraper.execute()
