from django.test import TransactionTestCase
from django.utils import timezone

from hello.models import Question0, Question1


class TestFasterTransactionTestCase(TransactionTestCase):
    def test_empty_1(self):
        assert Question0.objects.count() == 0
        assert Question1.objects.count() == 0
        Question0.objects.create(question_text="foo", pub_date=timezone.now())
        Question1.objects.create(question_text="foo", pub_date=timezone.now())

    def test_empty_2(self):
        assert Question0.objects.count() == 0
        assert Question1.objects.count() == 0
        Question0.objects.create(question_text="foo", pub_date=timezone.now())
        Question1.objects.create(question_text="foo", pub_date=timezone.now())


class TestResetSequences(TransactionTestCase):
    reset_sequences = True

    def test_empty_1(self):
        q1 = Question0.objects.create(question_text="foo", pub_date=timezone.now())
        self.assertEqual(q1.id, 1)
        q2 = Question0.objects.create(question_text="foo", pub_date=timezone.now())
        self.assertEqual(q2.id, 2)

    def test_empty_2(self):
        q1 = Question0.objects.create(question_text="foo", pub_date=timezone.now())
        self.assertEqual(q1.id, 1)
        q2 = Question0.objects.create(question_text="foo", pub_date=timezone.now())
        self.assertEqual(q2.id, 2)
