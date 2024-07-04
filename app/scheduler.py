from apscheduler.schedulers.blocking import BlockingScheduler
from check_new_videos import check_new_videos

scheduler = BlockingScheduler()

# Planifier la tâche tous les jours à 00:00
scheduler.add_job(check_new_videos, 'cron', hour=0)

if __name__ == '__main__':
    scheduler.start()
