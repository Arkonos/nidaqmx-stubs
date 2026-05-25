from numpy import ndarray
from ..constants import READ_ALL_AVAILABLE
from ..stream_readers._channel_reader_base import ChannelReaderBase
from ..types import CtrFreq, CtrTick, CtrTime

class CounterReader(ChannelReaderBase):
    def read_many_sample_double(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_pulse_frequency(
        self,
        frequencies: ndarray,
        duty_cycles: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_pulse_ticks(
        self,
        high_ticks: ndarray,
        low_ticks: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_pulse_time(
        self,
        high_times: ndarray,
        low_times: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_uint32(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample_double(self, timeout: float = 10) -> float: ...
    def read_one_sample_pulse_frequency(self, timeout: float = 10) -> CtrFreq: ...
    def read_one_sample_pulse_ticks(self, timeout: float = 10) -> CtrTick: ...
    def read_one_sample_pulse_time(self, timeout: float = 10) -> CtrTime: ...
    def read_one_sample_uint32(self, timeout: float = 10) -> int: ...
