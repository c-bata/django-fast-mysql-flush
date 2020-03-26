import time

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

        self.style = no_style()
        database = 'django'
        connection = connections['default']
        sql_list = sql_flush(self.style, connection, only_django=True,
                             reset_sequences=True,
                             allow_cascade=False)

        print("SQL: ", sql_list)

        try:
            connection.ops.execute_sql_flush(database, sql_list)
        except Exception as exc:
            raise CommandError(
                "Database %s couldn't be flushed. Possible reasons:\n"
                "  * The database isn't running or isn't configured correctly.\n"
                "  * At least one of the expected database tables doesn't exist.\n"
                "  * The SQL was invalid.\n"
                "Hint: Look at the output of 'django-admin sqlflush'. "
                "That's the SQL this command wasn't able to run.\n" % (
                    connection.settings_dict['NAME'],
                )
            ) from exc

        elapsed = time.time() - start
        print(f"elapsed: {elapsed:.3f}")
