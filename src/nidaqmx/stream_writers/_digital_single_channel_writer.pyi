from typing import Any
from numpy import ndarray
from nitypes.waveform import DigitalWaveform

from .._feature_toggles import WAVEFORM_SUPPORT, requires_feature

from ..stream_writers._channel_writer_base import ChannelWriterBase

class DigitalSingleChannelWriter(ChannelWriterBase):
    """Writes samples to a single digital output channel in an NI-DAQmx task."""

    def write_many_sample_port_byte(
        self, data: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_many_sample_port_uint16(
        self, data: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_many_sample_port_uint32(
        self, data: ndarray, timeout: float = 10.0
    ) -> int: ...
    def write_one_sample_multi_line(
        self, data: ndarray, timeout: float = 10
    ) -> int: ...
    def write_one_sample_one_line(self, data: int, timeout: float = 10) -> None: ...
    def write_one_sample_port_byte(self, data: int, timeout: float = 10) -> None: ...
    def write_one_sample_port_uint16(self, data: int, timeout: float = 10) -> None: ...
    def write_one_sample_port_uint32(self, data: int, timeout: float = 10) -> None: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(
        self, waveform: DigitalWaveform[Any], timeout: float = 10.0
    ) -> int: ...
