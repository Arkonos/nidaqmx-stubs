from numpy import ndarray, float64
from nitypes.waveform import AnalogWaveform

from .._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from ..constants import READ_ALL_AVAILABLE, ReallocationPolicy
from ..stream_readers._channel_reader_base import ChannelReaderBase

class AnalogMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more analog input channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        data: ndarray,
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> int: ...
    def read_one_sample(self, data: ndarray, timeout: float = 10) -> None: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveforms(
        self,
        waveforms: list[AnalogWaveform[float64]],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int: ...
