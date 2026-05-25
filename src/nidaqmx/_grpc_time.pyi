from datetime import timezone
from datetime import datetime as std_datetime
from datetime import tzinfo as dt_tzinfo
from hightime import datetime as ht_datetime

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp

# 66 years, 17 leap days = 24107 days = 2082844800 seconds
_BIAS_FROM_1970_EPOCH = 2082844800

_NS_PER_S = 10**9
_NS_PER_US = 10**3

_YS_PER_US = 10**18
_YS_PER_NS = 10**15
_YS_PER_FS = 10**9

_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)

def convert_time_to_timestamp(
    dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None = None
) -> GrpcTimestamp: ...
def convert_timestamp_to_time(
    ts: GrpcTimestamp, tzinfo: dt_tzinfo | None = None
) -> ht_datetime: ...
