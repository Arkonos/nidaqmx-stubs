from collections.abc import Sequence
from ...system.storage.persisted_scale import PersistedScale

class PersistedScaleCollection(Sequence[PersistedScale]):
    @property
    def scale_names(self) -> list[str]: ...
