from dataclasses import dataclass
from ._base_interpreter import BaseInterpreter
from .grpc_session_options import GrpcSessionOptions

@dataclass
class _ChannelInfo:
    def to_flattened_name(self) -> str: ...

def flatten_channel_string(channel_names: list[str]) -> str: ...
def unflatten_channel_string(channel_names: str) -> list[str]: ...
def _select_interpreter(
    grpc_options: GrpcSessionOptions | None = None,
    interpreter: BaseInterpreter | None = None,
) -> BaseInterpreter: ...
