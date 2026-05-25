from datetime import tzinfo as dt_tzinfo
from hightime import datetime as ht_datetime

def _convert_to_desired_timezone(
    expected_time_utc: ht_datetime, tzinfo: dt_tzinfo | None = None
) -> ht_datetime: ...
