# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbase.proto\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"3\n\tRectangle\x12\x12\n\x02lo\x18\x01 \x01(\x0b\x32\x06.Point\x12\x12\n\x02hi\x18\x02 \x01(\x0b\x32\x06.Point\"1\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x08location\x18\x02 \x01(\x0b\x32\x06.Point2X\n\nRouteGuide\x12 \n\nGetFeature\x12\x06.Point\x1a\x08.Feature\"\x00\x12(\n\x0cListFeatures\x12\n.Rectangle\x1a\x08.Feature\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POINT']._serialized_start=14
  _globals['_POINT']._serialized_end=58
  _globals['_RECTANGLE']._serialized_start=60
  _globals['_RECTANGLE']._serialized_end=111
  _globals['_FEATURE']._serialized_start=113
  _globals['_FEATURE']._serialized_end=162
  _globals['_ROUTEGUIDE']._serialized_start=164
  _globals['_ROUTEGUIDE']._serialized_end=252
# @@protoc_insertion_point(module_scope)