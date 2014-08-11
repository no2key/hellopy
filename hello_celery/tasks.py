from hello_celery.cel import app


@app.task
def add(x, y):
    return x + y