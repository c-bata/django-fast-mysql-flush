import time

from django.core.management import call_command
from django.core.management.color import no_style
from django.db import connections
from django.core.management.base import BaseCommand, CommandError
from django.core.management.sql import sql_flush
from django.utils import timezone

from hello.models import *


class Command(BaseCommand):
    help = 'measure the time for sql_flush()'

    def add_arguments(self, parser):
        parser.add_argument('question_count', nargs='?', type=int)

    def handle(self, *args, **options):
        question_count = options.get("question_count")

        if question_count is not None:
            attrs = globals()
            question_classes = [attrs[name] for name in attrs
                                if name.startswith("Question")]

            for i, klass in enumerate(question_classes):
                print("Inserting... ", klass.__name__)
                for j in range(question_count):
                    q = klass(question_text=f"test {i} {j}", pub_date=timezone.now())
                    q.save()

        start = time.time()

        call_command('flush', verbosity=0, interactive=False,
                     database='default', reset_sequences=False)

        elapsed = time.time() - start
        print(f"elapsed: {elapsed:.3f}")
