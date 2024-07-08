from app import create_app
#from celery_config import celery_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
