# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.parking_spot import ParkingSpot  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSpotController(BaseTestCase):
    """SpotController integration test stubs"""

    def test_create_spot(self):
        """Test case for create_spot

        Add a new parking spot
        """
        body = ParkingSpot()
        response = self.client.open(
            '/spot',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_spots(self):
        """Test case for get_spots

        Retrieve all available parking spots
        """
        response = self.client.open(
            '/spot',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_spot(self):
        """Test case for modify_spot

        Modify the information of a specific parking spot
        """
        body = ParkingSpot()
        query_string = [('address', 'address_example'),
                        ('type', 'type_example'),
                        ('charger', true)]
        response = self.client.open(
            '/spot/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_spot(self):
        """Test case for remove_spot

        Remove a specific parking spot from the system
        """
        response = self.client.open(
            '/spot/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_spot(self):
        """Test case for search_spot

        Search for available parking spots
        """
        query_string = [('address', 'address_example'),
                        ('type', 'type_example'),
                        ('charger', true)]
        response = self.client.open(
            '/spot/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
