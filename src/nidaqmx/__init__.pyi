"""The NI-DAQmx API for Python."""

from importlib.metadata import version

from .errors import (
    DaqError,
    DaqReadError,
    DaqResourceWarning,
    DaqWarning,
    DaqWriteError,
)
from .grpc_session_options import *  # noqa: F403 - 'from nidaqmx.grpc_session_options import *' used; unable to detect undefined names (auto-generated noqa)
from .scale import Scale
from .task import Task
from .types import CtrFreq, CtrTick, CtrTime

__version__ = version(__name__)

__all__ = [
    "DaqError",
    "DaqReadError",
    "DaqResourceWarning",
    "DaqWarning",
    "DaqWriteError",
    "Scale",
    "Task",
    "CtrFreq",
    "CtrTick",
    "CtrTime",
    "errors",
    "scale",
    "task",
]

# Do not add a null logging handler. If the application has not configured logging, the
# default behavior is to log warnings and errors to stderr.
