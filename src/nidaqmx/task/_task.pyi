from types import TracebackType
from typing import Any, Callable, NoReturn, Sequence
from datetime import datetime
from enum import Enum
import numpy as np
from numpy.typing import NDArray
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from ..grpc_session_options import GrpcSessionOptions
from ..task._in_stream import InStream
from ..task._out_stream import OutStream
from ..task._timing import Timing
from ..system.device import Device
from ..task.collections._ai_channel_collection import AIChannelCollection
from ..task.collections._ao_channel_collection import AOChannelCollection
from ..task.collections._ci_channel_collection import CIChannelCollection
from ..task.collections._co_channel_collection import COChannelCollection
from ..task.collections._di_channel_collection import DIChannelCollection
from ..task.collections._do_channel_collection import DOChannelCollection
from ..task._export_signals import ExportSignals
from ..task.channels._channel import Channel
from ..task.triggering import Triggers
from .._lib import TaskHandle
from .._base_interpreter import BaseInterpreter
from ..system.storage.persisted_channel import PersistedChannel
from .._feature_toggles import requires_feature, WAVEFORM_SUPPORT
from ..types import CtrFreq, CtrTick, CtrTime, PowerMeasurement
from ..constants import (
    READ_ALL_AVAILABLE,
    ShuntCalSelect,
    ShuntCalSource,
    ShuntElementLocation,
    Signal,
    TaskMode,
    TimestampEvent,
    UsageTypeCI,
)

__all__ = ["Task"]

class UnsetNumSamplesSentinel: ...
class UnsetAutoStartSentinel: ...

NUM_SAMPLES_UNSET = UnsetNumSamplesSentinel()
AUTO_START_UNSET = UnsetAutoStartSentinel()

