import connexion
import six

from swagger_server.models.payment import Payment  # noqa: E501
from swagger_server import util


def make_payment(body):  # noqa: E501
    """Process a payment through the payment gateway

    FR8: The user must be able to make a payment through the payment gateway # noqa: E501

    :param body: Payment object to process
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Payment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
