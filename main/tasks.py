from celery.schedules import crontab

from eshop.celery import celery_app as app


@app.task
def test(arg):
    print(arg)
    return arg
