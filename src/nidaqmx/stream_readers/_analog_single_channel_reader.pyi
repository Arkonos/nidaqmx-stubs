from numpy import ndarray, float64
from nitypes.waveform import AnalogWaveform

from .._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from ..constants import READ_ALL_AVAILABLE, ReallocationPolicy
from ..stream_readers._channel_reader_base import ChannelReaderBase

class AnalogSingleChannelReader(ChannelReaderBase):
    """Reads samples from an analog input channel in an NI-DAQmx task."""

    def read_many_sample(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample(self, timeout: float = 10) -> float: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self,
        waveform: AnalogWaveform[float64],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int: ...
