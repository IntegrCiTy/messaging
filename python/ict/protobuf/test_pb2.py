# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ict/protobuf/test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ict/protobuf/test.proto',
  package='backend.test',
  syntax='proto3',
  serialized_pb=_b('\n\x17ict/protobuf/test.proto\x12\x0c\x62\x61\x63kend.test\"*\n\x0cTestNodeInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x02\x62\x06proto3')
)




_TESTNODEINFO = _descriptor.Descriptor(
  name='TestNodeInfo',
  full_name='backend.test.TestNodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backend.test.TestNodeInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='backend.test.TestNodeInfo.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=41,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['TestNodeInfo'] = _TESTNODEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestNodeInfo = _reflection.GeneratedProtocolMessageType('TestNodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _TESTNODEINFO,
  __module__ = 'ict.protobuf.test_pb2'
  # @@protoc_insertion_point(class_scope:backend.test.TestNodeInfo)
  ))
_sym_db.RegisterMessage(TestNodeInfo)


# @@protoc_insertion_point(module_scope)