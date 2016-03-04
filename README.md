# plotGpsOnSatelitteMap

This ROS Node plot GPS data on a map

## Prerequis

This node is built with catkin under ROS Indigo. It subscribe to /fix (sensor_msgs/NavSatFix Message) and plot on a map the position in "real time".

This node connect to ROS_MASTER_URI and wait /fix messages. Could run when reading a bag file or during real experiment when connected to ROS_MASTER_URI.

## Usage

1. cd ~/catkin_ws
2. git clone https://github.com/ISENRobotics/plotGpsOnSatelitteMap.git
3. catkin_make
4. rosrun plotGpsOnSatelitteMap plotGpsDataOnMap.py

## Creating a map

1. With google map/earth or other, put two points (better with google earth) at bottom left and top right corners. Please Note those coordinates, they will be used to fit the image with coordinate system.
2. With the software you prefer, crop this image to fit with corner points.
3. In the main script plotGpsDataOnMap.py, in function Initialisation, put your coordinates and mapfile.

Run the script under the folder script so the script could find the image file.
