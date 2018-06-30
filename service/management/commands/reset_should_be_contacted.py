from django.core.management.base import BaseCommand

from service.models import Member


class Command(BaseCommand):
    help = 'Generates the call list on Google'

    def handle(self, *args, **options):
        for member in Member.objects.all():
            member.should_be_contacted = True
            member.save()
