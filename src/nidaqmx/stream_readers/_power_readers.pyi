from numpy import ndarray
from ..constants import READ_ALL_AVAILABLE
from ..stream_readers._channel_reader_base import ChannelReaderBase

class PowerSingleChannelReader(ChannelReaderBase):
    """Reads samples from an analog input power channel in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data: ndarray,
        current_data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample(self, timeout: float = 10) -> float: ...

class PowerMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data: ndarray,
        current_data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample(
        self, voltage_data: ndarray, current_data: ndarray, timeout: float = 10
    ) -> None: ...

class PowerBinaryReader(ChannelReaderBase):
    """Reads binary samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data: ndarray,
        current_data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
