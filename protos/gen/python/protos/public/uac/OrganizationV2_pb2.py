# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/OrganizationV2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import CommonService_pb2 as common_dot_CommonService__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uac/OrganizationV2.proto',
  package='ai.verta.uac',
  syntax='proto3',
  serialized_options=b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac',
  serialized_pb=b'\n\x18uac/OrganizationV2.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x1a\x63ommon/CommonService.proto\x1a\x14uac/UACService.proto\"\x1b\n\nOrgAdminV2\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\x9f\x01\n\x0eOrganizationV2\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12(\n\x06\x61\x64mins\x18\x06 \x03(\x0b\x32\x18.ai.verta.uac.OrgAdminV2\x12\x19\n\x11\x63reated_timestamp\x18\x04 \x01(\x03\x12\x19\n\x11updated_timestamp\x18\x05 \x01(\x03\"g\n\x15GetOrganizationByIdV2\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x1a>\n\x08Response\x12\x32\n\x0corganization\x18\x01 \x01(\x0b\x32\x1c.ai.verta.uac.OrganizationV2\"k\n\x17GetOrganizationByNameV2\x12\x10\n\x08org_name\x18\x01 \x01(\t\x1a>\n\x08Response\x12\x32\n\x0corganization\x18\x01 \x01(\x0b\x32\x1c.ai.verta.uac.OrganizationV2\"\xd0\x01\n\x13ListOrganizationsV2\x12/\n\npagination\x18\x01 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\x1a\x87\x01\n\x08Response\x12\x33\n\rorganizations\x18\x01 \x03(\x0b\x32\x1c.ai.verta.uac.OrganizationV2\x12\x15\n\rtotal_records\x18\x02 \x01(\x03\x12/\n\npagination\x18\x03 \x01(\x0b\x32\x1b.ai.verta.common.Pagination\"\x87\x01\n\x11SetOrganizationV2\x12\x32\n\x0corganization\x18\x01 \x01(\x0b\x32\x1c.ai.verta.uac.OrganizationV2\x1a>\n\x08Response\x12\x32\n\x0corganization\x18\x01 \x01(\x0b\x32\x1c.ai.verta.uac.OrganizationV2\"2\n\x14\x44\x65leteOrganizationV2\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x1a\n\n\x08Response2\xcd\x05\n\x15OrganizationServiceV2\x12\x8b\x01\n\x13getOrganizationById\x12#.ai.verta.uac.GetOrganizationByIdV2\x1a,.ai.verta.uac.GetOrganizationByIdV2.Response\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/organization/{org_id}\x12\x9e\x01\n\x15getOrganizationByName\x12%.ai.verta.uac.GetOrganizationByNameV2\x1a..ai.verta.uac.GetOrganizationByNameV2.Response\".\x82\xd3\xe4\x93\x02(\x12&/v2/organization/getOrganizationByName\x12|\n\x11listOrganizations\x12!.ai.verta.uac.ListOrganizationsV2\x1a*.ai.verta.uac.ListOrganizationsV2.Response\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v2/organization\x12y\n\x0fsetOrganization\x12\x1f.ai.verta.uac.SetOrganizationV2\x1a(.ai.verta.uac.SetOrganizationV2.Response\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/organization:\x01*\x12\x8b\x01\n\x12\x64\x65leteOrganization\x12\".ai.verta.uac.DeleteOrganizationV2\x1a+.ai.verta.uac.DeleteOrganizationV2.Response\"$\x82\xd3\xe4\x93\x02\x1e*\x19/v2/organization/{org_id}:\x01*B>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,common_dot_CommonService__pb2.DESCRIPTOR,uac_dot_UACService__pb2.DESCRIPTOR,])




_ORGADMINV2 = _descriptor.Descriptor(
  name='OrgAdminV2',
  full_name='ai.verta.uac.OrgAdminV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='ai.verta.uac.OrgAdminV2.email', index=0,
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
  serialized_end=149,
)


_ORGANIZATIONV2 = _descriptor.Descriptor(
  name='OrganizationV2',
  full_name='ai.verta.uac.OrganizationV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.OrganizationV2.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ai.verta.uac.OrganizationV2.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.uac.OrganizationV2.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admins', full_name='ai.verta.uac.OrganizationV2.admins', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='ai.verta.uac.OrganizationV2.created_timestamp', index=4,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='ai.verta.uac.OrganizationV2.updated_timestamp', index=5,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=152,
  serialized_end=311,
)


_GETORGANIZATIONBYIDV2_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.GetOrganizationByIdV2.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='ai.verta.uac.GetOrganizationByIdV2.Response.organization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=354,
  serialized_end=416,
)

_GETORGANIZATIONBYIDV2 = _descriptor.Descriptor(
  name='GetOrganizationByIdV2',
  full_name='ai.verta.uac.GetOrganizationByIdV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='ai.verta.uac.GetOrganizationByIdV2.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETORGANIZATIONBYIDV2_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=416,
)


