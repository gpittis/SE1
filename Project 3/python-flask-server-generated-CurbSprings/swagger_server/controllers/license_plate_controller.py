import connexion
import six

from swagger_server.models.license_plate import LicensePlate  # noqa: E501
from swagger_server import util


def modify_plate(body):  # noqa: E501
    """Modify vehicle&#x27;s license plate

    FR5: The user must be able to modify their vehicle&#x27;s license plate in the system # noqa: E501

    :param body: License plate object to update
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LicensePlate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_plate(body):  # noqa: E501
    """Register vehicle&#x27;s license plate

    FR4: The user must be able to register their vehicle&#x27;s license plate in the system # noqa: E501

    :param body: License plate to register
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = LicensePlate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
