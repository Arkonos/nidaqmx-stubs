from typing import NamedTuple
from .constants import (
    Level,
    PowerUpChannelType,
    PowerUpStates,
    ResistorState,
    WatchdogAOExpirState,
    WatchdogCOExpirState,
)

# region Task Counter IO namedtuples
class CtrFreq(NamedTuple):
    freq: float
    duty_cycle: float

class CtrTick(NamedTuple):
    high_tick: float
    low_tick: float

class CtrTime(NamedTuple):
    high_time: float
    low_time: float

# endregion

# region Power IO namedtuples

class PowerMeasurement(NamedTuple):
    voltage: float
    current: float

# endregion

# region Watchdog namedtuples

class AOExpirationState(NamedTuple):
    physical_channel: str
    expiration_state: float
    output_type: WatchdogAOExpirState

class COExpirationState(NamedTuple):
    physical_channel: str
    expiration_state: WatchdogCOExpirState

class DOExpirationState(NamedTuple):
    physical_channel: str
    expiration_state: Level

# endregion

# region Power Up States namedtuples

class AOPowerUpState(NamedTuple):
    physical_channel: str
    power_up_state: float
    channel_type: PowerUpChannelType

class DOPowerUpState(NamedTuple):
    physical_channel: str
    power_up_state: PowerUpStates

class DOResistorPowerUpState(NamedTuple):
    physical_channel: str
    power_up_state: ResistorState

# endregion

# region System namedtuples

class CDAQSyncConnection(NamedTuple):
    output_port: str
    input_port: str

class DriverVersion(NamedTuple):
    major_version: str
    minor_version: str
    update_version: str

# endregion

# region ID Pin namedtuples

class IDPinContents(NamedTuple):
    """IDPinContents represent the contents of the memory connected to the ID pin."""

    data: list[int]
    """The binary data stored on the memory connected to the ID pin."""

    format_code: int
    """The format code of the binary data."""

# endregion
