# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interop_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='interop_api.proto',
  package='auvsi_suas.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11interop_api.proto\x12\x10\x61uvsi_suas.proto\"1\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"H\n\x06TeamId\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nuniversity\x18\x04 \x01(\t\"\xc2\x01\n\nTeamStatus\x12&\n\x04team\x18\x01 \x01(\x0b\x32\x18.auvsi_suas.proto.TeamId\x12\x0e\n\x06in_air\x18\x02 \x01(\x08\x12.\n\ttelemetry\x18\x03 \x01(\x0b\x32\x1b.auvsi_suas.proto.Telemetry\x12\x14\n\x0ctelemetry_id\x18\x04 \x01(\x03\x12\x19\n\x11telemetry_age_sec\x18\x05 \x01(\x01\x12\x1b\n\x13telemetry_timestamp\x18\x06 \x01(\t\"\x81\x05\n\x07Mission\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x32\n\x0elost_comms_pos\x18\x02 \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12,\n\tfly_zones\x18\x03 \x03(\x0b\x32\x19.auvsi_suas.proto.FlyZone\x12-\n\twaypoints\x18\x04 \x03(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x36\n\x12search_grid_points\x18\x05 \x03(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x35\n\x11off_axis_odlc_pos\x18\x06 \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x32\n\x0emap_center_pos\x18\x0c \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x12\n\nmap_height\x18\r \x01(\x01\x12;\n\x17\x65mergent_last_known_pos\x18\x07 \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12<\n\x18\x61ir_drop_boundary_points\x18\x08 \x03(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x30\n\x0c\x61ir_drop_pos\x18\t \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x31\n\rugv_drive_pos\x18\n \x01(\x0b\x32\x1a.auvsi_suas.proto.Position\x12\x42\n\x14stationary_obstacles\x18\x0b \x03(\x0b\x32$.auvsi_suas.proto.StationaryObstacle\"j\n\x07\x46lyZone\x12\x14\n\x0c\x61ltitude_min\x18\x01 \x01(\x01\x12\x14\n\x0c\x61ltitude_max\x18\x02 \x01(\x01\x12\x33\n\x0f\x62oundary_points\x18\x03 \x03(\x0b\x32\x1a.auvsi_suas.proto.Position\"A\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\"S\n\tTelemetry\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\x12\x0f\n\x07heading\x18\x04 \x01(\x01\"Y\n\x12StationaryObstacle\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x0e\n\x06radius\x18\x03 \x01(\x01\x12\x0e\n\x06height\x18\x04 \x01(\x01\"\xa7\x06\n\x04Odlc\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07mission\x18\x02 \x01(\x05\x12)\n\x04type\x18\x03 \x01(\x0e\x32\x1b.auvsi_suas.proto.Odlc.Type\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x37\n\x0borientation\x18\x06 \x01(\x0e\x32\".auvsi_suas.proto.Odlc.Orientation\x12+\n\x05shape\x18\x07 \x01(\x0e\x32\x1c.auvsi_suas.proto.Odlc.Shape\x12\x14\n\x0c\x61lphanumeric\x18\x08 \x01(\t\x12\x31\n\x0bshape_color\x18\t \x01(\x0e\x32\x1c.auvsi_suas.proto.Odlc.Color\x12\x38\n\x12\x61lphanumeric_color\x18\n \x01(\x0e\x32\x1c.auvsi_suas.proto.Odlc.Color\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x12\n\nautonomous\x18\x0c \x01(\x08\"\"\n\x04Type\x12\x0c\n\x08STANDARD\x10\x01\x12\x0c\n\x08\x45MERGENT\x10\x04\"I\n\x0bOrientation\x12\x05\n\x01N\x10\x01\x12\x06\n\x02NE\x10\x02\x12\x05\n\x01\x45\x10\x03\x12\x06\n\x02SE\x10\x04\x12\x05\n\x01S\x10\x05\x12\x06\n\x02SW\x10\x06\x12\x05\n\x01W\x10\x07\x12\x06\n\x02NW\x10\x08\"\xba\x01\n\x05Shape\x12\n\n\x06\x43IRCLE\x10\x01\x12\x0e\n\nSEMICIRCLE\x10\x02\x12\x12\n\x0eQUARTER_CIRCLE\x10\x03\x12\x0c\n\x08TRIANGLE\x10\x04\x12\n\n\x06SQUARE\x10\x05\x12\r\n\tRECTANGLE\x10\x06\x12\r\n\tTRAPEZOID\x10\x07\x12\x0c\n\x08PENTAGON\x10\x08\x12\x0b\n\x07HEXAGON\x10\t\x12\x0c\n\x08HEPTAGON\x10\n\x12\x0b\n\x07OCTAGON\x10\x0b\x12\x08\n\x04STAR\x10\x0c\x12\t\n\x05\x43ROSS\x10\r\"t\n\x05\x43olor\x12\t\n\x05WHITE\x10\x01\x12\t\n\x05\x42LACK\x10\x02\x12\x08\n\x04GRAY\x10\x03\x12\x07\n\x03RED\x10\x04\x12\x08\n\x04\x42LUE\x10\x05\x12\t\n\x05GREEN\x10\x06\x12\n\n\x06YELLOW\x10\x07\x12\n\n\x06PURPLE\x10\x08\x12\t\n\x05\x42ROWN\x10\t\x12\n\n\x06ORANGE\x10\n')
)