_GETORGANIZATIONBYNAMEV2_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.GetOrganizationByNameV2.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='ai.verta.uac.GetOrganizationByNameV2.Response.organization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=354,
  serialized_end=416,
)

_GETORGANIZATIONBYNAMEV2 = _descriptor.Descriptor(
  name='GetOrganizationByNameV2',
  full_name='ai.verta.uac.GetOrganizationByNameV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_name', full_name='ai.verta.uac.GetOrganizationByNameV2.org_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETORGANIZATIONBYNAMEV2_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=525,
)


_LISTORGANIZATIONSV2_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.ListOrganizationsV2.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizations', full_name='ai.verta.uac.ListOrganizationsV2.Response.organizations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_records', full_name='ai.verta.uac.ListOrganizationsV2.Response.total_records', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ai.verta.uac.ListOrganizationsV2.Response.pagination', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=601,
  serialized_end=736,
)

_LISTORGANIZATIONSV2 = _descriptor.Descriptor(
  name='ListOrganizationsV2',
  full_name='ai.verta.uac.ListOrganizationsV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='ai.verta.uac.ListOrganizationsV2.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTORGANIZATIONSV2_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=736,
)


_SETORGANIZATIONV2_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.SetOrganizationV2.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='ai.verta.uac.SetOrganizationV2.Response.organization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=354,
  serialized_end=416,
)

_SETORGANIZATIONV2 = _descriptor.Descriptor(
  name='SetOrganizationV2',
  full_name='ai.verta.uac.SetOrganizationV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='ai.verta.uac.SetOrganizationV2.organization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SETORGANIZATIONV2_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=874,
)


_DELETEORGANIZATIONV2_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.DeleteOrganizationV2.Response',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=364,
)

_DELETEORGANIZATIONV2 = _descriptor.Descriptor(
  name='DeleteOrganizationV2',
  full_name='ai.verta.uac.DeleteOrganizationV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='ai.verta.uac.DeleteOrganizationV2.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEORGANIZATIONV2_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=926,
)

_ORGANIZATIONV2.fields_by_name['admins'].message_type = _ORGADMINV2
_GETORGANIZATIONBYIDV2_RESPONSE.fields_by_name['organization'].message_type = _ORGANIZATIONV2
_GETORGANIZATIONBYIDV2_RESPONSE.containing_type = _GETORGANIZATIONBYIDV2
_GETORGANIZATIONBYNAMEV2_RESPONSE.fields_by_name['organization'].message_type = _ORGANIZATIONV2
_GETORGANIZATIONBYNAMEV2_RESPONSE.containing_type = _GETORGANIZATIONBYNAMEV2
_LISTORGANIZATIONSV2_RESPONSE.fields_by_name['organizations'].message_type = _ORGANIZATIONV2
_LISTORGANIZATIONSV2_RESPONSE.fields_by_name['pagination'].message_type = common_dot_CommonService__pb2._PAGINATION
_LISTORGANIZATIONSV2_RESPONSE.containing_type = _LISTORGANIZATIONSV2
_LISTORGANIZATIONSV2.fields_by_name['pagination'].message_type = common_dot_CommonService__pb2._PAGINATION
_SETORGANIZATIONV2_RESPONSE.fields_by_name['organization'].message_type = _ORGANIZATIONV2
_SETORGANIZATIONV2_RESPONSE.containing_type = _SETORGANIZATIONV2
_SETORGANIZATIONV2.fields_by_name['organization'].message_type = _ORGANIZATIONV2
_DELETEORGANIZATIONV2_RESPONSE.containing_type = _DELETEORGANIZATIONV2
DESCRIPTOR.message_types_by_name['OrgAdminV2'] = _ORGADMINV2
DESCRIPTOR.message_types_by_name['OrganizationV2'] = _ORGANIZATIONV2
DESCRIPTOR.message_types_by_name['GetOrganizationByIdV2'] = _GETORGANIZATIONBYIDV2
DESCRIPTOR.message_types_by_name['GetOrganizationByNameV2'] = _GETORGANIZATIONBYNAMEV2
DESCRIPTOR.message_types_by_name['ListOrganizationsV2'] = _LISTORGANIZATIONSV2
DESCRIPTOR.message_types_by_name['SetOrganizationV2'] = _SETORGANIZATIONV2
DESCRIPTOR.message_types_by_name['DeleteOrganizationV2'] = _DELETEORGANIZATIONV2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrgAdminV2 = _reflection.GeneratedProtocolMessageType('OrgAdminV2', (_message.Message,), {
  'DESCRIPTOR' : _ORGADMINV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.OrgAdminV2)
  })
_sym_db.RegisterMessage(OrgAdminV2)

OrganizationV2 = _reflection.GeneratedProtocolMessageType('OrganizationV2', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.OrganizationV2)
  })
_sym_db.RegisterMessage(OrganizationV2)

GetOrganizationByIdV2 = _reflection.GeneratedProtocolMessageType('GetOrganizationByIdV2', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETORGANIZATIONBYIDV2_RESPONSE,
    '__module__' : 'uac.OrganizationV2_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.GetOrganizationByIdV2.Response)
    })
  ,
  'DESCRIPTOR' : _GETORGANIZATIONBYIDV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.GetOrganizationByIdV2)
  })
