from .error_codes import DAQmxErrors, DAQmxWarnings

__all__ = [
    "DaqError",
    "DaqReadError",
    "DaqWriteError",
    "DaqWarning",
    "DaqResourceWarning",
]

class Error(Exception): ...
class DaqNotFoundError(Error): ...
class DaqNotSupportedError(Error): ...
class DaqFunctionNotSupportedError(Error): ...

class DaqError(Error):
    """
    Error raised by any DAQmx method.
    """
    def __init__(self, message: str, error_code: int, task_name: str = "") -> None: ...
    @property
    def error_code(self) -> int: ...
    @property
    def error_type(self) -> DAQmxErrors: ...

class DaqReadError(DaqError):
    def __init__(
        self,
        message: str,
        error_code: int,
        samps_per_chan_read: int,
        task_name: str = "",
    ) -> None: ...
    @property
    def samps_per_chan_read(self) -> int: ...

class DaqWriteError(DaqError):
    """
    Error raised by DAQmx write method that includes the amount of data that was
    written.
    """
    def __init__(
        self,
        message: str,
        error_code: int,
        samps_per_chan_written: int,
        task_name: str = "",
    ) -> None: ...
    @property
    def samps_per_chan_written(self) -> int: ...

class DaqWarning(Warning):
    """
    Warning raised by any NI-DAQmx method.
    """
    def __init__(self, message: str, error_code: int) -> None: ...
    @property
    def error_code(self) -> int: ...
    @property
    def error_type(self) -> DAQmxWarnings: ...

class DaqResourceWarning(ResourceWarning): ...
