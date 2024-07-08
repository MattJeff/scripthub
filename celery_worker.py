from celery import Celery
from app import create_app

app = create_app()
celery = Celery(app.import_name, broker='redis://localhost:6379/0')
celery.conf.update(app.config)

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask
