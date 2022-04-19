#!/usr/bin/env python3

import serdes
from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2

class InteropClient:
    
    def __init__(self, SERVER_URL, USERNAME, PASSWORD):
        self.SERVER_URL = SERVER_URL
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD

        self.client = client.AsyncClient(url=SERVER_URL, username=USERNAME, password=PASSWORD)

    def get_teams(self):
        return self.client.get_teams().result()

    def get_mission(self, mission_id):
        mission_data = self.client.get_mission(mission_id).result()
        return serdes.MissionDeserializer.get_dict(mission_data)

    def upload_telemetry(self, telemetry_data):
        telemetry_data = serdes.TelemetrySerializer.get_dict(telemetry_data)

        telemetry = interop_api_pb2.Telemetry()
        telemetry.latitude = telemetry_data["latitude"]
        telemetry.longitude = telemetry_data["longitude"]
        telemetry.altitude = telemetry_data["altitude"]
        telemetry.heading = telemetry_data["heading"]
        
        self.client.post_telemetry(telemetry)

    def upload_odlc(self, odlc_data):
        odlc_data = serdes.OdlcSerializer.get_dict(odlc_data)

        odlc = interop_api_pb2.Odlc()
        odlc.type = odlc_data["type"]
        odlc.latitude = odlc_data["latitude"]
        odlc.longitude = odlc_data["longitude"]
        odlc.orientation = odlc_data["orientation"]
        odlc.shape = odlc_data["shape"]
        odlc.shape_color = odlc_data["shape_color"]
        odlc.alphanumeric = odlc_data["alphanumeric"]
        odlc.alphanumeric_color = odlc_data["alphanumeric_color"]

        odlc = self.client.post_odlc(odlc)
        
        with open(odlc_data["path_to_image"], 'rb') as f:
            image_data = f.read()
            self.client.put_odlc_image(odlc.id, image_data)

    def upload_map(self, mission_id, map_data):
        map_data = serdes.MapSerializer.get_dict(map_data)

        with open(map_data["path_to_map"], 'rb') as f:
            image_data = f.read()
            self.client.put_map_image(mission_id, image_data)
