# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deployment/APISync.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='deployment/APISync.proto',
  package='',
  syntax='proto3',
  serialized_options=b'ZAgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/deployment',
  serialized_pb=b'\n\x18\x64\x65ployment/APISync.proto\"0\n\x12\x43ommitObjectUpdate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\"*\n\x0cUpdateStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\"\x1a\n\x0c\x44\x65leteStatus\x12\n\n\x02id\x18\x01 \x01(\t\"\xb1\x01\n\x0e\x41PISyncRequest\x12\x31\n\x12\x63ommitObjectUpdate\x18\x01 \x01(\x0b\x32\x13.CommitObjectUpdateH\x00\x12%\n\x0cupdateStatus\x18\x02 \x01(\x0b\x32\r.UpdateStatusH\x00\x12%\n\x0c\x64\x65leteStatus\x18\x03 \x01(\x0b\x32\r.DeleteStatusH\x00\x12\x13\n\x0bpackageType\x18\x04 \x01(\tB\t\n\x07request\"+\n\rObjectUpdated\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\"+\n\rObjectDeleted\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\"\x93\x01\n\x0f\x41PISyncResponse\x12\'\n\robjectUpdated\x18\x01 \x01(\x0b\x32\x0e.ObjectUpdatedH\x00\x12\'\n\robjectDeleted\x18\x02 \x01(\x0b\x32\x0e.ObjectDeletedH\x00\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x13\n\x0bpackageType\x18\x04 \x01(\tB\n\n\x08response28\n\x07\x41PISync\x12-\n\x04Sync\x12\x0f.APISyncRequest\x1a\x10.APISyncResponse(\x01\x30\x01\x42\x43ZAgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/deploymentb\x06proto3'
)




_COMMITOBJECTUPDATE = _descriptor.Descriptor(
  name='CommitObjectUpdate',
  full_name='CommitObjectUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CommitObjectUpdate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='CommitObjectUpdate.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=76,
)


_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateStatus.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='UpdateStatus.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=120,
)


_DELETESTATUS = _descriptor.Descriptor(
  name='DeleteStatus',
  full_name='DeleteStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteStatus.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=148,
)


_APISYNCREQUEST = _descriptor.Descriptor(
  name='APISyncRequest',
  full_name='APISyncRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commitObjectUpdate', full_name='APISyncRequest.commitObjectUpdate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateStatus', full_name='APISyncRequest.updateStatus', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteStatus', full_name='APISyncRequest.deleteStatus', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageType', full_name='APISyncRequest.packageType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='APISyncRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=151,
  serialized_end=328,
)


_OBJECTUPDATED = _descriptor.Descriptor(
  name='ObjectUpdated',
  full_name='ObjectUpdated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ObjectUpdated.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='ObjectUpdated.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=373,
)


_OBJECTDELETED = _descriptor.Descriptor(
  name='ObjectDeleted',
  full_name='ObjectDeleted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ObjectDeleted.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='ObjectDeleted.object', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=418,
)


_APISYNCRESPONSE = _descriptor.Descriptor(
  name='APISyncResponse',
  full_name='APISyncResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectUpdated', full_name='APISyncResponse.objectUpdated', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectDeleted', full_name='APISyncResponse.objectDeleted', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='APISyncResponse.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageType', full_name='APISyncResponse.packageType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='APISyncResponse.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=421,
  serialized_end=568,
)

_APISYNCREQUEST.fields_by_name['commitObjectUpdate'].message_type = _COMMITOBJECTUPDATE
_APISYNCREQUEST.fields_by_name['updateStatus'].message_type = _UPDATESTATUS
_APISYNCREQUEST.fields_by_name['deleteStatus'].message_type = _DELETESTATUS
_APISYNCREQUEST.oneofs_by_name['request'].fields.append(
  _APISYNCREQUEST.fields_by_name['commitObjectUpdate'])
