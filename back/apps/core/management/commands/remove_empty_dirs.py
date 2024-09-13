from django.core.management.base import BaseCommand
from django.conf import settings

import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        for dir in os.listdir(f'{settings.BASE_DIR}/media'):
            try:
                os.rmdir(f'{settings.BASE_DIR}/media/{dir}')
                print(f'DELETED {dir}')
            except OSError as e:
                print(e)

        self.stdout.write(
            self.style.SUCCESS('Successfully removed empty dirs')
        )
