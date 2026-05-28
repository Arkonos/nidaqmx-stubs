from ...system._watchdog_modules.expiration_state import ExpirationState
from ..._base_interpreter import BaseInterpreter
from ..._lib import TaskHandle

class ExpirationStatesCollection:
    def __init__(
        self, task_handle: TaskHandle, interpreter: BaseInterpreter
    ) -> None: ...
    def __getitem__(self, index: str) -> ExpirationState: ...
