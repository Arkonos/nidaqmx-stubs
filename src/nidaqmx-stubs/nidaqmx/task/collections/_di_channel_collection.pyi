from ...task.channels._di_channel import DIChannel
from ...task.collections._channel_collection import ChannelCollection
from ..._grpc_interpreter import GrpcStubInterpreter
from ...constants import LineGrouping
from ..._lib import TaskHandle

class DIChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: GrpcStubInterpreter
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
