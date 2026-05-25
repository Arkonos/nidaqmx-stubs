import ctypes
from typing import Any
from typing_extensions import TypeAlias

_DAQ_NOT_FOUND_MESSAGE = (
    "Could not find an installation of NI-DAQmx. Please ensure that NI-DAQmx "
    "is installed on this machine or contact National Instruments for support."
)

_DAQ_NOT_SUPPORTED_MESSAGE = (
    "NI-DAQmx Python is not supported on this platform: {0}. Please "
    "direct any questions or feedback to National Instruments."
)

_FUNCTION_NOT_SUPPORTED_MESSAGE = (
    'The NI-DAQmx function "{0}" is not supported in this version '
    "of NI-DAQmx. Visit ni.com/downloads to upgrade."
)

class c_bool32(ctypes.c_uint):
    """
    Specifies a custom ctypes data type to represent 32-bit booleans.
    """

    # typeshed specifies that _SimpleCData[_T].value is an instance variable with type _T, so
    # accessing it with the descriptor protocol via its class results in "error: Access to generic
    # instance variables via class is ambiguous".

    def _getter(self) -> bool: ...
    def _setter(self, val: bool) -> None: ...

class CtypesByteString:
    """
    Custom argtype that automatically converts unicode strings to encoding
    used by the DAQmx C API DLL in Python 3.
    """
    @classmethod
    def from_param(cls, param: str) -> str: ...

ctypes_byte_str: TypeAlias = CtypesByteString

def wrapped_ndpointer(*args: Any, **kwargs: Any) -> Any: ...

class DaqFunctionImporter:
    """
    Wraps the function getter function of a ctypes library.

    Allows the NI-DAQmx Python API to fail elegantly if a function is not
    supported in the current version of the API.
    """

    def __init__(self, library: object) -> None: ...

CalHandle: TypeAlias = ctypes.c_uint
"""Calibration handle.

NIDAQmx.h defines CalHandle as a typedef for uInt32.
"""

TaskHandle: TypeAlias = ctypes.c_void_p
"""Task handle.

NIDAQmx.h defines TaskHandle as a typedef for void*.

From NI-DAQmx versions 7.0 to 8.8, TaskHandle was defined as uInt32. In NI-DAQmx 8.9, it was
changed to void* in order to support 64-bit platforms. This change did not break binary
compatibility because uInt32 and void* are the same size for 32-bit applications.
"""

def get_encoding_from_locale() -> str: ...

class DaqLibImporter:
    """
    Encapsulates NI-DAQmx library importing and handle type parsing logic.
    """

    def __init__(self) -> None: ...
    @property
    def windll(self) -> DaqFunctionImporter | None: ...
    @property
    def cdll(self) -> DaqFunctionImporter | None: ...
    @property
    def task_handle(self) -> type: ...
    @property
    def cal_handle(self) -> type: ...
    @property
    def encoding(self) -> str | None: ...
    def _import_lib(self) -> None: ...

lib_importer = DaqLibImporter()
