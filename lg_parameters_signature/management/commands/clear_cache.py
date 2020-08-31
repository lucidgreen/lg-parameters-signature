import django.core.cache
import django.core.management.base


class Command(django.core.management.base.BaseCommand):
    def handle(self, *args, **options):
        django.core.cache.cache.clear()
        pass
