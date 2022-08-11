"""Functionality for remote visualization over WebRTC."""
from __future__ import annotations

import typing

import open3d.visualization.webrtc_server
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "call_http_api",
    "disable_http_handshake",
    "enable_webrtc",
    "register_data_channel_message_callback",
]

def call_http_api(entry_point: str, query_string: str = "", data: str = "") -> str:
    """
    Emulates Open3D WebRTCWindowSystem's HTTP API calls. This is used when the HTTP handshake server is disabled (e.g. in Jupyter), and handshakes are done by this function.
    """

def disable_http_handshake() -> None:
    """
    Disables the HTTP handshake server. In Jupyter environment, WebRTC handshake is performed by call_http_api() with Jupyter's own COMMS interface, thus the HTTP server shall be turned off.
    """

def enable_webrtc() -> None:
    """
    Use WebRTC streams to display rendered gui window.
    """
