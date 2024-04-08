import os
from celery import Celery

import core.settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('core.settings', namespace='CELERY')
app.conf.broker_url = core.settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
