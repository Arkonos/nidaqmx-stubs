from collections.abc import Sequence
from ..storage.persisted_channel import PersistedChannel
from ..._base_interpreter import BaseInterpreter

class PersistedChannelCollection(Sequence[PersistedChannel]):
    def __init__(self, interpreter: BaseInterpreter) -> None: ...
    @property
    def global_channel_names(self) -> list[str]: ...
