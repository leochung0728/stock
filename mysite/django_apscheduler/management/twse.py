from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from stock.crawler import twse
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime,timedelta


scheduler = BlockingScheduler()
scheduler.add_jobstore(DjangoJobStore())

# @scheduler.scheduled_job('cron', name='twse', second='*/3')
# def twse_job():
#     # twse.spider_twse(datetime.today().strftime('%Y%m%d'), datetime.today().strftime('%Y%m%d')).crawler()
#     print 'my_job is running, Now is %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     scheduler.print_jobs()

scheduler.start()
scheduler.print_jobs()

# job = scheduler.add_job(twse.spider_twse('20170620', '20170620').crawler, 'interval', minutes=5)

# scheduler = BlockingScheduler()
# scheduler.add_jobstore(DjangoJobStore())
# # scheduler.add_executor(ThreadPoolExecutor(10))
# def my_job():
#     print 'my_job is running, Now is %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# scheduler.add_job(my_job, 'cron', second='*/5') # twse.spider_twse('20170621', '20170621').crawler
# scheduler.start()

# scheduler.print_jobs()
# print scheduler.get_jobs()