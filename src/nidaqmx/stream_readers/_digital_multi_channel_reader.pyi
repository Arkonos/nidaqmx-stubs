from nitypes.waveform import DigitalWaveform
from nitypes.waveform.typing import TDigitalState
from numpy import ndarray
from .._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from ..constants import READ_ALL_AVAILABLE, ReallocationPolicy
from ..stream_readers._channel_reader_base import ChannelReaderBase

class DigitalMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more digital input channels in an NI-DAQmx task."""

    def read_many_sample_port_byte(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_port_uint16(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_many_sample_port_uint32(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample_multi_line(
        self, data: ndarray, timeout: float = 10
    ) -> None: ...
    def read_one_sample_one_line(self, data: ndarray, timeout: float = 10) -> None: ...
    def read_one_sample_port_byte(self, data: ndarray, timeout: float = 10) -> None: ...
    def read_one_sample_port_uint16(
        self, data: ndarray, timeout: float = 10
    ) -> None: ...
    def read_one_sample_port_uint32(
        self, data: ndarray, timeout: float = 10
    ) -> None: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveforms(
        self,
        waveforms: list[DigitalWaveform[TDigitalState]],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int: ...
