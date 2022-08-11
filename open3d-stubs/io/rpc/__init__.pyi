from __future__ import annotations

import typing

import open3d.io.rpc
import open3d.t.geometry
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "BufferConnection",
    "Connection",
    "data_buffer_to_meta_geometry",
    "destroy_zmq_context",
    "set_active_camera",
    "set_legacy_camera",
    "set_mesh_data",
    "set_point_cloud",
    "set_time",
    "set_triangle_mesh",
]

class _ConnectionBase:
    pass

class Connection(_ConnectionBase):
    """
    The default connection class which uses a ZeroMQ socket.
    """

    def __init__(
        self,
        address: str = "tcp://127.0.0.1:51454",
        connect_timeout: int = 5000,
        timeout: int = 10000,
    ) -> None:
        """
        Creates a connection object
        """
    pass

class BufferConnection(_ConnectionBase):
    """
    A connection writing to a memory buffer.
    """

    def __init__(self) -> None: ...
    def get_buffer(self) -> bytes:
        """
        Returns a copy of the buffer.
        """
    pass

class _DummyReceiver:
    """
    Dummy receiver for the server side receiving requests from a client.
    """

    def __init__(
        self, address: str = "tcp://127.0.0.1:51454", timeout: int = 10000
    ) -> None:
        """
        Creates the receiver object which can be used for testing connections.
        """
    def start(self) -> None:
        """
        Starts the receiver mainloop in a new thread.
        """
    def stop(self) -> None:
        """
        Stops the receiver mainloop and joins the thread. This function blocks until the mainloop is done with processing messages that have already been received.
        """
    pass

def data_buffer_to_meta_geometry(
    data: str,
) -> typing.Tuple[str, float, open3d.t.geometry.Geometry]:
    """
    This function returns the geometry, the path and the time stored in a
    SetMeshData message. data must contain the Request header message followed
    by the SetMeshData message. The function returns None for the geometry if not
    successful.
    """

def destroy_zmq_context() -> None:
    """
    Destroys the ZMQ context.
    """
