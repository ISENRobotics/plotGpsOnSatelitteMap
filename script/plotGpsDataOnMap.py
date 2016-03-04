#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix,NavSatStatus,TimeReference
import matplotlib.pyplot as plt


def callback(data):
    rospy.loginfo("lat [%f], lon [%f], status [%i]", data.latitude, data.longitude, data.status.status)
    # with open('dataBlueTeam.txt','a') as f: f.write('{0} {1} {2}\n'.format(data.latitude, data.longitude, data.status.status))
    plt.scatter(x=[data.longitude], y=[data.latitude], s = 45, c='b') #sets your home position
    plt.show()

def initialisation():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('plotGpsDataOnMap')

    rospy.Subscriber("fix", NavSatFix, callback)

    #adjust these values based on your location and map, lat and long are in decimal degrees
    TRX = -4.49357          #top right longitude
    TRY = 48.40817            #top right latitude
    BLX = -4.49614          #bottom left longitude
    BLY = 48.40664             #bottom left latitude
    mapFile = 'mapISEN.png'
    imgMap = 0
    #now plot the data on a graph
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('POSITION (in Decimal Degrees)')

    #display the image under the graph
    #read a png file to map on
    imgMap = plt.imread('mapISEN.png')
    implot = plt.imshow(imgMap,extent=[BLX, TRX, BLY, TRY])
    plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    initialisation()
