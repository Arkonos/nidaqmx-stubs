from numpy import ndarray
from ..task._task import Task

class ChannelReaderBase:
    """Defines base class for all NI-DAQmx stream readers."""

    def __init__(self, task_in_stream: Task) -> None: ...
    @property
    def verify_array_shape(self) -> bool: ...
    @verify_array_shape.setter
    def verify_array_shape(self, val: bool) -> None: ...
    def _verify_array(
        self,
        data: ndarray,
        number_of_samples_per_channel: int,
        is_many_chan: bool,
        is_many_samp: bool,
    ) -> None: ...
    def _verify_array_digital_lines(
        self, data: ndarray, is_many_chan: bool, is_many_line: bool
    ) -> None: ...
