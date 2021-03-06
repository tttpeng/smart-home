from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myhome.settings')

app = Celery('myhome')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.update(
#     CELERYBEAT_SCHEDULE={
#         'do-task-every-5-hours': {
#             'task': 'myhome.tasks.check',
#             'schedule': timedelta(hours=5),
#         },
#     }, )
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    print('hhhhhhh')
    return "哈哈哈"
