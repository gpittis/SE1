import connexion
import six

from swagger_server.models.spot_owner import SpotOwner  # noqa: E501
from swagger_server import util


def add_spot_owner(body):  # noqa: E501
    """Add a new spot owner

    FR15: The system administrator must be able to add a spot owner to the system # noqa: E501

    :param body: Spot owner object to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SpotOwner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
