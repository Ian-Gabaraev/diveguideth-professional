# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: professional_unary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18professional_unary.proto\x12\x05unary"\x17\n\x05ProId\x12\x0e\n\x06pro_id\x18\x01 \x01(\x05"y\n\x0e\x43ontactDetails\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x18\n\x10instagram_handle\x18\x04 \x01(\t\x12\x17\n\x0f\x64iveplus_handle\x18\x05 \x01(\t2O\n\x11ProfessionalUnary\x12:\n\x11GetProContactInfo\x12\x0c.unary.ProId\x1a\x15.unary.ContactDetails"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "professional_unary_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PROID._serialized_start = 35
    _PROID._serialized_end = 58
    _CONTACTDETAILS._serialized_start = 60
    _CONTACTDETAILS._serialized_end = 181
    _PROFESSIONALUNARY._serialized_start = 183
    _PROFESSIONALUNARY._serialized_end = 262
# @@protoc_insertion_point(module_scope)
