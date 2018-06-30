from django.core.management.base import BaseCommand

from service.views import generate_call_list


class Command(BaseCommand):
    help = 'Generates the call list on Google'

    def handle(self, *args, **options):
        generate_call_list('')
