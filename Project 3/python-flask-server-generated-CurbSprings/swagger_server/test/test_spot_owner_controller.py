# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.spot_owner import SpotOwner  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSpotOwnerController(BaseTestCase):
    """SpotOwnerController integration test stubs"""

    def test_add_spot_owner(self):
        """Test case for add_spot_owner

        Add a new spot owner
        """
        body = SpotOwner()
        response = self.client.open(
            '/spotowner',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
