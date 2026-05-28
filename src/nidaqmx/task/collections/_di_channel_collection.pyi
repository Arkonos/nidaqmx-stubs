from ...task.channels._di_channel import DIChannel
from ...task.collections._channel_collection import ChannelCollection
from ..._base_interpreter import BaseInterpreter
from ...constants import LineGrouping
from ..._lib import TaskHandle

class DIChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: BaseInterpreter
    ) -> None: ...
    def _create_chan(
        self,
        lines: str,
        line_grouping: LineGrouping = LineGrouping.CHAN_FOR_ALL_LINES,
        name_to_assign_to_lines: str = "",
    ) -> DIChannel: ...
    def add_di_chan(
        self,
        lines: str,
        name_to_assign_to_lines: str = "",
        line_grouping: LineGrouping = LineGrouping.CHAN_FOR_ALL_LINES,
    ) -> DIChannel: ...
