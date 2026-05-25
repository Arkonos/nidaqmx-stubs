from ...constants import Level, WatchdogAOExpirState, WatchdogCOExpirState
from ..physical_channel import PhysicalChannel
from ..._base_interpreter import BaseInterpreter
from ..._lib import TaskHandle

class ExpirationState:
    """
    Represents a DAQmx Watchdog expiration state.
    """

    __slots__ = ("_handle", "_physical_channel", "_interpreter")

    def __init__(
        self,
        task_handle: TaskHandle,
        physical_channel: PhysicalChannel,
        interpreter: BaseInterpreter,
    ) -> None: ...
    @property
    def ao_output_type(self) -> WatchdogAOExpirState: ...
    @ao_output_type.setter
    def ao_output_type(self, val: WatchdogAOExpirState) -> None: ...
    @ao_output_type.deleter
    @property
    def ao_state(self) -> float: ...
    @ao_state.setter
    def ao_state(self, val: float) -> None: ...
    @ao_state.deleter
    def ao_state(self) -> None: ...
    @property
    def co_state(self) -> WatchdogCOExpirState: ...
    @co_state.setter
    def co_state(self, val: WatchdogCOExpirState) -> None: ...
    @co_state.deleter
    def co_state(self) -> None: ...
    @property
    def do_state(self) -> Level: ...
    @do_state.setter
    def do_state(self, val: Level) -> None: ...
    @do_state.deleter
    def do_state(self) -> None: ...
