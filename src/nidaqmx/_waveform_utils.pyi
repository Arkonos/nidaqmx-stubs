from collections.abc import Sequence
from typing import Any

from nitypes.waveform import AnalogWaveform, DigitalWaveform

def get_num_samps_per_chan(
    waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]],
) -> int: ...
