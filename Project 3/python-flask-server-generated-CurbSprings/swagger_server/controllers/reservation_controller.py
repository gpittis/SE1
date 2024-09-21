import connexion
import six

from swagger_server.models.reservation import Reservation  # noqa: E501
from swagger_server import util


def delete_reservation(id):  # noqa: E501
    """Cancel a specific reservation

    FR7: The user must be able to manage their reservation in the system # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def make_reservation(body):  # noqa: E501
    """Create a new reservation

    FR6: The user must be able to reserve a parking spot # noqa: E501

    :param body: Reservation object to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Reservation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def modify_reservation(body, spot_id, user_id, start_time, duration, _date, id):  # noqa: E501
    """Modify a specific reservation

    FR7: The user must be able to manage their reservation in the system # noqa: E501

    :param body: Reservation object to update
    :type body: dict | bytes
    :param spot_id: 
    :type spot_id: int
    :param user_id: 
    :type user_id: int
    :param start_time: 
    :type start_time: str
    :param duration: 
    :type duration: str
    :param _date: 
    :type _date: str
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Reservation.from_dict(connexion.request.get_json())  # noqa: E501
    start_time = util.deserialize_datetime(start_time)
    duration = util.deserialize_datetime(duration)
    _date = util.deserialize_date(_date)
    return 'do some magic!'
