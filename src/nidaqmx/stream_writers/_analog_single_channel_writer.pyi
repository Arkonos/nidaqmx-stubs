from typing import Any
from numpy import ndarray

from nitypes.waveform import AnalogWaveform

from .._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from ..stream_writers._channel_writer_base import ChannelWriterBase

class AnalogSingleChannelWriter(ChannelWriterBase):
    def write_many_sample(self, data: ndarray, timeout: float = 10.0) -> int: ...
    def write_one_sample(self, data: float, timeout: float = 10) -> None: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(
        self, waveform: AnalogWaveform[Any], timeout: float = 10.0
    ) -> int: ...
