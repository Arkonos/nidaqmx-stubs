from collections.abc import Sequence
from ..storage.persisted_channel import PersistedChannel
from ..._grpc_interpreter import GrpcStubInterpreter

class PersistedChannelCollection(Sequence[PersistedChannel]):
    def __init__(self, interpreter: GrpcStubInterpreter) -> None: ...
    @property
    def global_channel_names(self) -> list[str]: ...
