from django.core.management.base import BaseCommand
from diplomapp.models import Status


class Command(BaseCommand):
    help = "Create status by name"

    def add_arguments(self, parser):
        parser.add_argument('status', type=str, help='status name')

    def handle(self, *args, **kwargs):
        status = kwargs.get('status')
        status = Status(status=status)
        status.save()
        self.stdout.write(f'{status}')