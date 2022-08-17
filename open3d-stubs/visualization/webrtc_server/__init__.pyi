from typing import Any, Set

import numpy as np
import numpy.typing as npt
from typing_extensions import Annotated

def call_http_api(
    entry_point: str, query_string: str = ..., data: str = ...
) -> str: ...
def disable_http_handshake() -> None: ...
def enable_webrtc() -> None: ...
def register_data_channel_message_callback(class_name, callback) -> Any: ...

__all__ = [
    "call_http_api",
    "disable_http_handshake",
    "enable_webrtc",
    "register_data_channel_message_callback",
]
