from typing import Any, Callable, Literal, Mapping, Sequence
import pathlib
from datetime import datetime, timezone
from hightime import datetime as ht_datetime
from enum import Enum
from typing_extensions import TypeAlias
import numpy as np
from numpy.typing import NDArray
import ctypes
from .error_codes import DAQmxErrors
from ._base_interpreter import BaseEventHandler, BaseInterpreter
from ._lib import TaskHandle
from nitypes.waveform import AnalogWaveform, DigitalWaveform, ExtendedPropertyDictionary
from nitypes.waveform.typing import ExtendedPropertyValue
from .types import DriverVersion
from .constants import (
    AccelSensitivityUnits,
    AccelUnits,
    AcquisitionType,
    AngleUnits,
    AngularVelocityUnits,
    BridgeConfiguration,
    BridgeElectricalUnits,
    BridgePhysicalUnits,
    BridgeUnits,
    CJCSource,
    ChargeUnits,
    CountDirection,
    CounterFrequencyMethod,
    CurrentShuntResistorLocation,
    CurrentUnits,
    DigitalPatternCondition,
    Edge,
    EncoderType,
    EncoderZIndexPhase,
    EveryNSamplesEventType,
    ExcitationSource,
    FillMode,
    ForceUnits,
    FrequencyUnits,
    FuncGenType,
    GpsSignalType,
    LengthUnits,
    Level,
    LineGrouping,
    LoggingMode,
    LoggingOperation,
    LogicFamily,
    Polarity,
    PowerUnits,
    PowerUpStates,
    PressureUnits,
    RTDType,
    ResistanceConfiguration,
    ResistanceUnits,
    ShuntCalSelect,
    ShuntCalSource,
    ShuntElementLocation,
    Signal,
    SignalModifiers,
    Slope,
    SoundPressureUnits,
    StrainGageBridgeType,
    StrainGageRosetteMeasurementType,
    StrainGageRosetteType,
    StrainUnits,
    TEDSUnits,
    TaskMode,
    TemperatureUnits,
    TerminalConfiguration,
    ThermocoupleType,
    TimeUnits,
    Timescale,
    TorqueUnits,
    UnitsPreScaled,
    VelocityUnits,
    VoltageUnits,
    WDTTaskAction,
    WaveformAttributeMode,
    WindowTriggerCondition1,
    WriteBasicTEDSOptions,
)

_was_runtime_environment_set = None

_INT64_WFM_SEC_PER_TICK = 100e-9
_T0_EPOCH = ht_datetime(1, 1, 1, tzinfo=timezone.utc)

# typedef np.int32 (CVICALLBACK *DAQmxSetWfmAttrCallbackPtr)(uInt32 channelIndex, const char attributeName[], np.int32 attributeType, const void* value, uInt32 valueSizeInBytes, void *callbackData);  # noqa: W505 - doc line too long
# CSetWfmAttrCallbackPtr = ctypes.CFUNCTYPE(
#     ctypes.c_int32,  # return value (error code)
#     ctypes.c_uint32,  # channel_index
#     ctypes.c_char_p,  # attribute_name
#     ctypes.c_int32,  # attribute_type
#     ctypes.c_void_p,  # value
#     ctypes.c_uint32,  # value_size_in_bytes
#     ctypes.c_void_p,  # callback_data
# )

class CSetWfmAttrCallbackPtr:
    def __call__(
        self,
        channel_index: int,
        attribute_name: bytes,
        attribute_type: int,
        value: ctypes.c_void_p,
        value_size_in_bytes: int,
        callback_data: object,
    ) -> int: ...

class WfmAttrType(Enum):
    BOOL32 = 1
    FLOAT64 = 2
    INT32 = 3
    STRING = 4

SetWfmAttrCallback: TypeAlias = Callable[
    [int, str, WfmAttrType, ExtendedPropertyValue, object], int
]

class LibraryEventHandler(BaseEventHandler):
    def __init__(self, callback_method_ptr: object) -> None: ...
    def close(self) -> None: ...

