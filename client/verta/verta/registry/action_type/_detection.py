from ..._protos.public.registry import RegistryService_pb2

from . import _ActionType


class Detection(_ActionType):
    """
    Detection action of the registered model.

    Examples
    --------
    .. code-block:: python

        from verta.registry import action_type
        reg_model = client.create_registered_model("My Model", workspace="my-org", action_type=action_type.Detection())

    """

    _ACTION_TYPE = RegistryService_pb2.ActionTypeEnum.ActionType.DETECTION