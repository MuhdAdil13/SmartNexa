import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Backup the database'

    def handle(self, *args, **kwargs):
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        backup_file = os.path.join(settings.BASE_DIR, 'backup.sql')

        os.system(f"mysqldump -u {db_user} -p{db_password} -h {db_host} {db_name} > {backup_file}")

        self.stdout.write(self.style.SUCCESS('Successfully backed up the database'))
