from ...task.channels._ci_channel import CIChannel
from ...task.collections._channel_collection import ChannelCollection
from ..._grpc_interpreter import GrpcStubInterpreter
from ..._lib import TaskHandle
from ...constants import (
    AngleUnits,
    AngularVelocityUnits,
    CountDirection,
    CounterFrequencyMethod,
    Edge,
    EncoderType,
    EncoderZIndexPhase,
    FrequencyUnits,
    GpsSignalType,
    LengthUnits,
    TimeUnits,
    VelocityUnits,
)

class CIChannelCollection(ChannelCollection):
    def __init__(
        self, task_handle: TaskHandle, interpreter: GrpcStubInterpreter
    ) -> None: ...
    def _create_chan(
        self, counter: str, name_to_assign_to_channel: str = ""
    ) -> CIChannel: ...
    def add_ci_ang_encoder_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        decoding_type: EncoderType = EncoderType.X_4,
        zidx_enable: bool = False,
        zidx_val: float = 0,
        zidx_phase: EncoderZIndexPhase = EncoderZIndexPhase.AHIGH_BHIGH,
        units: AngleUnits = AngleUnits.DEGREES,
        pulses_per_rev: int = 24,
        initial_angle: float = 0.0,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_ang_velocity_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.0,
        max_val: float = 1.0,
        decoding_type: EncoderType = EncoderType.X_4,
        units: AngularVelocityUnits = AngularVelocityUnits.RPM,
        pulses_per_rev: int = 24,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_count_edges_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        edge: Edge = Edge.RISING,
        initial_count: int = 0,
        count_direction: CountDirection = CountDirection.COUNT_UP,
    ) -> CIChannel: ...
    def add_ci_duty_cycle_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_freq: float = 2.0,
        max_freq: float = 10000.0,
        edge: Edge = Edge.RISING,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_freq_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 2.0,
        max_val: float = 100.0,
        units: FrequencyUnits = FrequencyUnits.HZ,
        edge: Edge = Edge.RISING,
        meas_method: CounterFrequencyMethod = CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER,
        meas_time: float = 0.001,
        divisor: int = 4,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_gps_timestamp_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        units: TimeUnits = TimeUnits.SECONDS,
        sync_method: GpsSignalType = GpsSignalType.IRIGB,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_lin_encoder_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        decoding_type: EncoderType = EncoderType.X_4,
        zidx_enable: bool = False,
        zidx_val: float = 0,
        zidx_phase: EncoderZIndexPhase = EncoderZIndexPhase.AHIGH_BHIGH,
        units: LengthUnits = LengthUnits.METERS,
        dist_per_pulse: float = 0.001,
        initial_pos: float = 0.0,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_lin_velocity_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.0,
        max_val: float = 1.0,
        decoding_type: EncoderType = EncoderType.X_4,
        units: VelocityUnits = VelocityUnits.METERS_PER_SECOND,
        dist_per_pulse: float = 0.001,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_period_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.000001,
        max_val: float = 0.1,
        units: TimeUnits = TimeUnits.SECONDS,
        edge: Edge = Edge.RISING,
        meas_method: CounterFrequencyMethod = CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER,
        meas_time: float = 0.001,
        divisor: int = 4,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_pulse_chan_freq(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 1000,
        max_val: float = 1000000,
        units: FrequencyUnits = FrequencyUnits.HZ,
    ) -> CIChannel: ...
    def add_ci_pulse_chan_ticks(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        source_terminal: str = "OnboardClock",
        min_val: float = 1000,
        max_val: float = 1000000,
    ) -> CIChannel: ...
    def add_ci_pulse_chan_time(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.000001,
        max_val: float = 0.001,
        units: TimeUnits = TimeUnits.SECONDS,
    ) -> CIChannel: ...
    def add_ci_pulse_width_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.000001,
        max_val: float = 0.1,
        units: TimeUnits = TimeUnits.SECONDS,
        starting_edge: Edge = Edge.RISING,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_semi_period_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.000001,
        max_val: float = 0.1,
        units: TimeUnits = TimeUnits.SECONDS,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
    def add_ci_two_edge_sep_chan(
        self,
        counter: str,
        name_to_assign_to_channel: str = "",
        min_val: float = 0.000001,
        max_val: float = 1.0,
        units: TimeUnits = TimeUnits.SECONDS,
        first_edge: Edge = Edge.RISING,
        second_edge: Edge = Edge.FALLING,
        custom_scale_name: str = "",
    ) -> CIChannel: ...
