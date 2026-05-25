from .constants import ScaleType, UnitsPreScaled
from .grpc_session_options import GrpcSessionOptions
from ._base_interpreter import BaseInterpreter

__all__ = ["Scale"]

class Scale:
    def __init__(
        self, name: str, *, grpc_options: GrpcSessionOptions | None = None
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, val: str) -> None: ...
    @property
    def lin_slope(self) -> float: ...
    @lin_slope.setter
    def lin_slope(self, val: float) -> None: ...
    @property
    def lin_y_intercept(self) -> float: ...
    @lin_y_intercept.setter
    def lin_y_intercept(self, val: float) -> None: ...
    @property
    def map_pre_scaled_max(self) -> float: ...
    @map_pre_scaled_max.setter
    def map_pre_scaled_max(self, val: float) -> None: ...
    @property
    def map_pre_scaled_min(self) -> float: ...
    @map_pre_scaled_min.setter
    def map_pre_scaled_min(self, val: float) -> None: ...
    @property
    def map_scaled_max(self) -> float: ...
    @map_scaled_max.setter
    def map_scaled_max(self, val: float) -> None: ...
    @property
    def map_scaled_min(self) -> float: ...
    @map_scaled_min.setter
    def map_scaled_min(self, val: float) -> None: ...
    @property
    def poly_forward_coeff(self) -> list[float]: ...
    @poly_forward_coeff.setter
    def poly_forward_coeff(self, val: list[float]) -> None: ...
    @property
    def poly_reverse_coeff(self) -> list[float]: ...
    @poly_reverse_coeff.setter
    def poly_reverse_coeff(self, val: list[float]) -> None: ...
    @property
    def pre_scaled_units(self) -> UnitsPreScaled: ...
    @pre_scaled_units.setter
    def pre_scaled_units(self, val: UnitsPreScaled) -> None: ...
    @property
    def scale_type(self) -> ScaleType: ...
    @property
    def scaled_units(self) -> str: ...
    @scaled_units.setter
    def scaled_units(self, val: str) -> None: ...
    @property
    def table_pre_scaled_vals(self) -> list[float]: ...
    @table_pre_scaled_vals.setter
    def table_pre_scaled_vals(self, val: list[float]) -> None: ...
    @property
    def table_scaled_vals(self) -> list[float]: ...
    @table_scaled_vals.setter
    def table_scaled_vals(self, val: list[float]) -> None: ...
    @staticmethod
    def calculate_reverse_poly_coeff(
        forward_coeffs: list[float],
        min_val_x: float = -5.0,
        max_val_x: float = 5.0,
        num_points_to_compute: int = 1000,
        reverse_poly_order: int = -1,
        *,
        grpc_options: GrpcSessionOptions | None = None,
    ) -> list[float]: ...
    @staticmethod
    def create_lin_scale(
        scale_name: str,
        slope: float,
        y_intercept: float = 0.0,
        pre_scaled_units: UnitsPreScaled = UnitsPreScaled.VOLTS,
        scaled_units: str | None = None,
        *,
        grpc_options: GrpcSessionOptions | None = None,
    ) -> Scale: ...
    @staticmethod
    def create_map_scale(
        scale_name: str,
        prescaled_min: float,
        prescaled_max: float,
        scaled_min: float,
        scaled_max: float,
        pre_scaled_units: UnitsPreScaled = UnitsPreScaled.VOLTS,
        scaled_units: str | None = None,
        *,
        grpc_options: GrpcSessionOptions | None = None,
    ) -> Scale: ...
    @staticmethod
    def create_polynomial_scale(
        scale_name: str,
        forward_coeffs: list[float],
        reverse_coeffs: list[float],
        pre_scaled_units: UnitsPreScaled = UnitsPreScaled.VOLTS,
        scaled_units: str | None = None,
        *,
        grpc_options: GrpcSessionOptions | None = None,
    ) -> Scale: ...
    @staticmethod
    def create_table_scale(
        scale_name: str,
        prescaled_vals: list[float],
        scaled_vals: list[float],
        pre_scaled_units: UnitsPreScaled = UnitsPreScaled.VOLTS,
        scaled_units: str | None = None,
        *,
        grpc_options: GrpcSessionOptions | None = None,
    ) -> Scale: ...
    def save(
        self,
        save_as: str = "",
        author: str = "",
        overwrite_existing_scale: bool = False,
        allow_interactive_editing: bool = True,
        allow_interactive_deletion: bool = True,
    ) -> None: ...

class _ScaleAlternateConstructor(Scale):
    def __init__(self, name: str, interpreter: BaseInterpreter) -> None: ...
