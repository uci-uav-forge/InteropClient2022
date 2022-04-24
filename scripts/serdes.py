#!/usr/bin/env python3

from auvsi_suas.proto import interop_api_pb2

class MissionDeserializer:
	
	def get_dict(self, mission_data):
		mission_data_dict = {
		"lost_comm_pos": self.get_lost_comm_pos(mission_data.get_lost_comm_pos),
		"flyzones": self.get_flyzones(mission_data.fly_zones),
		"waypoints": self.get_waypoints(mission_data.waypoints),
		"search_grid_points": self.get_search_grid_points(mission_data.search_grid_points),
		"off_axis_odlc_pos": self.get_off_axis_odlc_pos(mission_data.off_axis_odlc_pos),
		"emergent_last_known_pos": self.get_emergent_last_known_pos(mission_data.emergent_last_known_pos),
		"air_drop_boundary_points": self.get_air_drop_boundary_points(mission_data.air_drop_boundary_points),
		"air_drop_pos": self.get_air_drop_pos(mission_data.air_drop_pos),
		"ugv_drive_pos": self.get_ugv_drive_pos(mission_data.ugv_drive_pos),
		"map_center_pos": self.get_map_center_pos(mission_data.map_center_pos)
		}

		return mission_data_dict

	def get_waypoints(self, data): #data is a list??? mission["waypoints"] 
		coordList = []
		if len(data[0]) == 4:
			for coordPair in data:
				lat = coordPair['latitude']
				long = coordPair['longitude']
				rad = coordPair['radius']
				height = coordPair['height']
				coordList.append((lat, long, rad, height))
		elif len(data[0]) == 3:
			for coordPair in data:
				lat = coordPair['latitude']
				long = coordPair['longitude']
				alt = coordPair['altitude']
				coordList.append((lat, long, alt))
		else:
			for coordPair in data:
				lat = coordPair['latitude']
				long = coordPair['longitude']
				coordList.append((lat, long))
		# print(coordList)
		return (coordList)

	def get_lost_comm_pos(self, data):

	def get_flyzones(self, data):

	def get_off_axis_odlc_pos(self, data):

	def get_emergent_last_known_pos(self, data):

	def get_air_drop_boundary_points(self, data):

	def get_air_drop_pos(self, data):

	def get_ugv_drive_pos(self, data):

	def get_stationary_obstacles(self, data):

	def get_map_center_pos(self, data):


class TelemetrySerializer:
	
	def get_dict(self, telemetry_data):
		telemetry_data_dict = {
		"latitude":,
		"longitude":,
		"altitude":,
		"heading":
		}

		return telemetry_data_dict

class OdlcSerializer:
	
	def get_dict(self, odlc_data):
		odlc_data_dict = {
		"type":,
		"latitude":,
		"longitude":,
		"orientation":,
		"shape":,
		"shape_color":,
		"alphanumeric":,
		"alphanumeric_color":,
		"path_to_image"
		}

		return odlc_data_dict

class MapSerializer:

	def get_dict(self, map_data):
		map_data_dict = {
		"path_to_map"
		}

		return map_data_dict