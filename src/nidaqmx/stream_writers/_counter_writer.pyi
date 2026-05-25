from numpy import ndarray
from ..stream_writers._channel_writer_base import ChannelWriterBase

class CounterWriter(ChannelWriterBase):
    """Writes samples to a counter output channel in an NI-DAQmx task."""

    def write_many_sample_pulse_frequency(
        self, frequencies: ndarray, duty_cycles: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_many_sample_pulse_ticks(
        self, high_ticks: ndarray, low_ticks: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_many_sample_pulse_time(
        self, high_times: ndarray, low_times: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_one_sample_pulse_frequency(
        self, frequency: float, duty_cycle: float, timeout: float = 10
    ) -> None: ...
    def write_one_sample_pulse_ticks(
        self, high_ticks: float, low_ticks: float, timeout: float = 10
    ) -> None: ...
    def write_one_sample_pulse_time(
        self, high_time: float, low_time: float, timeout: float = 10
    ) -> None: ...
