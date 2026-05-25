from enum import IntEnum
import grpc  # type: ignore

GRPC_SERVICE_INTERFACE_NAME = "nidaqmx_grpc.NiDAQmx"
MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY = "147D9BA7-BE75-4B29-8591-BA4A737AA8CF"

class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    INITIALIZE_SERVER_SESSION = 1
    ATTACH_TO_SERVER_SESSION = 2

class GrpcSessionOptions:
    def __init__(
        self,
        grpc_channel: grpc.Channel,
        session_name: str,
        *,
        api_key: str = MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None: ...