_ODLC_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='auvsi_suas.proto.Odlc.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENT', index=1, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1748,
  serialized_end=1782,
)
_sym_db.RegisterEnumDescriptor(_ODLC_TYPE)

_ODLC_ORIENTATION = _descriptor.EnumDescriptor(
  name='Orientation',
  full_name='auvsi_suas.proto.Odlc.Orientation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='N', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SE', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SW', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='W', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NW', index=7, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1784,
  serialized_end=1857,
)
_sym_db.RegisterEnumDescriptor(_ODLC_ORIENTATION)

_ODLC_SHAPE = _descriptor.EnumDescriptor(
  name='Shape',
  full_name='auvsi_suas.proto.Odlc.Shape',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CIRCLE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEMICIRCLE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARTER_CIRCLE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRIANGLE', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SQUARE', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECTANGLE', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAPEZOID', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENTAGON', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEXAGON', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEPTAGON', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OCTAGON', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAR', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS', index=12, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1860,
  serialized_end=2046,
)
_sym_db.RegisterEnumDescriptor(_ODLC_SHAPE)

_ODLC_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='auvsi_suas.proto.Odlc.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHITE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAY', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURPLE', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROWN', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORANGE', index=9, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2048,
  serialized_end=2164,
)
_sym_db.RegisterEnumDescriptor(_ODLC_COLOR)


_CREDENTIALS = _descriptor.Descriptor(
  name='Credentials',
  full_name='auvsi_suas.proto.Credentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='auvsi_suas.proto.Credentials.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='auvsi_suas.proto.Credentials.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=88,
)


_TEAMID = _descriptor.Descriptor(
  name='TeamId',
  full_name='auvsi_suas.proto.TeamId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='auvsi_suas.proto.TeamId.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='auvsi_suas.proto.TeamId.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='auvsi_suas.proto.TeamId.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='university', full_name='auvsi_suas.proto.TeamId.university', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=162,
)


_TEAMSTATUS = _descriptor.Descriptor(
  name='TeamStatus',
  full_name='auvsi_suas.proto.TeamStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team', full_name='auvsi_suas.proto.TeamStatus.team', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_air', full_name='auvsi_suas.proto.TeamStatus.in_air', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry', full_name='auvsi_suas.proto.TeamStatus.telemetry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_id', full_name='auvsi_suas.proto.TeamStatus.telemetry_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_age_sec', full_name='auvsi_suas.proto.TeamStatus.telemetry_age_sec', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_timestamp', full_name='auvsi_suas.proto.TeamStatus.telemetry_timestamp', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=359,
)


