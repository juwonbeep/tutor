from django.apps import AppConfig


class CrawlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crawl'

    def ready(self):
        from.scheduler import articleupdater
        articleupdater.artcrawlstart()