class LibraryInterpreter(BaseInterpreter):
    def __init__(self) -> None: ...
    @property
    def driver_version(self) -> DriverVersion: ...
    def add_cdaq_sync_connection(self, port_list: str) -> None: ...
    def add_global_chans_to_task(
        self, task: TaskHandle, channel_names: str
    ) -> None: ...
    def add_network_device(
        self,
        ip_address: str,
        device_name: str,
        attempt_reservation: bool,
        timeout: float,
    ) -> str: ...
    def are_configured_cdaq_sync_ports_disconnected(
        self, chassis_devices_ports: str, timeout: float | None
    ) -> bool: ...
    def auto_configure_cdaq_sync_connections(
        self, chassis_devices_ports: str, timeout: float | None
    ) -> list[float]: ...
    def calculate_reverse_poly_coeff(
        self,
        forward_coeffs: list[float],
        min_val_x: float,
        max_val_x: float,
        num_points_to_compute: int,
        reverse_poly_order: int,
    ) -> None: ...
    def cfg_anlg_edge_ref_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        pretrigger_samples: int,
        trigger_slope: Slope,
        trigger_level: float,
    ) -> None: ...
    def cfg_anlg_edge_start_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        trigger_slope: Slope,
        trigger_level: float,
    ) -> None: ...
    def cfg_anlg_multi_edge_ref_trig(
        self,
        task: TaskHandle,
        trigger_sources: str,
        pretrigger_samples: int,
        trigger_slope_array: list[Slope],
        trigger_level_array: list[float],
    ) -> None: ...
    def cfg_anlg_multi_edge_start_trig(
        self,
        task: TaskHandle,
        trigger_sources: str,
        trigger_slope_array: list[Slope],
        trigger_level_array: list[float],
    ) -> None: ...
    def cfg_anlg_window_ref_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        window_top: float,
        window_bottom: float,
        pretrigger_samples: int,
        trigger_when: WindowTriggerCondition1,
    ) -> None: ...
    def cfg_anlg_window_start_trig(
        self,
        task: TaskHandle,
        window_top: float,
        window_bottom: float,
        trigger_source: str,
        trigger_when: WindowTriggerCondition1,
    ) -> None: ...
    def cfg_burst_handshaking_timing_export_clock(
        self,
        task: TaskHandle,
        sample_clk_rate: float,
        sample_clk_outp_term: str,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
        sample_clk_pulse_polarity: Polarity,
        pause_when: Level,
        ready_event_active_level: Polarity,
    ) -> None: ...
    def cfg_burst_handshaking_timing_import_clock(
        self,
        task: TaskHandle,
        sample_clk_rate: float,
        sample_clk_src: str,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
        sample_clk_active_edge: Edge,
        pause_when: Level,
        ready_event_active_level: Polarity,
    ) -> None: ...
    def cfg_change_detection_timing(
        self,
        task: TaskHandle,
        rising_edge_chan: str,
        falling_edge_chan: str,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
    ) -> None: ...
    def cfg_dig_edge_ref_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        pretrigger_samples: int,
        trigger_edge: Edge,
    ) -> None: ...
    def cfg_dig_edge_start_trig(
        self, task: TaskHandle, trigger_source: str, trigger_edge: Edge | None
    ) -> None: ...
    def cfg_dig_pattern_ref_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        trigger_pattern: str,
        pretrigger_samples: int,
        trigger_when: DigitalPatternCondition,
    ) -> None: ...
    def cfg_dig_pattern_start_trig(
        self,
        task: TaskHandle,
        trigger_source: str,
        trigger_pattern: str,
        trigger_when: DigitalPatternCondition,
    ) -> None: ...
    def cfg_handshaking_timing(
        self,
        task: TaskHandle,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
    ) -> None: ...
    def cfg_implicit_timing(
        self,
        task: TaskHandle,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
    ) -> None: ...
    def cfg_pipelined_samp_clk_timing(
        self,
        task: TaskHandle,
        rate: float,
        source: str,
        active_edge: Edge,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
    ) -> None: ...
    def cfg_samp_clk_timing(
        self,
        task: TaskHandle,
        rate: float,
        source: str,
        active_edge: Edge,
        sample_mode: AcquisitionType,
        samps_per_chan: int,
    ) -> None: ...
    def cfg_time_start_trig(
        self, task: TaskHandle, when: datetime, timescale: Timescale | None
    ) -> None: ...
    def cfg_watchdog_ao_expir_states(
        self,
        task: TaskHandle,
        channel_names: str,
        expir_state_array: NDArray[np.float64],
        output_type_array: NDArray[np.int32],
    ) -> None: ...
    def cfg_watchdog_co_expir_states(
        self,
        task: TaskHandle,
        channel_names: str,
        expir_state_array: NDArray[np.float64],
    ) -> None: ...
    def cfg_watchdog_do_expir_states(
        self,
        task: TaskHandle,
        channel_names: str,
        expir_state_array: NDArray[np.float64],
    ) -> None: ...
    def clear_task(self, task: TaskHandle) -> None: ...
    def clear_teds(self, physical_channel: str) -> None: ...
    def configure_logging(
        self,
        task: TaskHandle,
        file_path: str | pathlib.PurePath,
        logging_mode: LoggingMode,
        group_name: str,
        operation: LoggingOperation,
    ) -> None: ...
    def configure_teds(
        self, physical_channel: str, file_path: str | pathlib.PurePath
    ) -> None: ...
    def connect_terms(
        self,
        source_terminal: str,
        destination_terminal: str,
        signal_modifiers: SignalModifiers,
    ) -> None: ...
    def control_watchdog_task(
        self, task: TaskHandle, action: WDTTaskAction
    ) -> None: ...
    def create_ai_accel4_wire_dc_voltage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: AccelUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        use_excit_for_scaling: bool,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_accel_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: AccelUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_accel_charge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: AccelUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_bridge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: BridgeUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_calculated_power_chan(
        self,
        task: TaskHandle,
        voltage_physical_channel: str,
        current_physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        voltage_min_val: float,
        voltage_max_val: float,
        current_min_val: float,
        current_max_val: float,
        units: PowerUnits,
        shunt_resistor_loc: CurrentShuntResistorLocation,
        ext_shunt_resistor_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_charge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: ChargeUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_current_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: CurrentUnits,
        shunt_resistor_loc: CurrentShuntResistorLocation,
        ext_shunt_resistor_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_current_rms_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: CurrentUnits,
        shunt_resistor_loc: CurrentShuntResistorLocation,
        ext_shunt_resistor_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_force_bridge_polynomial_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        forward_coeffs: list[float],
        reverse_coeffs: list[float],
        electrical_units: BridgeElectricalUnits,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_force_bridge_table_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        electrical_vals: NDArray[np.float64],
        electrical_units: BridgeElectricalUnits,
        physical_vals: NDArray[np.float64],
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_force_bridge_two_point_lin_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        first_electrical_val: float,
        second_electrical_val: float,
        electrical_units: BridgeElectricalUnits,
        first_physical_val: float,
        second_physical_val: float,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_force_iepe_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_freq_voltage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: FrequencyUnits,
        threshold_level: float,
        hysteresis: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_microphone_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        units: SoundPressureUnits,
        mic_sensitivity: float,
        max_snd_press_level: float,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_pos_eddy_curr_prox_probe_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: LengthUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_pos_lvdt_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: LengthUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        voltage_excit_freq: float,
        ac_excit_wire_mode: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_pos_rvdt_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: AngleUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        voltage_excit_freq: float,
        ac_excit_wire_mode: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_power_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        voltage_setpoint: float,
        current_setpoint: float,
        output_enable: bool,
        name_to_assign_to_channel: str,
    ) -> None: ...
    def create_ai_pressure_bridge_polynomial_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: PressureUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        forward_coeffs: list[float],
        reverse_coeffs: list[float],
        electrical_units: BridgeElectricalUnits,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_pressure_bridge_table_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: PressureUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        electrical_vals: NDArray[np.float64],
        electrical_units: BridgeElectricalUnits,
        physical_vals: NDArray[np.float64],
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_pressure_bridge_two_point_lin_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: PressureUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        first_electrical_val: float,
        second_electrical_val: float,
        electrical_units: BridgeElectricalUnits,
        first_physical_val: float,
        second_physical_val: float,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_resistance_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: ResistanceUnits,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_rosette_strain_gage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        rosette_type: StrainGageRosetteType,
        gage_orientation: float,
        rosette_meas_types: list[StrainGageRosetteMeasurementType],
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        strain_config: StrainGageBridgeType,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        gage_factor: float,
        nominal_gage_resistance: float,
        poisson_ratio: float,
        lead_wire_resistance: float,
    ) -> None: ...
    def create_ai_strain_gage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: StrainUnits,
        strain_config: StrainGageBridgeType,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        gage_factor: float,
        initial_bridge_voltage: float,
        nominal_gage_resistance: float,
        poisson_ratio: float,
        lead_wire_resistance: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_temp_built_in_sensor_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        units: TemperatureUnits,
    ) -> None: ...
    def create_ai_thrmcpl_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        thermocouple_type: ThermocoupleType,
        cjc_source: CJCSource,
        cjc_val: float,
        cjc_channel: str,
    ) -> None: ...
    def create_ai_thrmstr_chan_iex(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        a: float,
        b: float,
        c: float,
    ) -> None: ...
    def create_ai_thrmstr_chan_vex(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        resistance_config: ResistanceConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        a: float,
        b: float,
        c: float,
        r_1: float,
    ) -> None: ...
    def create_ai_torque_bridge_polynomial_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TorqueUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        forward_coeffs: list[float],
        reverse_coeffs: list[float],
        electrical_units: BridgeElectricalUnits,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_torque_bridge_table_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TorqueUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        electrical_vals: NDArray[np.float64],
        electrical_units: BridgeElectricalUnits,
        physical_vals: NDArray[np.float64],
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_torque_bridge_two_point_lin_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TorqueUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        nominal_bridge_resistance: float,
        first_electrical_val: float,
        second_electrical_val: float,
        electrical_units: BridgeElectricalUnits,
        first_physical_val: float,
        second_physical_val: float,
        physical_units: BridgePhysicalUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_velocity_iepe_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: VelocityUnits,
        sensitivity: float,
        sensitivity_units: AccelSensitivityUnits,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_voltage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: VoltageUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_voltage_chan_with_excit(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: VoltageUnits,
        bridge_config: BridgeConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        use_excit_for_scaling: bool,
        custom_scale_name: str,
    ) -> None: ...
    def create_ai_voltage_rms_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: VoltageUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_airtd_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        rtd_type: RTDType,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        r_0: float,
    ) -> None: ...
    def create_ao_current_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: CurrentUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ao_func_gen_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        type: FuncGenType,
        freq: float,
        amplitude: float,
        offset: float,
    ) -> None: ...
    def create_ao_voltage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: VoltageUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_ang_encoder_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        decoding_type: EncoderType,
        zidx_enable: bool,
        zidx_val: float,
        zidx_phase: EncoderZIndexPhase,
        units: AngleUnits,
        pulses_per_rev: int,
        initial_angle: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_ang_velocity_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        decoding_type: EncoderType,
        units: AngularVelocityUnits,
        pulses_per_rev: int,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_count_edges_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        edge: Edge,
        initial_count: int,
        count_direction: CountDirection,
    ) -> None: ...
    def create_ci_duty_cycle_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_freq: float,
        max_freq: float,
        edge: Edge,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_freq_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: FrequencyUnits,
        edge: Edge,
        meas_method: CounterFrequencyMethod,
        meas_time: float,
        divisor: int,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_lin_encoder_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        decoding_type: EncoderType,
        zidx_enable: bool,
        zidx_val: float,
        zidx_phase: EncoderZIndexPhase,
        units: LengthUnits,
        dist_per_pulse: float,
        initial_pos: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_lin_velocity_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        decoding_type: EncoderType,
        units: VelocityUnits,
        dist_per_pulse: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_period_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TimeUnits,
        edge: Edge,
        meas_method: float,
        meas_time: float,
        divisor: int,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_pulse_chan_freq(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: FrequencyUnits,
    ) -> None: ...
    def create_ci_pulse_chan_ticks(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        source_terminal: str,
        min_val: float,
        max_val: float,
    ) -> None: ...
    def create_ci_pulse_chan_time(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TimeUnits,
    ) -> None: ...
    def create_ci_pulse_width_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TimeUnits,
        starting_edge: Edge,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_semi_period_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TimeUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_ci_two_edge_sep_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TimeUnits,
        first_edge: Edge,
        second_edge: Edge,
        custom_scale_name: str,
    ) -> None: ...
    def create_cigps_timestamp_chan(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        units: TimeUnits,
        sync_method: GpsSignalType,
        custom_scale_name: str,
    ) -> None: ...
    def create_co_pulse_chan_freq(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        units: FrequencyUnits,
        idle_state: Level,
        initial_delay: float,
        freq: float,
        duty_cycle: float,
    ) -> None: ...
    def create_co_pulse_chan_ticks(
        self,
        task: TaskHandle,
        counter: str,
        source_terminal: str,
        name_to_assign_to_channel: str,
        idle_state: Level,
        initial_delay: float,
        low_ticks: int,
        high_ticks: int,
    ) -> None: ...
    def create_co_pulse_chan_time(
        self,
        task: TaskHandle,
        counter: str,
        name_to_assign_to_channel: str,
        units: TimeUnits,
        idle_state: Level,
        initial_delay: float,
        low_time: float,
        high_time: float,
    ) -> None: ...
    def create_di_chan(
        self,
        task: TaskHandle,
        lines: str,
        name_to_assign_to_lines: str,
        line_grouping: LineGrouping,
    ) -> None: ...
    def create_do_chan(
        self,
        task: TaskHandle,
        lines: str,
        name_to_assign_to_lines: str,
        line_grouping: LineGrouping,
    ) -> None: ...
    def create_lin_scale(
        self,
        name: str,
        slope: float,
        y_intercept: float,
        pre_scaled_units: UnitsPreScaled,
        scaled_units: str,
    ) -> None: ...
    def create_map_scale(
        self,
        name: str,
        prescaled_min: float,
        prescaled_max: float,
        scaled_min: float,
        scaled_max: float,
        pre_scaled_units: UnitsPreScaled,
        scaled_units: str,
    ) -> None: ...
    def create_polynomial_scale(
        self,
        name: str,
        forward_coeffs: list[float],
        reverse_coeffs: list[float],
        pre_scaled_units: UnitsPreScaled,
        scaled_units: str,
    ) -> None: ...
    def create_table_scale(
        self,
        name: str,
        prescaled_vals: list[float],
        scaled_vals: list[float],
        pre_scaled_units: UnitsPreScaled,
        scaled_units: str,
    ) -> None: ...
    def create_task(self, session_name: str) -> tuple[TaskHandle, bool]: ...
    def create_tedsai_accel_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: AccelUnits,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_bridge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TEDSUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_current_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: TEDSUnits,
        shunt_resistor_loc: CurrentShuntResistorLocation,
        ext_shunt_resistor_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_force_bridge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_force_iepe_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: ForceUnits,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_microphone_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        units: SoundPressureUnits,
        max_snd_press_level: float,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_pos_lvdt_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: LengthUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        voltage_excit_freq: float,
        ac_excit_wire_mode: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_pos_rvdt_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: AngleUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        voltage_excit_freq: float,
        ac_excit_wire_mode: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_pressure_bridge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: PressureUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_resistance_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TEDSUnits,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_strain_gage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: StrainUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        initial_bridge_voltage: float,
        lead_wire_resistance: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_thrmcpl_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        cjc_source: CJCSource,
        cjc_val: float,
        cjc_channel: str,
    ) -> None: ...
    def create_tedsai_thrmstr_chan_iex(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
    ) -> None: ...
    def create_tedsai_thrmstr_chan_vex(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        resistance_config: ResistanceConfiguration,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        r_1: float,
    ) -> None: ...
    def create_tedsai_torque_bridge_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TorqueUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_voltage_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: TEDSUnits,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsai_voltage_chan_with_excit(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        terminal_config: TerminalConfiguration,
        min_val: float,
        max_val: float,
        units: TEDSUnits,
        voltage_excit_source: ExcitationSource,
        voltage_excit_val: float,
        custom_scale_name: str,
    ) -> None: ...
    def create_tedsairtd_chan(
        self,
        task: TaskHandle,
        physical_channel: str,
        name_to_assign_to_channel: str,
        min_val: float,
        max_val: float,
        units: TemperatureUnits,
        resistance_config: ResistanceConfiguration,
        current_excit_source: ExcitationSource,
        current_excit_val: float,
    ) -> None: ...
    def create_watchdog_timer_task_ex(
        self, device_name: str, session_name: str, timeout: float
    ) -> tuple[TaskHandle, bool]: ...
    def delete_network_device(self, device_name: str) -> None: ...
    def delete_saved_global_chan(self, channel_name: str) -> None: ...
    def delete_saved_scale(self, scale_name: str) -> None: ...
    def delete_saved_task(self, task_name: str) -> None: ...
    def device_supports_cal(self, device_name: str) -> bool: ...
    def disable_ref_trig(self, task: TaskHandle) -> None: ...
    def disable_start_trig(self, task: TaskHandle) -> None: ...
    def disconnect_terms(
        self, source_terminal: str, destination_terminal: str
    ) -> None: ...
    def export_signal(
        self, task: TaskHandle, signal_id: Signal, output_terminal: str
    ) -> None: ...
    def get_analog_power_up_states_with_output_type(
        self, channel_names: str, array_size: int
    ) -> tuple[list[float], list[int]]: ...
    def get_auto_configured_cdaq_sync_connections(self) -> str: ...
    def get_buffer_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_cal_info_attribute_bool(self, device_name: str, attribute: int) -> bool: ...
    def get_cal_info_attribute_double(
        self, device_name: str, attribute: int
    ) -> float: ...
    def get_cal_info_attribute_string(
        self, device_name: str, attribute: int
    ) -> str: ...
    def get_cal_info_attribute_uint32(
        self, device_name: str, attribute: int
    ) -> int: ...
    def get_chan_attribute_bool(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> bool: ...
    def get_chan_attribute_double(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> float: ...
    def get_chan_attribute_double_array(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> list[float]: ...
    def get_chan_attribute_int32(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> int: ...
    def get_chan_attribute_string(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> str: ...
    def get_chan_attribute_uint32(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> int: ...
    def get_device_attribute_bool(self, device_name: str, attribute: int) -> bool: ...
    def get_device_attribute_double(
        self, device_name: str, attribute: int
    ) -> float: ...
    def get_device_attribute_double_array(
        self, device_name: str, attribute: int
    ) -> list[float]: ...
    def get_device_attribute_int32(self, device_name: str, attribute: int) -> int: ...
    def get_device_attribute_int32_array(
        self, device_name: str, attribute: int
    ) -> list[int]: ...
    def get_device_attribute_string(self, device_name: str, attribute: int) -> str: ...
    def get_device_attribute_uint32(self, device_name: str, attribute: int) -> int: ...
    def get_device_attribute_uint32_array(
        self, device_name: str, attribute: int
    ) -> list[int]: ...
    def get_digital_logic_family_power_up_state(self, device_name: str) -> int: ...
    def get_digital_power_up_states(
        self, device_name: str, channel_name: str
    ) -> list[int]: ...
    def get_digital_pull_up_pull_down_states(
        self, device_name: str, channel_name: str
    ) -> list[int]: ...
    def get_disconnected_cdaq_sync_ports(self) -> str: ...
    def get_exported_signal_attribute_bool(
        self, task: TaskHandle, attribute: int
    ) -> bool: ...
    def get_exported_signal_attribute_double(
        self, task: TaskHandle, attribute: int
    ) -> float: ...
    def get_exported_signal_attribute_int32(
        self, task: TaskHandle, attribute: int
    ) -> int: ...
    def get_exported_signal_attribute_string(
        self, task: TaskHandle, attribute: int
    ) -> str: ...
    def get_exported_signal_attribute_uint32(
        self, task: TaskHandle, attribute: int
    ) -> int: ...
    def get_ext_cal_last_date_and_time(self, device_name: str) -> datetime: ...
    def get_persisted_chan_attribute_bool(
        self, channel: str, attribute: int
    ) -> bool: ...
    def get_persisted_chan_attribute_string(
        self, channel: str, attribute: int
    ) -> str: ...
    def get_persisted_scale_attribute_bool(
        self, scale_name: str, attribute: int
    ) -> bool: ...
    def get_persisted_scale_attribute_string(
        self, scale_name: str, attribute: int
    ) -> str: ...
    def get_persisted_task_attribute_bool(
        self, task_name: str, attribute: int
    ) -> bool: ...
    def get_persisted_task_attribute_string(
        self, task_name: str, attribute: int
    ) -> str: ...
    def get_physical_chan_attribute_bool(
        self, physical_channel: str, attribute: int
    ) -> bool: ...
    def get_physical_chan_attribute_bytes(
        self, physical_channel: str, attribute: int
    ) -> bytes: ...
    def get_physical_chan_attribute_double(
        self, physical_channel: str, attribute: int
    ) -> float: ...
    def get_physical_chan_attribute_double_array(
        self, physical_channel: str, attribute: int
    ) -> list[float]: ...
    def get_physical_chan_attribute_int32(
        self, physical_channel: str, attribute: int
    ) -> int: ...
    def get_physical_chan_attribute_int32_array(
        self, physical_channel: str, attribute: int
    ) -> list[int]: ...
    def get_physical_chan_attribute_string(
        self, physical_channel: str, attribute: int
    ) -> str: ...
    def get_physical_chan_attribute_uint32(
        self, physical_channel: str, attribute: int
    ) -> int: ...
    def get_physical_chan_attribute_uint32_array(
        self, physical_channel: str, attribute: int
    ) -> list[int]: ...
    def get_read_attribute_bool(self, task: TaskHandle, attribute: int) -> bool: ...
    def get_read_attribute_double(self, task: TaskHandle, attribute: int) -> float: ...
    def get_read_attribute_int32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_read_attribute_string(
        self, task: TaskHandle, attribute: int, size_hint: int = ...
    ) -> str: ...
    def get_read_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_read_attribute_uint64(self, task: TaskHandle, attribute: int) -> int: ...
    def get_scale_attribute_double(self, scale_name: str, attribute: int) -> float: ...
    def get_scale_attribute_double_array(
        self, scale_name: str, attribute: int
    ) -> list[float]: ...
    def get_scale_attribute_int32(self, scale_name: str, attribute: int) -> int: ...
    def get_scale_attribute_string(self, scale_name: str, attribute: int) -> str: ...
    def get_self_cal_last_date_and_time(self, device_name: str) -> datetime: ...
    def get_system_info_attribute_string(self, attribute: int) -> str: ...
    def get_system_info_attribute_uint32(self, attribute: int) -> int: ...
    def get_task_attribute_bool(self, task: TaskHandle, attribute: int) -> bool: ...
    def get_task_attribute_string(self, task: TaskHandle, attribute: int) -> str: ...
    def get_task_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_timing_attribute_bool(self, task: TaskHandle, attribute: int) -> bool: ...
    def get_timing_attribute_double(
        self, task: TaskHandle, attribute: int
    ) -> float: ...
    def get_timing_attribute_ex_bool(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> bool: ...
    def get_timing_attribute_ex_double(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> float: ...
    def get_timing_attribute_ex_int32(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> int: ...
    def get_timing_attribute_ex_string(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> str: ...
    def get_timing_attribute_ex_uint32(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> int: ...
    def get_timing_attribute_ex_uint64(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> int: ...
    def get_timing_attribute_int32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_timing_attribute_string(self, task: TaskHandle, attribute: int) -> str: ...
    def get_timing_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_timing_attribute_uint64(self, task: TaskHandle, attribute: int) -> int: ...
    def get_trig_attribute_bool(self, task: TaskHandle, attribute: int) -> bool: ...
    def get_trig_attribute_double(self, task: TaskHandle, attribute: int) -> float: ...
    def get_trig_attribute_double_array(
        self, task: TaskHandle, attribute: int
    ) -> list[float]: ...
    def get_trig_attribute_int32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_trig_attribute_int32_array(
        self, task: TaskHandle, attribute: int
    ) -> list[int]: ...
    def get_trig_attribute_string(self, task: TaskHandle, attribute: int) -> str: ...
    def get_trig_attribute_timestamp(
        self, task: TaskHandle, attribute: int
    ) -> datetime: ...
    def get_trig_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_watchdog_attribute_bool(
        self, task: TaskHandle, lines: str, attribute: int
    ) -> bool: ...
    def get_watchdog_attribute_double(
        self, task: TaskHandle, lines: str, attribute: int
    ) -> float: ...
    def get_watchdog_attribute_int32(
        self, task: TaskHandle, lines: str, attribute: int
    ) -> int: ...
    def get_watchdog_attribute_string(
        self, task: TaskHandle, lines: str, attribute: int
    ) -> str: ...
    def get_write_attribute_bool(self, task: TaskHandle, attribute: int) -> bool: ...
    def get_write_attribute_double(self, task: TaskHandle, attribute: int) -> float: ...
    def get_write_attribute_int32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_write_attribute_string(
        self, task: TaskHandle, attribute: int, size_hint: int = 0
    ) -> str: ...
    def get_write_attribute_uint32(self, task: TaskHandle, attribute: int) -> int: ...
    def get_write_attribute_uint64(self, task: TaskHandle, attribute: int) -> int: ...
    def internal_get_last_created_chan(self) -> str: ...
    def is_task_done(self, task: TaskHandle) -> bool: ...
    def load_task(self, session_name: str) -> tuple[TaskHandle, bool]: ...
    def perform_bridge_offset_nulling_cal_ex(
        self, task: TaskHandle, channel: str, skip_unsupported_channels: bool
    ) -> None: ...
    def perform_bridge_shunt_cal_ex(
        self,
        task: TaskHandle,
        channel: str,
        shunt_resistor_value: float,
        shunt_resistor_location: ShuntElementLocation,
        shunt_resistor_select: ShuntCalSelect,
        shunt_resistor_source: ShuntCalSource,
        bridge_resistance: int,
        skip_unsupported_channels: bool,
    ) -> None: ...
    def perform_strain_shunt_cal_ex(
        self,
        task: TaskHandle,
        channel: str,
        shunt_resistor_value: float,
        shunt_resistor_location: ShuntElementLocation,
        shunt_resistor_select: ShuntCalSelect,
        shunt_resistor_source: ShuntCalSource,
        skip_unsupported_channels: bool,
    ) -> None: ...
    def perform_thrmcpl_lead_offset_nulling_cal(
        self, task: TaskHandle, channel: str, skip_unsupported_channels: bool
    ) -> None: ...
    def read_analog_f64(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], int]: ...
    def read_analog_scalar_f64(self, task: TaskHandle, timeout: float) -> float: ...
    def read_binary_i16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.int16],
    ) -> tuple[NDArray[np.int16], int]: ...
    def read_binary_i32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.int32],
    ) -> tuple[NDArray[np.int32], int]: ...
    def read_binary_u16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint16],
    ) -> tuple[NDArray[np.uint16], int]: ...
    def read_binary_u32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint32],
    ) -> tuple[NDArray[np.uint32], int]: ...
    def read_counter_f64(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        read_array: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], int]: ...
    def read_counter_f64_ex(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], int]: ...
    def read_counter_scalar_f64(self, task: TaskHandle, timeout: float) -> float: ...
    def read_counter_scalar_u32(
        self, task: TaskHandle, timeout: float
    ) -> np.uint32: ...
    def read_counter_u32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        read_array: NDArray[np.uint32],
    ) -> tuple[NDArray[np.uint32], int]: ...
    def read_counter_u32_ex(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint32],
    ) -> tuple[NDArray[np.uint32], int]: ...
    def read_ctr_freq(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        interleaved: int,
        read_array_frequency: NDArray[np.float64],
        read_array_duty_cycle: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], NDArray[np.float64], int]: ...
    def read_ctr_freq_scalar(
        self, task: TaskHandle, timeout: float
    ) -> tuple[float, float]: ...
    def read_ctr_ticks(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        interleaved: int,
        read_array_high_ticks: NDArray[np.uint32],
        read_array_low_ticks: NDArray[np.uint32],
    ) -> tuple[NDArray[np.uint32], NDArray[np.uint32], int]: ...
    def read_ctr_ticks_scalar(
        self, task: TaskHandle, timeout: float
    ) -> tuple[int, int]: ...
    def read_ctr_time(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        interleaved: int,
        read_array_high_time: NDArray[np.float64],
        read_array_low_time: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], NDArray[np.float64], int]: ...
    def read_ctr_time_scalar(self, task: TaskHandle, timeout: float) -> None: ...
    def read_digital_lines(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.bool_],
    ) -> tuple[NDArray[np.bool_], int, int]: ...
    def read_digital_scalar_u32(self, task: TaskHandle, timeout: float) -> int: ...
    def read_digital_u16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint16],
    ) -> tuple[NDArray[np.bool_], int]: ...
    def read_digital_u32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint32],
    ) -> tuple[NDArray[np.bool_], int]: ...
    def read_digital_u8(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array: NDArray[np.uint8],
    ) -> tuple[NDArray[np.bool_], int]: ...
    def read_power_binary_i16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array_voltage: NDArray[np.int16],
        read_array_current: NDArray[np.int16],
    ) -> tuple[NDArray[np.int16], NDArray[np.int16], int]: ...
    def read_power_f64(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        fill_mode: FillMode,
        read_array_voltage: NDArray[np.float64],
        read_array_current: NDArray[np.float64],
    ) -> tuple[NDArray[np.float64], NDArray[np.float64], int]: ...
    def read_power_scalar_f64(
        self, task: TaskHandle, timeout: float
    ) -> tuple[float, float]: ...
    def read_raw(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        read_array: NDArray[np.number[Any]],
    ) -> tuple[NDArray[np.number[Any]], int, int]: ...
    def register_done_event(
        self,
        task: TaskHandle,
        options: int,
        callback_function: object,
        callback_data: object,
    ) -> object: ...
    def register_every_n_samples_event(
        self,
        task: TaskHandle,
        every_n_samples_event_type: EveryNSamplesEventType,
        n_samples: int,
        options: int,
        callback_function: Callable[[int, int, object], int],
        callback_data: object,
    ) -> object: ...
    def register_signal_event(
        self,
        task: TaskHandle,
        signal_id: Signal,
        options: int,
        callback_function: Callable[[int, int, object], int],
        callback_data: object,
    ) -> object: ...
    def remove_cdaq_sync_connection(self, port_list: str) -> None: ...
    def reserve_network_device(
        self, device_name: str, override_reservation: bool
    ) -> None: ...
    def reset_buffer_attribute(self, task: TaskHandle, attribute: int) -> None: ...
    def reset_chan_attribute(
        self, task: TaskHandle, channel: str, attribute: int
    ) -> None: ...
    def reset_device(self, device_name: str) -> None: ...
    def reset_exported_signal_attribute(
        self, task: TaskHandle, attribute: int
    ) -> None: ...
    def reset_read_attribute(self, task: TaskHandle, attribute: int) -> None: ...
    def reset_timing_attribute(self, task: TaskHandle, attribute: int) -> None: ...
    def reset_timing_attribute_ex(
        self, task: TaskHandle, device_names: object | str | None, attribute: int
    ) -> None: ...
    def reset_trig_attribute(self, task: TaskHandle, attribute: int) -> None: ...
    def reset_watchdog_attribute(
        self, task: TaskHandle, lines: str, attribute: int
    ) -> None: ...
    def reset_write_attribute(self, task: TaskHandle, attribute: int) -> None: ...
    def restore_last_ext_cal_const(self, device_name: str) -> None: ...
    def save_global_chan(
        self,
        task: TaskHandle,
        channel_name: str,
        save_as: str,
        author: str,
        options: int,
    ) -> None: ...
    def save_scale(
        self, scale_name: str, save_as: str, author: str, options: int
    ) -> None: ...
    def save_task(
        self, task: TaskHandle, save_as: str, author: str, options: int
    ) -> None: ...
    def self_cal(self, device_name: str) -> None: ...
    def self_test_device(self, device_name: str) -> None: ...
    def set_analog_power_up_states(
        self, device_name: str, channel_names: str, state: float, channel_type: int
    ) -> None: ...
    def set_analog_power_up_states_with_output_type(
        self,
        channel_names: str,
        state_array: NDArray[np.float64],
        channel_type_array: NDArray[np.int32],
    ) -> None: ...
    def set_buffer_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: int
    ) -> None: ...
    def set_cal_info_attribute_bool(
        self, device_name: str, attribute: int, value: bool
    ) -> None: ...
    def set_cal_info_attribute_double(
        self, device_name: str, attribute: int, value: float
    ) -> None: ...
    def set_cal_info_attribute_string(
        self, device_name: str, attribute: int, value: str
    ) -> None: ...
    def set_cal_info_attribute_uint32(
        self, device_name: str, attribute: int, value: int
    ) -> None: ...
    def set_chan_attribute_bool(
        self, task: TaskHandle, channel: str, attribute: int, value: bool
    ) -> None: ...
    def set_chan_attribute_double(
        self, task: TaskHandle, channel: str, attribute: int, value: float
    ) -> None: ...
    def set_chan_attribute_double_array(
        self, task: TaskHandle, channel: str, attribute: int, value: NDArray[np.float64]
    ) -> None: ...
    def set_chan_attribute_int32(
        self, task: TaskHandle, channel: str, attribute: int, value: np.int32
    ) -> None: ...
    def set_chan_attribute_string(
        self, task: TaskHandle, channel: str, attribute: int, value: str
    ) -> None: ...
    def set_chan_attribute_uint32(
        self, task: TaskHandle, channel: str, attribute: int, value: np.uint32
    ) -> None: ...
    def set_digital_logic_family_power_up_state(
        self, device_name: str, logic_family: LogicFamily
    ) -> None: ...
    def set_digital_power_up_states(
        self, device_name: str, channel_names: str, state: PowerUpStates
    ) -> None: ...
    def set_digital_pull_up_pull_down_states(
        self, device_name: str, channel_names: str, state: PowerUpStates
    ) -> None: ...
    def set_exported_signal_attribute_bool(
        self, task: TaskHandle, attribute: int, value: bool
    ) -> None: ...
    def set_exported_signal_attribute_double(
        self, task: TaskHandle, attribute: int, value: float
    ) -> None: ...
    def set_exported_signal_attribute_int32(
        self, task: TaskHandle, attribute: int, value: np.int32
    ) -> None: ...
    def set_exported_signal_attribute_string(
        self, task: TaskHandle, attribute: int, value: str
    ) -> None: ...
    def set_exported_signal_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: np.uint32
    ) -> None: ...
    def set_read_attribute_bool(
        self, task: TaskHandle, attribute: int, value: bool
    ) -> None: ...
    def set_read_attribute_double(
        self, task: TaskHandle, attribute: int, value: float
    ) -> None: ...
    def set_read_attribute_int32(
        self, task: TaskHandle, attribute: int, value: np.int32
    ) -> None: ...
    def set_read_attribute_string(
        self, task: TaskHandle, attribute: int, value: str
    ) -> None: ...
    def set_read_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: np.uint32
    ) -> None: ...
    def set_read_attribute_uint64(
        self, task: TaskHandle, attribute: int, value: np.uint64
    ) -> None: ...
    def set_runtime_environment(
        self,
        environment: str,
        environment_version: str,
        reserved_1: str,
        reserved_2: str,
    ) -> None: ...
    def set_scale_attribute_double(
        self, scale_name: str, attribute: int, value: float
    ) -> None: ...
    def set_scale_attribute_double_array(
        self, scale_name: str, attribute: int, value: NDArray[np.float64]
    ) -> None: ...
    def set_scale_attribute_int32(
        self, scale_name: str, attribute: int, value: np.int32
    ) -> None: ...
    def set_scale_attribute_string(
        self, scale_name: str, attribute: int, value: str
    ) -> None: ...
    def set_timing_attribute_bool(
        self, task: TaskHandle, attribute: int, value: bool
    ) -> None: ...
    def set_timing_attribute_double(
        self, task: TaskHandle, attribute: int, value: float
    ) -> None: ...
    def set_timing_attribute_ex_bool(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: bool,
    ) -> None: ...
    def set_timing_attribute_ex_double(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: float,
    ) -> None: ...
    def set_timing_attribute_ex_int32(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: np.int32,
    ) -> None: ...
    def set_timing_attribute_ex_string(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: str,
    ) -> None: ...
    def set_timing_attribute_ex_uint32(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: np.uint32,
    ) -> None: ...
    def set_timing_attribute_ex_uint64(
        self,
        task: TaskHandle,
        device_names: object | str | None,
        attribute: int,
        value: np.uint64,
    ) -> None: ...
    def set_timing_attribute_int32(
        self, task: TaskHandle, attribute: int, value: np.int32
    ) -> None: ...
    def set_timing_attribute_string(
        self, task: TaskHandle, attribute: int, value: str
    ) -> None: ...
    def set_timing_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: np.uint32
    ) -> None: ...
    def set_timing_attribute_uint64(
        self, task: TaskHandle, attribute: int, value: np.uint64
    ) -> None: ...
    def set_trig_attribute_bool(
        self, task: TaskHandle, attribute: int, value: bool
    ) -> None: ...
    def set_trig_attribute_double(
        self, task: TaskHandle, attribute: int, value: float
    ) -> None: ...
    def set_trig_attribute_double_array(
        self, task: TaskHandle, attribute: int, value: NDArray[np.float64]
    ) -> None: ...
    def set_trig_attribute_int32(
        self, task: TaskHandle, attribute: int, value: np.int32
    ) -> None: ...
    def set_trig_attribute_int32_array(
        self, task: TaskHandle, attribute: int, value: NDArray[np.int32]
    ) -> None: ...
    def set_trig_attribute_string(
        self, task: TaskHandle, attribute: int, value: str
    ) -> None: ...
    def set_trig_attribute_timestamp(
        self, task: TaskHandle, attribute: int, value: datetime
    ) -> None: ...
    def set_trig_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: np.uint32
    ) -> None: ...
    def set_watchdog_attribute_bool(
        self, task: TaskHandle, lines: str, attribute: int, value: bool
    ) -> None: ...
    def set_watchdog_attribute_double(
        self, task: TaskHandle, lines: str, attribute: int, value: float
    ) -> None: ...
    def set_watchdog_attribute_int32(
        self, task: TaskHandle, lines: str, attribute: int, value: np.int32
    ) -> None: ...
    def set_watchdog_attribute_string(
        self, task: TaskHandle, lines: str, attribute: int, value: str
    ) -> None: ...
    def set_write_attribute_bool(
        self, task: TaskHandle, attribute: int, value: bool
    ) -> None: ...
    def set_write_attribute_double(
        self, task: TaskHandle, attribute: int, value: float
    ) -> None: ...
    def set_write_attribute_int32(
        self, task: TaskHandle, attribute: int, value: np.int32
    ) -> None: ...
    def set_write_attribute_string(
        self, task: TaskHandle, attribute: int, value: str
    ) -> None: ...
    def set_write_attribute_uint32(
        self, task: TaskHandle, attribute: int, value: np.uint32
    ) -> None: ...
    def set_write_attribute_uint64(
        self, task: TaskHandle, attribute: int, value: np.uint64
    ) -> None: ...
    def start_new_file(
        self, task: TaskHandle, file_path: str | pathlib.PurePath
    ) -> None: ...
    def start_task(self, task: TaskHandle) -> None: ...
    def stop_task(self, task: TaskHandle) -> None: ...
    def task_control(self, task: TaskHandle, action: TaskMode) -> None: ...
    def tristate_output_term(self, output_terminal: str) -> None: ...
    def unregister_done_event(self, task: TaskHandle) -> None: ...
    def unregister_every_n_samples_event(
        self, task: TaskHandle, every_n_samples_event_type: EveryNSamplesEventType
    ) -> None: ...
    def unregister_signal_event(self, task: TaskHandle, signal_id: Signal) -> None: ...
    def unreserve_network_device(self, device_name: str) -> None: ...
    def wait_for_valid_timestamp(
        self, task: TaskHandle, timestamp_event: int, timeout: float
    ) -> datetime: ...
    def wait_until_task_done(self, task: TaskHandle, time_to_wait: float) -> None: ...
    def write_analog_f64(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.float64],
    ) -> int: ...
    def write_analog_scalar_f64(
        self, task: TaskHandle, auto_start: bool, timeout: float, value: float
    ) -> None: ...
    def write_binary_i16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.int16],
    ) -> int: ...
    def write_binary_i32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.int32],
    ) -> int: ...
    def write_binary_u16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.uint16],
    ) -> int: ...
    def write_binary_u32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.uint32],
    ) -> int: ...
    def write_ctr_freq(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        frequency: NDArray[np.float64],
        duty_cycle: NDArray[np.float64],
    ) -> int: ...
    def write_ctr_freq_scalar(
        self,
        task: TaskHandle,
        auto_start: bool,
        timeout: float,
        frequency: float,
        duty_cycle: float,
    ) -> None: ...
    def write_ctr_ticks(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        high_ticks: float,
        low_ticks: float,
    ) -> int: ...
    def write_ctr_ticks_scalar(
        self,
        task: TaskHandle,
        auto_start: bool,
        timeout: float,
        high_ticks: float,
        low_ticks: float,
    ) -> None: ...
    def write_ctr_time(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        high_time: NDArray[np.uint32],
        low_time: NDArray[np.uint32],
    ) -> int: ...
    def write_ctr_time_scalar(
        self,
        task: TaskHandle,
        auto_start: bool,
        timeout: float,
        high_time: float,
        low_time: float,
    ) -> None: ...
    def write_digital_lines(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.bool_],
    ) -> int: ...
    def write_digital_scalar_u32(
        self, task: TaskHandle, auto_start: bool, timeout: float, value: np.uint32
    ) -> None: ...
    def write_digital_u16(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.uint16],
    ) -> int: ...
    def write_digital_u32(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.uint32],
    ) -> int: ...
    def write_digital_u8(
        self,
        task: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,  # FillMode Enum
        write_array: NDArray[np.uint8],
    ) -> int: ...
    def write_id_pin_memory(
        self, device_name: str, id_pin_name: str, data: list[int], format_code: int
    ) -> None: ...
    def write_to_teds_from_array(
        self,
        physical_channel: str,
        bit_stream: list[int],
        basic_teds_options: WriteBasicTEDSOptions,
    ) -> None: ...
    def write_to_teds_from_file(
        self,
        physical_channel: str,
        file_path: str,
        basic_teds_options: WriteBasicTEDSOptions,
    ) -> None: ...
    def get_error_string(self, error_code: int) -> str: ...
    def get_extended_error_info(
        self,
    ) -> Any | Literal["Failed to retrieve error description."]: ...
    def read_analog_waveform(
        self,
        task_handle: TaskHandle,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[np.float64],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int: ...
    def read_analog_waveforms(
        self,
        task_handle: TaskHandle,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: list[AnalogWaveform[np.float64]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int: ...
    def _internal_read_analog_waveform_ex(
        self,
        task_handle: TaskHandle,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: NDArray[np.float64],
        properties: Mapping[str, ExtendedPropertyValue] | None,
        t0_array: NDArray[np.int64] | None,
        dt_array: NDArray[np.int64] | None,
    ) -> tuple[
        int,  # error code
        int,  # The number of samples per channel that were read
    ]: ...
    def _internal_read_analog_waveform_per_chan(
        self,
        task_handle: TaskHandle,
        num_samps_per_chan: int,
        timeout: float,
        read_arrays: list[NDArray[np.float64]],
        properties: Mapping[str, ExtendedPropertyValue] | None,
        t0_array: NDArray[np.int64] | None,
        dt_array: NDArray[np.int64] | None,
    ) -> tuple[
        int,  # error code
        int,  # The number of samples per channel that were read
    ]: ...
    def _get_wfm_attr_callback(
        self, properties: Sequence[ExtendedPropertyDictionary]
    ) -> CSetWfmAttrCallbackPtr: ...
    def _get_wfm_attr_value(
        self, attribute_type: int, value: ctypes.c_void_p, value_size_in_bytes: int
    ) -> ExtendedPropertyValue: ...
    def _get_wfm_attr_callback_ptr(
        self, set_wfm_attr_callback: SetWfmAttrCallback
    ) -> CSetWfmAttrCallbackPtr: ...
    def _set_waveform_timings(
        self,
        waveforms: Sequence[AnalogWaveform[np.float64] | DigitalWaveform[np.uint8]],
        t0_array: NDArray[np.int64],
        dt_array: NDArray[np.int64],
    ) -> None: ...
    def read_digital_waveform(
        self,
        task_handle: TaskHandle,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int: ...
    def _get_digital_read_array(
        self, waveform: DigitalWaveform[Any]
    ) -> NDArray[np.uint8]: ...
    def read_digital_waveforms(
        self,
        task_handle: TaskHandle,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int: ...
    def read_new_digital_waveforms(
        self,
        task_handle: TaskHandle,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[np.uint8]]: ...
    def _internal_read_digital_waveform(
        self,
        task_handle: TaskHandle,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: NDArray[np.uint8],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: NDArray[np.int64] | None,
        dt_array: NDArray[np.int64] | None,
        bytes_per_chan_array: NDArray[np.uint32] | None = None,
    ) -> tuple[
        int,  # error code
        int,  # The number of samples per channel that were read
    ]: ...
    def read_id_pin_memory(
        self, device_name: str, id_pin_name: str
    ) -> tuple[list[int], int, int]: ...
    def write_analog_waveform(
        self,
        task_handle: TaskHandle,
        waveform: AnalogWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int: ...
    def write_analog_waveforms(
        self,
        task_handle: TaskHandle,
        waveforms: Sequence[AnalogWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int: ...
    def _get_analog_write_array(
        self, waveform: AnalogWaveform[Any]
    ) -> NDArray[np.float64]: ...
    def _internal_write_analog_waveform_per_chan(
        self,
        task_handle: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        write_arrays: Sequence[NDArray[np.float64]],
    ) -> tuple[
        int,  # error code
        int,  # The number of samples per channel that were written
    ]: ...
    def write_digital_waveform(
        self,
        task_handle: TaskHandle,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int: ...
    def _get_digital_write_array(
        self, waveform: DigitalWaveform[Any]
    ) -> NDArray[np.uint8]: ...
    def write_digital_waveforms(
        self,
        task_handle: TaskHandle,
        waveforms: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int: ...
    def _internal_write_digital_waveform(
        self,
        task_handle: TaskHandle,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,
        write_array: NDArray[np.uint8],
        bytes_per_chan_array: NDArray[np.uint32] | None = None,
    ) -> tuple[
        int,  # error code
        int,  # The number of samples per channel that were written
    ]: ...
    def write_raw(
        self,
        task: TaskHandle,
        num_samps: int,
        auto_start: bool,
        timeout: float,
        write_array: NDArray[np.number[Any]],
    ) -> int: ...
    def hash_task_handle(self, task_handle: TaskHandle) -> int: ...
    def check_for_error(
        self,
        error_code: int,
        samps_per_chan_written: int | None = None,
        samps_per_chan_read: int | None = None,
    ) -> None: ...

def is_string_buffer_too_small(error_code: DAQmxErrors) -> bool: ...
def is_array_buffer_too_small(error_code: DAQmxErrors) -> bool: ...