_MISSION = _descriptor.Descriptor(
  name='Mission',
  full_name='auvsi_suas.proto.Mission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='auvsi_suas.proto.Mission.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lost_comms_pos', full_name='auvsi_suas.proto.Mission.lost_comms_pos', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fly_zones', full_name='auvsi_suas.proto.Mission.fly_zones', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waypoints', full_name='auvsi_suas.proto.Mission.waypoints', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_grid_points', full_name='auvsi_suas.proto.Mission.search_grid_points', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='off_axis_odlc_pos', full_name='auvsi_suas.proto.Mission.off_axis_odlc_pos', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_center_pos', full_name='auvsi_suas.proto.Mission.map_center_pos', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_height', full_name='auvsi_suas.proto.Mission.map_height', index=7,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emergent_last_known_pos', full_name='auvsi_suas.proto.Mission.emergent_last_known_pos', index=8,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='air_drop_boundary_points', full_name='auvsi_suas.proto.Mission.air_drop_boundary_points', index=9,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='air_drop_pos', full_name='auvsi_suas.proto.Mission.air_drop_pos', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ugv_drive_pos', full_name='auvsi_suas.proto.Mission.ugv_drive_pos', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stationary_obstacles', full_name='auvsi_suas.proto.Mission.stationary_obstacles', index=12,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=1003,
)


_FLYZONE = _descriptor.Descriptor(
  name='FlyZone',
  full_name='auvsi_suas.proto.FlyZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='altitude_min', full_name='auvsi_suas.proto.FlyZone.altitude_min', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude_max', full_name='auvsi_suas.proto.FlyZone.altitude_max', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundary_points', full_name='auvsi_suas.proto.FlyZone.boundary_points', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1005,
  serialized_end=1111,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='auvsi_suas.proto.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='auvsi_suas.proto.Position.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='auvsi_suas.proto.Position.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='auvsi_suas.proto.Position.altitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1113,
  serialized_end=1178,
)


_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='auvsi_suas.proto.Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='auvsi_suas.proto.Telemetry.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='auvsi_suas.proto.Telemetry.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='auvsi_suas.proto.Telemetry.altitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='auvsi_suas.proto.Telemetry.heading', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1180,
  serialized_end=1263,
)


_STATIONARYOBSTACLE = _descriptor.Descriptor(
  name='StationaryObstacle',
  full_name='auvsi_suas.proto.StationaryObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='auvsi_suas.proto.StationaryObstacle.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='auvsi_suas.proto.StationaryObstacle.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='auvsi_suas.proto.StationaryObstacle.radius', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='auvsi_suas.proto.StationaryObstacle.height', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1265,
  serialized_end=1354,
)


_ODLC = _descriptor.Descriptor(
  name='Odlc',
  full_name='auvsi_suas.proto.Odlc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='auvsi_suas.proto.Odlc.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mission', full_name='auvsi_suas.proto.Odlc.mission', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='auvsi_suas.proto.Odlc.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='auvsi_suas.proto.Odlc.latitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='auvsi_suas.proto.Odlc.longitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='auvsi_suas.proto.Odlc.orientation', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='auvsi_suas.proto.Odlc.shape', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alphanumeric', full_name='auvsi_suas.proto.Odlc.alphanumeric', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape_color', full_name='auvsi_suas.proto.Odlc.shape_color', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alphanumeric_color', full_name='auvsi_suas.proto.Odlc.alphanumeric_color', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='auvsi_suas.proto.Odlc.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autonomous', full_name='auvsi_suas.proto.Odlc.autonomous', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ODLC_TYPE,
    _ODLC_ORIENTATION,
    _ODLC_SHAPE,
    _ODLC_COLOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1357,
  serialized_end=2164,
)

