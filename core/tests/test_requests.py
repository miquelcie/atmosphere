"""
"""
from django.test import TestCase

from core.models.request import AllocationRequest, QuotaRequest
from core.models.status_type import get_status_type


class TestAllocationRequest(TestCase):
    def setUp(self):
        self.status = get_status_type()
        self.message = "Allocation admin message"
        self.request = "Allocation of size x"
        self.blank_request = AllocationRequest(
            admin_message=self.message, request=self.request,
            status=self.status)

    def test_blank_request(self):
        self.assertEquals(self.blank_request.admin_message, self.message)
        self.assertEquals(self.blank_request.status, self.status)
        self.assertEquals(
            self.blank_request.request, self.request)


class TestQuotaRequest(TestCase):
    def setUp(self):
        self.status = get_status_type()
        self.message = "Quota admin message"
        self.request = "Quota x"
        self.blank_request = QuotaRequest(
            admin_message=self.message, request=self.request,
            status=self.status)

    def test_blank_request(self):
        self.assertEquals(self.blank_request.admin_message, self.message)
        self.assertEquals(self.blank_request.status, self.status)
        self.assertEquals(
            self.blank_request.request, self.request)
