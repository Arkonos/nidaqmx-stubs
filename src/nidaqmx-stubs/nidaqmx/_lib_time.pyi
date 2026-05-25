import ctypes
import functools
from datetime import timezone
from datetime import datetime as std_datetime
from datetime import tzinfo as dt_tzinfo
from hightime import datetime as ht_datetime
from typing import Any

@functools.total_ordering
class AbsoluteTime(ctypes.Structure):
    # Please visit ni.com/info and enter the Info Code NI_BTF for detailed information.
    # The summary is:
    #    * lsb - positive fractions (2^-64) of a second
    #    * msb - number of whole seconds since 12am, Friday, January 1, 1904, UTC

    _pack_ = 4
    _fields_ = [("lsb", ctypes.c_uint64), ("msb", ctypes.c_int64)]

    # 66 years, 17 leap days = 24107 days = 2082844800 seconds
    _BIAS_FROM_1970_EPOCH = 2082844800
    _NUM_SUBSECONDS = 2**64
    _US_PER_S = 10**6
    _YS_PER_S = 10**24
    _YS_PER_US = 10**18
    _YS_PER_FS = 10**9

    MAX_FS = 10**9
    MAX_YS = 10**9

    _EPOCH_1904 = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)

    @classmethod
    def from_datetime(cls, dt: std_datetime | ht_datetime) -> AbsoluteTime: ...
    def to_datetime(self, tzinfo: dt_tzinfo | None = None) -> ht_datetime: ...
    def __str__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
