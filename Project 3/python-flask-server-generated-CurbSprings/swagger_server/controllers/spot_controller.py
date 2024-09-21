import connexion
import six

from swagger_server.models.parking_spot import ParkingSpot  # noqa: E501
from swagger_server import util


def create_spot(body):  # noqa: E501
    """Add a new parking spot

    FR12: The spot owner must be able to add a new parking spot to the system # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ParkingSpot.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_spots():  # noqa: E501
    """Retrieve all available parking spots

    FR1: The user must be able to view all available parking spots # noqa: E501


    :rtype: List[ParkingSpot]
    """
    return 'do some magic!'


def modify_spot(body, address, type, charger, id):  # noqa: E501
    """Modify the information of a specific parking spot

    FR13: The spot owner must be able to modify the information of their spots # noqa: E501

    :param body: Parking spot object to update
    :type body: dict | bytes
    :param address: 
    :type address: str
    :param type: 
    :type type: str
    :param charger: 
    :type charger: bool
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = ParkingSpot.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def remove_spot(id):  # noqa: E501
    """Remove a specific parking spot from the system

    FR14: The spot owner must be able to remove a spot from the system # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def search_spot(address, type, charger):  # noqa: E501
    """Search for available parking spots

    FR2: The user must be able to search for available parking spots in the system # noqa: E501

    :param address: 
    :type address: str
    :param type: 
    :type type: str
    :param charger: 
    :type charger: bool

    :rtype: List[ParkingSpot]
    """
    return 'do some magic!'
