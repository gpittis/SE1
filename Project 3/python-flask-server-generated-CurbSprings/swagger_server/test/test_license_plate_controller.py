# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.license_plate import LicensePlate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLicensePlateController(BaseTestCase):
    """LicensePlateController integration test stubs"""

    def test_modify_plate(self):
        """Test case for modify_plate

        Modify vehicle's license plate
        """
        body = LicensePlate()
        response = self.client.open(
            '/licensePlate',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_plate(self):
        """Test case for register_plate

        Register vehicle's license plate
        """
        body = LicensePlate()
        response = self.client.open(
            '/licensePlate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
