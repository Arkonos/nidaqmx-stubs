from ...system._watchdog_modules.expiration_state import ExpirationState
from ..._grpc_interpreter import GrpcStubInterpreter
from ..._lib import TaskHandle

class ExpirationStatesCollection:
    def __init__(
        self, task_handle: TaskHandle, interpreter: GrpcStubInterpreter
    ) -> None: ...
    def __getitem__(self, index: str) -> ExpirationState: ...