_TEAMSTATUS.fields_by_name['team'].message_type = _TEAMID
_TEAMSTATUS.fields_by_name['telemetry'].message_type = _TELEMETRY
_MISSION.fields_by_name['lost_comms_pos'].message_type = _POSITION
_MISSION.fields_by_name['fly_zones'].message_type = _FLYZONE
_MISSION.fields_by_name['waypoints'].message_type = _POSITION
_MISSION.fields_by_name['search_grid_points'].message_type = _POSITION
_MISSION.fields_by_name['off_axis_odlc_pos'].message_type = _POSITION
_MISSION.fields_by_name['map_center_pos'].message_type = _POSITION
_MISSION.fields_by_name['emergent_last_known_pos'].message_type = _POSITION
_MISSION.fields_by_name['air_drop_boundary_points'].message_type = _POSITION
_MISSION.fields_by_name['air_drop_pos'].message_type = _POSITION
_MISSION.fields_by_name['ugv_drive_pos'].message_type = _POSITION
_MISSION.fields_by_name['stationary_obstacles'].message_type = _STATIONARYOBSTACLE
_FLYZONE.fields_by_name['boundary_points'].message_type = _POSITION
_ODLC.fields_by_name['type'].enum_type = _ODLC_TYPE
_ODLC.fields_by_name['orientation'].enum_type = _ODLC_ORIENTATION
_ODLC.fields_by_name['shape'].enum_type = _ODLC_SHAPE
_ODLC.fields_by_name['shape_color'].enum_type = _ODLC_COLOR
_ODLC.fields_by_name['alphanumeric_color'].enum_type = _ODLC_COLOR
_ODLC_TYPE.containing_type = _ODLC
_ODLC_ORIENTATION.containing_type = _ODLC
_ODLC_SHAPE.containing_type = _ODLC
_ODLC_COLOR.containing_type = _ODLC
DESCRIPTOR.message_types_by_name['Credentials'] = _CREDENTIALS
DESCRIPTOR.message_types_by_name['TeamId'] = _TEAMID
DESCRIPTOR.message_types_by_name['TeamStatus'] = _TEAMSTATUS
DESCRIPTOR.message_types_by_name['Mission'] = _MISSION
DESCRIPTOR.message_types_by_name['FlyZone'] = _FLYZONE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Telemetry'] = _TELEMETRY
DESCRIPTOR.message_types_by_name['StationaryObstacle'] = _STATIONARYOBSTACLE
DESCRIPTOR.message_types_by_name['Odlc'] = _ODLC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), dict(
  DESCRIPTOR = _CREDENTIALS,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.Credentials)
  ))
_sym_db.RegisterMessage(Credentials)

TeamId = _reflection.GeneratedProtocolMessageType('TeamId', (_message.Message,), dict(
  DESCRIPTOR = _TEAMID,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.TeamId)
  ))
_sym_db.RegisterMessage(TeamId)

TeamStatus = _reflection.GeneratedProtocolMessageType('TeamStatus', (_message.Message,), dict(
  DESCRIPTOR = _TEAMSTATUS,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.TeamStatus)
  ))
_sym_db.RegisterMessage(TeamStatus)

Mission = _reflection.GeneratedProtocolMessageType('Mission', (_message.Message,), dict(
  DESCRIPTOR = _MISSION,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.Mission)
  ))
_sym_db.RegisterMessage(Mission)

FlyZone = _reflection.GeneratedProtocolMessageType('FlyZone', (_message.Message,), dict(
  DESCRIPTOR = _FLYZONE,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.FlyZone)
  ))
_sym_db.RegisterMessage(FlyZone)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.Position)
  ))
_sym_db.RegisterMessage(Position)

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), dict(
  DESCRIPTOR = _TELEMETRY,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.Telemetry)
  ))
_sym_db.RegisterMessage(Telemetry)

StationaryObstacle = _reflection.GeneratedProtocolMessageType('StationaryObstacle', (_message.Message,), dict(
  DESCRIPTOR = _STATIONARYOBSTACLE,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.StationaryObstacle)
  ))
_sym_db.RegisterMessage(StationaryObstacle)

Odlc = _reflection.GeneratedProtocolMessageType('Odlc', (_message.Message,), dict(
  DESCRIPTOR = _ODLC,
  __module__ = 'interop_api_pb2'
  # @@protoc_insertion_point(class_scope:auvsi_suas.proto.Odlc)
  ))
_sym_db.RegisterMessage(Odlc)


# @@protoc_insertion_point(module_scope)