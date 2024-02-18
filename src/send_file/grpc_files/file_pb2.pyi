from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("chunk", "file_size")
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    file_size: int
    def __init__(self, chunk: _Optional[bytes] = ..., file_size: _Optional[int] = ...) -> None: ...
