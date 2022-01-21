#!/usr/bin/env python3


# AUVSI SUAS UAV Forge
# Interop Client + ROS

from constants import *
from interop_client import InteropClient

import rospy
from std_msgs.msg import String

import threading

def talker():
    mission_data = client.get_mission(1)

    waypoints_pub = rospy.Publisher(WAYPOINTS_TOPIC, Waypoints, queue_size=10)
    flyzones_pub = rospy.Pubsliher(FLYZONES_TOPIC, FlyZones, queue_size=10)
    search_grid_pub = rospy.Publisher(SEARCH_GRID_TOPIC, GeoPolygonStamped, queue_size=10)
    air_drop_boundary_pub = rospy.Publisher(AIR_DROP_BOUNDARY_TOPIC, GeoPointStamped, queue_size=10)
    off_axis_odlc_pub = rospy.Publisher(OFF_AXIS_ODLC_TOPIC, GeoPointStamped, queue_size=10)
    emergent_last_known_pub = rospy.Publisher(EMERGENT_LAST_KNOWN_TOPIC, GeoPointStamped, queue_size=10)
    ugv_drive_pub = rospy.Pubsliher(UGV_DRIVE_TOPIC, GeoPointStamped, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        waypoints_pub.pulish(mission_data[WAYPOINTS_TOPIC])
        flyzones_pub.publish(mission_data[FLYZONES_TOPIC])
        search_grid_pub.publish(mission_data[SEARCH_GRID_TOPIC])
        air_drop_boundary_pub.publish(mission_data[AIR_DROP_BOUNDARY_TOPIC])
        off_axis_odlc_pub.publish(mission_data[OFF_AXIS_ODLC_TOPIC])
        emergent_last_known_pub.publish(mission_data[EMERGENT_LAST_KNOWN_TOPIC])
        ugv_drive_pub.publish(mission_data[UGV_DRIVE_TOPIC])

        rate.sleep()

def odlc_callback(data):
    client.upload_odlc(data)

def maps_callback(data):
    client.upload_map(1, data)

def telemetry_callback(data):
    client.upload_telemetry(data)

def listener():
    rospy.Subscriber(ODLC_TOPIC, Odlc, odlc_callback)
    rospy.Subscriber(MAPS_TOPIC, Map, maps_callback)
    rospy.Subscriber(TELEMETRY_TOPIC, Telemetry, telemetry_callback)

    rospy.spin()

def main():
    rospy.init_node('interop_client', anonymous=True)

    global client
    client = InteropClient(SERVER_URL, USERNAME, PASSWORD)

    listenerThread = threading.Thread(target=listener)
    listenerThread.setDaemon(True)
    listenerThread.start()
    talker()

if __name__ == "__main__":
    main()
