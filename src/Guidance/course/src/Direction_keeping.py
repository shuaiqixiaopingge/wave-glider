import rospy
import math
from math import pi
import numpy as np
import copy

WTSTinput = [0, 0, 0, 0, 0, 0, 0, 0, 0]
direction = 0

def dataWrapper():
    def __init__(self):
        self.Direction = 'Directiokeeping'
    def pubData(self,msg,Keeping_Direction):
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'DirectionKeeping'
        msg.Direction = Keeping_Direction
        return msg
def talker(keepingdirection):
    rospy.init_node('DirectionKeeping_talker', anonymous = True)
    pub = rospy.Publisher('DirectionKeeping', DirectionKeeping_msg, quene_size = 1)
    rate = rospy.Rate(10)
    msg = DirectionKeeping_msg()
    datawrapper = dataWrapper()
    try:
        keepingdirection_msg = datawrapper.pubData(msg, keepingdirection)
        pub.publish(keepingdirection_msg)
        rate.sleep()
    except rospy.ROSInterruptException as e:
        print(e)

if __name__ == '__main__':
    talker(direction)