from ...task.channels._ao_channel import AOChannel
from ...task.collections._channel_collection import ChannelCollection
from ..._base_interpreter import BaseInterpreter
from ...constants import CurrentUnits, FuncGenType, VoltageUnits
from ..._lib import TaskHandle

class AOChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: BaseInterpreter
    ) -> None: ...
    def _create_chan(
        self, physical_channel: str = "", name_to_assign_to_channel: str = ""
    ) -> AOChannel: ...
    def add_ao_current_chan(
        self,
        physical_channel: str = "",
        name_to_assign_to_channel: str = "",
        min_val: float = 0.0,
        max_val: float = 0.02,
        units: CurrentUnits = CurrentUnits.AMPS,
        custom_scale_name: str = "",
    ) -> AOChannel: ...
    def add_ao_func_gen_chan(
        self,
        physical_channel: str = "",
        name_to_assign_to_channel: str = "",
        type: FuncGenType = FuncGenType.SINE,
        freq: float = 1000.0,
        amplitude: float = 5.0,
        offset: float = 0.0,
    ) -> AOChannel: ...
    def add_ao_voltage_chan(
        self,
        physical_channel: str = "",
        name_to_assign_to_channel: str = "",
        min_val: float = -10.0,
        max_val: float = 10.0,
        units: VoltageUnits = VoltageUnits.VOLTS,
        custom_scale_name: str = "",
    ) -> AOChannel: ...
