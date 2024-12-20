from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from.artcrawl import articlereg

def artcrawlstart():
    scheduler = BackgroundScheduler()
    scheduler.add_job(articlereg, 'cron', day_of_week='mon', hour=15, minute=30, timezone="Asia/Seoul")
    scheduler.start()
    