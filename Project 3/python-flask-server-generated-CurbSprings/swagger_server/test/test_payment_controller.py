# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.payment import Payment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPaymentController(BaseTestCase):
    """PaymentController integration test stubs"""

    def test_make_payment(self):
        """Test case for make_payment

        Process a payment through the payment gateway
        """
        body = Payment()
        response = self.client.open(
            '/payment',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
