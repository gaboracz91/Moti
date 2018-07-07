import datetime
import os

import django
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import management

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings.prod'
django.setup()

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=21, minute=5)
def scheduled_job():
    print('Run generate_call_list: {}'.format(datetime.datetime.now()))
    management.call_command('generate_call_list')
    print('Run reset_should_be_contacted: {}'.format(datetime.datetime.now()))
    management.call_command('reset_should_be_contacted')


sched.start()
