from ...task.channels._co_channel import COChannel
from ...task.collections._channel_collection import ChannelCollection
from ...constants import FrequencyUnits, Level, TimeUnits
from ..._grpc_interpreter import GrpcStubInterpreter
from ..._lib import TaskHandle

class COChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: GrpcStubInterpreter
    ) -> None: ...
    def _create_chan(
        self, counter: str, name_to_assign_to_channel: str = ""
    ) -> COChannel: ...
    def add_co_pulse_chan_freq(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        units: FrequencyUnits = FrequencyUnits.HZ,
        idle_state: Level = Level.LOW,
        initial_delay: float = 0.0,
        freq: float = 1.0,
        duty_cycle: float = 0.5,
    ) -> COChannel: ...
    def add_co_pulse_chan_ticks(
        self,
        counter: str,
        source_terminal: str,
        name_to_assign_to_channel: str = "",
        idle_state: Level = Level.LOW,
        initial_delay: int = 0,
        low_ticks: int = 100,
        high_ticks: int = 100,
    ) -> COChannel: ...
    def add_co_pulse_chan_time(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        units: TimeUnits = TimeUnits.SECONDS,
        idle_state: Level = Level.LOW,
        initial_delay: float = 0.0,
        low_time: float = 0.01,
        high_time: float = 0.01,
    ) -> COChannel: ...
