from numpy import ndarray
from ..constants import READ_ALL_AVAILABLE
from ..stream_readers._channel_reader_base import ChannelReaderBase

class AnalogUnscaledReader(ChannelReaderBase):
    """Reads unscaled samples from one or more analog input channels in an NI-DAQmx task."""

    def read_int16(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_int32(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_uint16(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_uint32(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
