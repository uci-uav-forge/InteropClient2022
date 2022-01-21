#!/usr/bin/env python3

# SERVER INFO

SERVER_IP = "127.0.0.1"
SERVER_PORT = "8000"
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
USERNAME = "testadmin"
PASSWORD = "testpass"

# TOPICS

WAYPOINTS_TOPIC = "waypoints"
FLYZONES_TOPIC = "flyzones"
SEARCH_GRID_TOPIC = "search_grid_points"
AIR_DROP_BOUNDARY_TOPIC = "air_drop_boundary_points"
OFF_AXIS_ODLC_TOPIC = "off_axis_odlc_pos"
EMERGENT_LAST_KNOWN_TOPIC = "emergent_last_known_pos"
UGV_DRIVE_TOPIC = "ugv_drive_pos"

ODLC_TOPIC = "odlc"
MAPS_TOPIC = "map"
TELEMETRY_TOPIC = "telemetry"