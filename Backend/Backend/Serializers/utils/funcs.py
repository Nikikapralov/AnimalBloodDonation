from rest_framework.utils.serializer_helpers import ReturnDict
from Backend.AnimalBloodDonationBE.models import Owner


def get_value_from_model_pk(data: ReturnDict, model: object, key: str) -> object:
    """
    Get a query results from a model based on pk.
    @param data: ReturnDict instance of data to extract the PK from.
    @param model: Model to be queried and extract the filtered by PK results
    @param key: ReturnDict key to be queried.
    @return: Returns an instance of the model with filtered items.
    """
    pk = data[key]
    result = model.objects.get(pk=pk)
    return result


def get_sender(data: ReturnDict, model: Owner, key: str) -> str:
    """
    Gets the sender.
    @param data: ReturnDict instance with the data information.
    @param model: Model to extract the sender from.
    @param key: Key to query the "data" for the "pk"
    @return: Returns the sender name.
    """
    data = get_value_from_model_pk(data, model, key)
    sender_name = data.__str__()
    return sender_name


def get_recipient(data: ReturnDict, model: Owner, key: str) -> str:
    """
    Gets the recipient.
    @param data: ReturnDict instance with the data information.
    @param model: Model to extract the sender from.
    @param key: Key to query the "data" for the "pk"
    @return: Returns the recipient name
    """
    data = get_value_from_model_pk(data, model, key)
    recipient_name = data.__str__()
    return recipient_name