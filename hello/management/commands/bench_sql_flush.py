import time
from statistics import mean, stdev

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone

from hello.models import *


def bench(question_count):
    if question_count is not None:
        attrs = globals()
        question_classes = [attrs[name] for name in attrs
                            if name.startswith("Question")]

        for i, klass in enumerate(question_classes):
            klass.objects.bulk_create([
                klass(question_text=f"question {i} {j}", pub_date=timezone.now())
                for j in range(question_count)
            ])

    start = time.time()

    call_command('flush', verbosity=0, interactive=False,
                 database='default', reset_sequences=False)

    elapsed = time.time() - start
    return elapsed


class Command(BaseCommand):
    help = 'measure the time for sql_flush()'

    def add_arguments(self, parser):
        parser.add_argument('question_count', nargs='?', type=int)

    def handle(self, *args, **options):
        question_count = options.get("question_count")

        elapsed = []
        for i in range(5):
            t = bench(question_count)
            print(f"{i}th elapsed: {t:.3f}")
            elapsed.append(t)

        print(f"elapsed: {mean(elapsed):.3f} sec (+/- {stdev(elapsed)})")
