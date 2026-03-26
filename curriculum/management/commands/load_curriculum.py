from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load initial curriculum data into the database (dev_wizard)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("load_curriculum command is set up (no data loaded yet)."))

