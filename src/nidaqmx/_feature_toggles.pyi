from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar

from decouple import AutoConfig, Undefined, undefined

from ._dotenv_path import get_dotenv_search_path

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Self

    _P = ParamSpec("_P")
    _T = TypeVar("_T")

_PREFIX = "NIDAQMX"

if TYPE_CHECKING:
    # Work around decouple's lack of type hints.
    def _config(
        option: str,
        default: _T | Undefined = undefined,
        cast: Callable[[str], _T] | Undefined = undefined,
    ) -> _T: ...

else:
    _config = AutoConfig(str(get_dotenv_search_path()))

# Based on the recipe at https://docs.python.org/3/howto/enum.html
class _OrderedEnum:
    _DUMMY_MEMBER = 0
    def __ge__(self, other: Self) -> bool: ...
    def __gt__(self, other: Self) -> bool: ...
    def __le__(self, other: Self) -> bool: ...
    def __lt__(self, other: Self) -> bool: ...

class CodeReadiness(_OrderedEnum):
    """Indicates whether code is ready to be supported."""

    RELEASE = 0
    NEXT_RELEASE = 1
    INCOMPLETE = 2
    PROTOTYPE = 3

def _init_code_readiness_level() -> CodeReadiness: ...

# This is not public because `from _feature_toggles import CODE_READINESS_LEVEL`
# is incompatible with the patching performed by the use_code_readiness mark.
_CODE_READINESS_LEVEL = _init_code_readiness_level()

def get_code_readiness_level() -> CodeReadiness: ...

class FeatureToggle:
    """A run-time feature toggle."""

    name: str
    """The name of the feature."""

    readiness: CodeReadiness
    """The code readiness at which this feature is enabled."""

    def __init__(self, name: str, readiness: CodeReadiness) -> None: ...
    @property
    def is_enabled(self) -> bool: ...
    def raise_if_disabled(self) -> None: ...

def requires_feature(
    feature_toggle: FeatureToggle,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...

WAVEFORM_SUPPORT = FeatureToggle("WAVEFORM_SUPPORT", CodeReadiness.RELEASE)
