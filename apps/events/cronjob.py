from apscheduler.schedulers.background import BackgroundScheduler

from .jobs import delete_past_events


# def start_jobs():
#     scheduler = BackgroundScheduler()
#
#     cron_job = {"month": "*", "day": "*", "hour": "*", "minute": "*/1"}
#
#     scheduler.add_job(delete_past_events, "cron", **cron_job)
#     scheduler.start()
