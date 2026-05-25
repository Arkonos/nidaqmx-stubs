from ...task.channels._do_channel import DOChannel
from ...task.collections._channel_collection import ChannelCollection
from ...constants import LineGrouping
from ..._grpc_interpreter import GrpcStubInterpreter
from ..._lib import TaskHandle

class DOChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: GrpcStubInterpreter
    ) -> None: ...
    def _create_chan(
        self,
        lines: str,
        line_grouping: LineGrouping = LineGrouping.CHAN_FOR_ALL_LINES,
        name_to_assign_to_lines: str = "",
    ) -> DOChannel: ...
    def add_do_chan(
        self,
        lines: str,
        name_to_assign_to_lines: str = "",
        line_grouping: LineGrouping = LineGrouping.CHAN_FOR_ALL_LINES,
    ) -> DOChannel: ...
