import rospy
from sensor_float_msgs.msg import WTST_msg
import WTST_Pro_msg
import math
from math import pi
import numpy as np
import copy

WTSTinput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
points = [0,0]
RADIUS = 0

def pretreat(wtstinput):
    wtst=copy.deepcopy(wtstinput)
    wtst[4] = wtst[4] * np.pi / 180
    wtst[5] = (wtst[5]+5.04 )* np.pi / 180
    wtst[6] = wtst[6] * np.pi / 180
    wtst[2] = wtst[2] * np.pi / 180
    wtst[3]=wtst[3]*0.5144
    wtst[7] = wtst[7] * np.pi / 180
    if wtst[6]>np.pi:
        wtst[6]=wtst[6]-2*np.pi
    if wtst[2]>np.pi:
        wtst[2]=wtst[2]-2*np.pi
    if wtst[7]>np.pi:
        wtst[7]=wtst[7]-2*np.pi

def wtst_callback(data):
    global WTSTinput,wtst_time,wtstnum
    #print ('start')
    #rospy.loginfo("I heard %f", data.roll)
    WTSTinput[0] = data.PosX
    WTSTinput[1] = data.PosY
    WTSTinput[2] = data.DegreeTrue
    WTSTinput[3] = data.SpeedKnots
    WTSTinput[4] = data.Roll
    WTSTinput[5] = data.Pitch
    WTSTinput[6] = data.Yaw
    WTSTinput[7] = data.WindAngle
    WTSTinput[8] = data.WindSpeed
    wtst_time=data.header.stamp

def listener():
    rospy.init_node('StationKeeping', anonymous=True)
    rospy.Subscriber('wtst', WTST_msg, wtst_callback)
    rospy.spin()

class Station_Keeping():
    def __init__(self, point, input_state):
        self.point = point
        self.posX = input_state['x']
        self.posY = input_state['Y']
        self.flag = 0
        self.direction = 0
    def get_direction(self, RADIUS):
        if (self.posX)**2 + (self.posY)**2 < RADIUS**2 :
            self.flag = 1
        else:
            self.flag = 0
            self.direction = atan2((posY - point[1]), (posX - point[0]))

def dataWrapper():
    def __init__(self):
        self.Flag = 'StationKeepingFlag'
        self.Direction = 'StationKeepingDirection'
    def pubData(self,msg,station_keeping):
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'Station_Keeping'
        msg.Flag = station_keeping.flag
        msg.Direction = station_keeping.direction
        return msg
def talker():
    rospy.init_node('StationKeeping_talker', anonymous = True)
    pub = rospy.Publisher('StationKeeping', StationKeeping_msg, quene_size = 1)
    rate = rospy.Rate(10)

    station_keeping = Station_Keeping()
    msg = StationKeeping_msg()
    datawrapper = dataWrapper()
    try:
        stationkeeping_msg = datawrapper.pubData(msg, station_keeping)
        pub.publish(stationkeeping_msg)
        rate.sleep()
    except rospy.ROSInterruptException as e:
        print(e)

if __name__ == '__main__':
    listener()
    talker()