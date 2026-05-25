from ...constants import ChannelType, SyncUnlockBehavior
from ...task.channels._ai_channel import AIChannel
from ...task.channels._ao_channel import AOChannel
from ...task.channels._ci_channel import CIChannel
from ...task.channels._co_channel import COChannel
from ...task.channels._di_channel import DIChannel
from ...task.channels._do_channel import DOChannel
from ..._base_interpreter import BaseInterpreter

from ..._lib import TaskHandle
from ...system.physical_channel import PhysicalChannel

class Channel:
    def __init__(
        self,
        task_handle: TaskHandle,
        virtual_or_physical_name: str,
        interpreter: BaseInterpreter,
    ) -> None: ...
    @staticmethod
    def _factory(
        task_handle: TaskHandle,
        virtual_or_physical_name: str,
        interpreter: BaseInterpreter,
    ) -> AIChannel | AOChannel | CIChannel | COChannel | DIChannel | DOChannel: ...
    @property
    def name(self) -> str: ...
    @property
    def channel_names(self) -> list[str]: ...
    @property
    def _all_channels_name(self) -> str: ...
    @property
    def chan_type(self) -> ChannelType: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, val: str) -> None: ...
    @description.deleter
    def description(self) -> None: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def physical_channel(self) -> PhysicalChannel: ...
    @physical_channel.setter
    def physical_channel(self, val: PhysicalChannel) -> None: ...
    @property
    def sync_unlock_behavior(self) -> SyncUnlockBehavior: ...
    @sync_unlock_behavior.setter
    def sync_unlock_behavior(self, val: SyncUnlockBehavior) -> None: ...
    @sync_unlock_behavior.deleter
    def sync_unlock_behavior(self) -> None: ...
    def save(
        self,
        save_as: str | None = ...,
        author: str | None = ...,
        overwrite_existing_channel: bool | None = ...,
        allow_interactive_editing: bool | None = ...,
        allow_interactive_deletion: bool | None = ...,
    ) -> None: ...
