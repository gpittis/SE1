# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.reservation import Reservation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReservationController(BaseTestCase):
    """ReservationController integration test stubs"""

    def test_delete_reservation(self):
        """Test case for delete_reservation

        Cancel a specific reservation
        """
        response = self.client.open(
            '/reservation/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_make_reservation(self):
        """Test case for make_reservation

        Create a new reservation
        """
        body = Reservation()
        response = self.client.open(
            '/reservation',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_modify_reservation(self):
        """Test case for modify_reservation

        Modify a specific reservation
        """
        body = Reservation()
        query_string = [('spot_id', 56),
                        ('user_id', 56),
                        ('start_time', '2013-10-20T19:20:30+01:00'),
                        ('duration', '2013-10-20T19:20:30+01:00'),
                        ('_date', '2013-10-20')]
        response = self.client.open(
            '/reservation/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
