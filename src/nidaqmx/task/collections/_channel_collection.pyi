from collections.abc import Sequence

from ...task.channels._channel import Channel
from ..._base_interpreter import BaseInterpreter
from ..._lib import TaskHandle

class ChannelCollection(Sequence[Channel]):
    """
    Contains the collection of channels for a DAQmx Task.

    This class defines methods that implements a container object.
    """
    def __init__(
        self, task_handle: TaskHandle, interpreter: BaseInterpreter
    ) -> None: ...
    @property
    def all(self) -> Channel: ...
    @property
    def channel_names(self) -> list[str]: ...