_APISYNCREQUEST.fields_by_name['commitObjectUpdate'].containing_oneof = _APISYNCREQUEST.oneofs_by_name['request']
_APISYNCREQUEST.oneofs_by_name['request'].fields.append(
  _APISYNCREQUEST.fields_by_name['updateStatus'])
_APISYNCREQUEST.fields_by_name['updateStatus'].containing_oneof = _APISYNCREQUEST.oneofs_by_name['request']
_APISYNCREQUEST.oneofs_by_name['request'].fields.append(
  _APISYNCREQUEST.fields_by_name['deleteStatus'])
_APISYNCREQUEST.fields_by_name['deleteStatus'].containing_oneof = _APISYNCREQUEST.oneofs_by_name['request']
_APISYNCRESPONSE.fields_by_name['objectUpdated'].message_type = _OBJECTUPDATED
_APISYNCRESPONSE.fields_by_name['objectDeleted'].message_type = _OBJECTDELETED
_APISYNCRESPONSE.oneofs_by_name['response'].fields.append(
  _APISYNCRESPONSE.fields_by_name['objectUpdated'])
_APISYNCRESPONSE.fields_by_name['objectUpdated'].containing_oneof = _APISYNCRESPONSE.oneofs_by_name['response']
_APISYNCRESPONSE.oneofs_by_name['response'].fields.append(
  _APISYNCRESPONSE.fields_by_name['objectDeleted'])
_APISYNCRESPONSE.fields_by_name['objectDeleted'].containing_oneof = _APISYNCRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['CommitObjectUpdate'] = _COMMITOBJECTUPDATE
DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
DESCRIPTOR.message_types_by_name['DeleteStatus'] = _DELETESTATUS
DESCRIPTOR.message_types_by_name['APISyncRequest'] = _APISYNCREQUEST
DESCRIPTOR.message_types_by_name['ObjectUpdated'] = _OBJECTUPDATED
DESCRIPTOR.message_types_by_name['ObjectDeleted'] = _OBJECTDELETED
DESCRIPTOR.message_types_by_name['APISyncResponse'] = _APISYNCRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommitObjectUpdate = _reflection.GeneratedProtocolMessageType('CommitObjectUpdate', (_message.Message,), {
  'DESCRIPTOR' : _COMMITOBJECTUPDATE,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:CommitObjectUpdate)
  })
_sym_db.RegisterMessage(CommitObjectUpdate)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTATUS,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStatus)
  })
_sym_db.RegisterMessage(UpdateStatus)

DeleteStatus = _reflection.GeneratedProtocolMessageType('DeleteStatus', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTATUS,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:DeleteStatus)
  })
_sym_db.RegisterMessage(DeleteStatus)

APISyncRequest = _reflection.GeneratedProtocolMessageType('APISyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _APISYNCREQUEST,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:APISyncRequest)
  })
_sym_db.RegisterMessage(APISyncRequest)

ObjectUpdated = _reflection.GeneratedProtocolMessageType('ObjectUpdated', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTUPDATED,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:ObjectUpdated)
  })
_sym_db.RegisterMessage(ObjectUpdated)

ObjectDeleted = _reflection.GeneratedProtocolMessageType('ObjectDeleted', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDELETED,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:ObjectDeleted)
  })
_sym_db.RegisterMessage(ObjectDeleted)

APISyncResponse = _reflection.GeneratedProtocolMessageType('APISyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _APISYNCRESPONSE,
  '__module__' : 'deployment.APISync_pb2'
  # @@protoc_insertion_point(class_scope:APISyncResponse)
  })
_sym_db.RegisterMessage(APISyncResponse)


DESCRIPTOR._options = None

_APISYNC = _descriptor.ServiceDescriptor(
  name='APISync',
  full_name='APISync',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=570,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sync',
    full_name='APISync.Sync',
    index=0,
    containing_service=None,
    input_type=_APISYNCREQUEST,
    output_type=_APISYNCRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_APISYNC)

DESCRIPTOR.services_by_name['APISync'] = _APISYNC

# @@protoc_insertion_point(module_scope)