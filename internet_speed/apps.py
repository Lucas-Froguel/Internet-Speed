from django.apps import AppConfig as DjangoConfig


class AppConfig(DjangoConfig):
    name = "internet_speed"
    verbose_name = "InternetSpeed"

    def ready(self):
        from internet_speed.cron.config import scheduler
        scheduler.start()
