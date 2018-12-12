from django.dispatch import receiver
from ..scraper.signals import post_saved
from .stats_calculator import StatsCalculator

@receiver(post_saved)
def send_mail_on_publish(post):
    calculator = StatsCalculator()
    calculator.recalculate(post)