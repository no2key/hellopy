from celery import Celery

app = Celery('hello_celery',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['hello_celery.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)


if __name__ == '__main__':
    app.start()