from apscheduler.schedulers.background import BackgroundScheduler

from internet_speed.cron.test_internet import test_internet
from internet_speed.cron.send_email import send_email


scheduler = BackgroundScheduler()
scheduler.add_job(test_internet, trigger='cron', minute='*/15', id='test_internet', replace_existing=True)
scheduler.add_job(send_email, trigger='cron', day_of_week="mon", minute="0", hour="8",
                  id='send_email', replace_existing=True)
