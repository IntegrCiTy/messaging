# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ict/protobuf/core.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ict/protobuf/core.proto',
  package='backend.common',
  syntax='proto3',
  serialized_pb=_b('\n\x17ict/protobuf/core.proto\x12\x0e\x62\x61\x63kend.common\x1a\x19google/protobuf/any.proto\"G\n\x0bMetaMessage\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12%\n\x07\x64\x65tails\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"\x06\n\x04Quitb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_METAMESSAGE = _descriptor.Descriptor(
  name='MetaMessage',
  full_name='backend.common.MetaMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='backend.common.MetaMessage.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details', full_name='backend.common.MetaMessage.details', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=141,
)


_QUIT = _descriptor.Descriptor(
  name='Quit',
  full_name='backend.common.Quit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=149,
)

_METAMESSAGE.fields_by_name['details'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['MetaMessage'] = _METAMESSAGE
DESCRIPTOR.message_types_by_name['Quit'] = _QUIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetaMessage = _reflection.GeneratedProtocolMessageType('MetaMessage', (_message.Message,), dict(
  DESCRIPTOR = _METAMESSAGE,
  __module__ = 'ict.protobuf.core_pb2'
  # @@protoc_insertion_point(class_scope:backend.common.MetaMessage)
  ))
_sym_db.RegisterMessage(MetaMessage)

Quit = _reflection.GeneratedProtocolMessageType('Quit', (_message.Message,), dict(
  DESCRIPTOR = _QUIT,
  __module__ = 'ict.protobuf.core_pb2'
  # @@protoc_insertion_point(class_scope:backend.common.Quit)
  ))
_sym_db.RegisterMessage(Quit)


# @@protoc_insertion_point(module_scope)