_sym_db.RegisterMessage(GetOrganizationByIdV2)
_sym_db.RegisterMessage(GetOrganizationByIdV2.Response)

GetOrganizationByNameV2 = _reflection.GeneratedProtocolMessageType('GetOrganizationByNameV2', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETORGANIZATIONBYNAMEV2_RESPONSE,
    '__module__' : 'uac.OrganizationV2_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.GetOrganizationByNameV2.Response)
    })
  ,
  'DESCRIPTOR' : _GETORGANIZATIONBYNAMEV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.GetOrganizationByNameV2)
  })
_sym_db.RegisterMessage(GetOrganizationByNameV2)
_sym_db.RegisterMessage(GetOrganizationByNameV2.Response)

ListOrganizationsV2 = _reflection.GeneratedProtocolMessageType('ListOrganizationsV2', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _LISTORGANIZATIONSV2_RESPONSE,
    '__module__' : 'uac.OrganizationV2_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.ListOrganizationsV2.Response)
    })
  ,
  'DESCRIPTOR' : _LISTORGANIZATIONSV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.ListOrganizationsV2)
  })
_sym_db.RegisterMessage(ListOrganizationsV2)
_sym_db.RegisterMessage(ListOrganizationsV2.Response)

SetOrganizationV2 = _reflection.GeneratedProtocolMessageType('SetOrganizationV2', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _SETORGANIZATIONV2_RESPONSE,
    '__module__' : 'uac.OrganizationV2_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.SetOrganizationV2.Response)
    })
  ,
  'DESCRIPTOR' : _SETORGANIZATIONV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.SetOrganizationV2)
  })
_sym_db.RegisterMessage(SetOrganizationV2)
_sym_db.RegisterMessage(SetOrganizationV2.Response)

DeleteOrganizationV2 = _reflection.GeneratedProtocolMessageType('DeleteOrganizationV2', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _DELETEORGANIZATIONV2_RESPONSE,
    '__module__' : 'uac.OrganizationV2_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteOrganizationV2.Response)
    })
  ,
  'DESCRIPTOR' : _DELETEORGANIZATIONV2,
  '__module__' : 'uac.OrganizationV2_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteOrganizationV2)
  })
_sym_db.RegisterMessage(DeleteOrganizationV2)
_sym_db.RegisterMessage(DeleteOrganizationV2.Response)


DESCRIPTOR._options = None

_ORGANIZATIONSERVICEV2 = _descriptor.ServiceDescriptor(
  name='OrganizationServiceV2',
  full_name='ai.verta.uac.OrganizationServiceV2',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=929,
  serialized_end=1646,
  methods=[
  _descriptor.MethodDescriptor(
    name='getOrganizationById',
    full_name='ai.verta.uac.OrganizationServiceV2.getOrganizationById',
    index=0,
    containing_service=None,
    input_type=_GETORGANIZATIONBYIDV2,
    output_type=_GETORGANIZATIONBYIDV2_RESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/v2/organization/{org_id}',
  ),
  _descriptor.MethodDescriptor(
    name='getOrganizationByName',
    full_name='ai.verta.uac.OrganizationServiceV2.getOrganizationByName',
    index=1,
    containing_service=None,
    input_type=_GETORGANIZATIONBYNAMEV2,
    output_type=_GETORGANIZATIONBYNAMEV2_RESPONSE,
    serialized_options=b'\202\323\344\223\002(\022&/v2/organization/getOrganizationByName',
  ),
  _descriptor.MethodDescriptor(
    name='listOrganizations',
    full_name='ai.verta.uac.OrganizationServiceV2.listOrganizations',
    index=2,
    containing_service=None,
    input_type=_LISTORGANIZATIONSV2,
    output_type=_LISTORGANIZATIONSV2_RESPONSE,
    serialized_options=b'\202\323\344\223\002\022\022\020/v2/organization',
  ),
  _descriptor.MethodDescriptor(
    name='setOrganization',
    full_name='ai.verta.uac.OrganizationServiceV2.setOrganization',
    index=3,
    containing_service=None,
    input_type=_SETORGANIZATIONV2,
    output_type=_SETORGANIZATIONV2_RESPONSE,
    serialized_options=b'\202\323\344\223\002\025\"\020/v2/organization:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='deleteOrganization',
    full_name='ai.verta.uac.OrganizationServiceV2.deleteOrganization',
    index=4,
    containing_service=None,
    input_type=_DELETEORGANIZATIONV2,
    output_type=_DELETEORGANIZATIONV2_RESPONSE,
    serialized_options=b'\202\323\344\223\002\036*\031/v2/organization/{org_id}:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGANIZATIONSERVICEV2)

DESCRIPTOR.services_by_name['OrganizationServiceV2'] = _ORGANIZATIONSERVICEV2

# @@protoc_insertion_point(module_scope)