class Task:
    __slots__ = (
        "_handle",
        "_close_on_exit",
        "_saved_name",
        "_grpc_options",
        "_event_handlers",
        "_interpreter",
        "_ai_channels",
        "_ao_channels",
        "_ci_channels",
        "_co_channels",
        "_di_channels",
        "_do_channels",
        "_export_signals",
        "_in_stream",
        "_timing",
        "_triggers",
        "_out_stream",
        "_event_handler_lock",
        "__weakref__",
    )

    def __init__(
        self, new_task_name: str = "", *, grpc_options: GrpcSessionOptions | None = None
    ) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> Task: ...
    def __eq__(self, other: Any) -> bool: ...
    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def channels(self) -> Channel: ...
    @property
    def channel_names(self) -> list[str]: ...
    @property
    def number_of_channels(self) -> int: ...
    @property
    def devices(self) -> Device: ...
    @property
    def number_of_devices(self) -> int: ...
    @property
    def ai_channels(self) -> AIChannelCollection: ...
    @property
    def ao_channels(self) -> AOChannelCollection: ...
    @property
    def ci_channels(self) -> CIChannelCollection: ...
    @property
    def co_channels(self) -> COChannelCollection: ...
    @property
    def di_channels(self) -> DIChannelCollection: ...
    @property
    def do_channels(self) -> DOChannelCollection: ...
    @property
    def export_signals(self) -> ExportSignals: ...
    @property
    def in_stream(self) -> InStream: ...
    @property
    def out_stream(self) -> OutStream: ...
    @property
    def timing(self) -> Timing: ...
    @property
    def triggers(self) -> Triggers: ...
    def _initialize(
        self,
        task_handle: TaskHandle,
        interpreter: BaseInterpreter,
    ) -> None: ...
    def _calculate_num_samps_per_chan(self, num_samps_per_chan: int) -> int: ...
    def add_global_channels(self, global_channels: list[PersistedChannel]) -> None: ...
    def close(self) -> None: ...
    def control(self, action: TaskMode) -> None: ...
    def is_task_done(self) -> bool: ...
    def perform_bridge_offset_nulling_cal(
        self, channel: str = "", skip_unsupported_channels: bool = False
    ) -> None: ...
    def perform_strain_shunt_cal(
        self,
        channel: str = "",
        shunt_resistor_value: int = 100000,
        shunt_resistor_location: ShuntElementLocation = ShuntElementLocation.R3,
        shunt_resistor_select: ShuntCalSelect = ShuntCalSelect.A,
        shunt_resistor_source: ShuntCalSource = ShuntCalSource.DEFAULT,
        skip_unsupported_channels: bool = False,
    ) -> None: ...
    def perform_bridge_shunt_cal(
        self,
        channel: str = "",
        shunt_resistor_value: int = 100000,
        shunt_resistor_location: ShuntElementLocation = ShuntElementLocation.R3,
        shunt_resistor_select: ShuntCalSelect = ShuntCalSelect.A,
        shunt_resistor_source: ShuntCalSource = ShuntCalSource.DEFAULT,
        bridge_resistance: int = 120,
        skip_unsupported_channels: bool = False,
    ) -> None: ...
    def perform_thrmcpl_lead_offset_nulling_cal(
        self, channel: str = "", skip_unsupported_channels: bool = False
    ) -> None: ...
    def read(
        self,
        number_of_samples_per_channel: int
        | UnsetNumSamplesSentinel = NUM_SAMPLES_UNSET,
        timeout: float = 10.0,
    ) -> float | list[float] | list[list[float]]: ...
    def _read_ctr_pulse(
        self,
        array_shape: tuple[int, ...],
        meas_type: UsageTypeCI,
        number_of_channels: int,
        number_of_samples_per_channel: int,
        num_samples_not_set: bool,
        timeout: float,
    ) -> (
        CtrFreq | CtrTick | CtrTime | list[CtrFreq] | list[CtrTick] | list[CtrTime]
    ): ...
    def _read_power(
        self,
        array_shape: tuple[int, ...],
        number_of_channels: int,
        number_of_samples_per_channel: int,
        timeout: float,
    ) -> PowerMeasurement | list[PowerMeasurement] | list[list[PowerMeasurement]]: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self,
        number_of_samples_per_channel: int
        | UnsetNumSamplesSentinel = READ_ALL_AVAILABLE,
        timeout: float = 10.0,
    ) -> (
        AnalogWaveform[Any]
        | DigitalWaveform[Any]
        | list[AnalogWaveform[Any]]
        | list[DigitalWaveform[Any]]
    ): ...
    def register_done_event(self, callback_method: Callable[..., Any]) -> None: ...
    def register_every_n_samples_acquired_into_buffer_event(
        self, sample_interval: int, callback_method: Callable[..., Any]
    ) -> None: ...
    def register_every_n_samples_transferred_from_buffer_event(
        self, sample_interval: int, callback_method: Callable[..., Any]
    ) -> None: ...
    def register_signal_event(
        self, signal_type: Signal, callback_method: Callable[..., Any]
    ) -> None: ...
    def save(
        self,
        save_as: str = "",
        author: str = "",
        overwrite_existing_task: bool = False,
        allow_interactive_editing: bool = True,
        allow_interactive_deletion: bool = True,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def wait_for_valid_timestamp(
        self, timestamp_event: TimestampEvent, timeout: float = 10.0
    ) -> datetime: ...
    def wait_until_done(self, timeout: float = 10.0) -> None: ...
    def _raise_invalid_num_lines_error(
        self, num_lines_expected: int, num_lines_in_data: int
    ) -> NoReturn: ...
    def _raise_invalid_write_num_chans_error(
        self, number_of_channels: int, number_of_channels_in_data: int
    ) -> NoReturn: ...
    def _raise_invalid_write_mixed_data_error(self) -> NoReturn: ...
    def _raise_no_output_channels_error(self) -> NoReturn: ...
    def _raise_unsupported_output_type_error(self, output_type: type) -> NoReturn: ...
    def write(
        self,
        data: np.number
        | NDArray[np.number]
        | list[NDArray[np.number]]
        | list[list[np.number]],
        auto_start: bool | UnsetAutoStartSentinel = AUTO_START_UNSET,
        timeout: float = 10.0,
    ) -> int: ...
    def _is_waveform_data(
        self,
        data: AnalogWaveform[Any]
        | DigitalWaveform[Any]
        | list[AnalogWaveform[Any]]
        | list[DigitalWaveform[Any]],
    ) -> bool: ...
    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(
        self,
        waveforms: (
            AnalogWaveform[Any]
            | DigitalWaveform[Any]
            | Sequence[AnalogWaveform[Any]]
            | Sequence[DigitalWaveform[Any]]
        ),
        auto_start: bool | UnsetAutoStartSentinel = AUTO_START_UNSET,
        timeout: float = 10.0,
    ) -> int: ...

class _TaskAlternateConstructor(Task):
    def __init__(
        self,
        task_handle: TaskHandle,
        interpreter: BaseInterpreter,
        close_on_exit: bool,
    ) -> None: ...

class _TaskEventType(Enum):
    """Internal enum for task event bookkeeping."""

    DONE = 1
    EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER = 2
    EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER = 3
    SIGNAL = 4
