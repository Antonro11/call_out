from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import sample_account


class TestAccountModel(TestCase):
    def setUp(self):
        self.test_account = sample_account(email="test@gmail.com")

    def tearDown(self):
        self.test_account.delete()

    def test_nickname_lenght(self):
        with self.assertRaises(ValidationError):
            self.assertEqual(len(sample_account(nickname="a" * 50).nickname))

    def test_phonenumber_validation(self):
        with self.assertRaises(TypeError):
            self.assertEqual(sample_account(phone_number=+8392948421111).phone_number)

    def test_email_validation(self):
        with self.assertRaises(ValidationError):
            self.assertEqual(sample_account(email="Anton").email)

    def test_correct_phonenumber(self):
        self.assertEqual(sample_account(phone_number="+380957662083").phone_number, "+380957662083")
