from unittest import TestCase

from rest_framework.request import Request
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.test import APIClient

from core.utils.samples import sample_account


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_first = sample_account(email="example10@gmail.com")
        self.customer_first.save()

        self.customer_second = sample_account(email="example11@gmail.com")
        self.customer_second.save()

    def tearDown(self):
        self.customer_first.delete()
        self.customer_second.delete()

    def test_subscribtions(self):
        self.customer_first.subscribtions.add(self.customer_second)
        instance = self.customer_first.subscribtions.get(email=self.customer_second.email).email
        self.assertEqual(instance, "example11@gmail.com")

    def test_authenticated_no_admin_delete_custumer(self):
        self.client.force_authenticate(self.customer_first)
        request = self.client.get(reverse("api:delete-customer", kwargs={"pk": self.customer_second.pk}))
        self.assertEqual(request.status_code, 403)

    def test_authenticated_admin_delete_custumer(self):
        self.customer_first.is_superuser = True
        self.customer_first.save()
        self.client.force_authenticate(self.customer_first)
        request = self.client.get(reverse("api:delete-customer", kwargs={"pk": self.customer_second.pk}))
        self.assertEqual(request.status_code, 200)

    def test_no_authenticated_access_battles_for_all(self):
        request = self.client.get(reverse("api:battles-list"))
        self.assertEqual(request.status_code, 401)

    def test_authenticated_access_battles_for_all(self):
        self.client.force_authenticate(self.customer_first)
        request = self.client.get(reverse("api:battles-list"))
        self.assertEqual(request.status_code, 200)
