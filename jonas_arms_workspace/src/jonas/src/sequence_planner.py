#!/usr/bin/env python

# --- Import libraries

import rospy

import numpy as np
import time
import actionlib

from std_msgs.msg import Int16MultiArray

from jonas.srv import sequence, sequenceResponse


# ----------- Classes

class Planner(object):

    sequence_active = True
    service_result = False

    msg = Int16MultiArray()



    def __init__(self):

        # ------------------------------------- Create publisher

        self.jointPublisher = rospy.Publisher("joint_value",Int16MultiArray, queue_size=10)
        
        rospy.sleep(0.005)


    def SequenceClient(self,joint_values):

        # ------------------------------------- Publish joint values

        self.msg.data = joint_values.tolist()
        self.jointPublisher.publish(self.msg)

        rospy.wait_for_service("sequence_service")

        self.client = rospy.ServiceProxy("sequence_service", sequence)
        self.service = self.client(self.sequence_active)
        self.service_result = self.service.order_recieved

def main():

    rospy.init_node("planner_node")

    freq = 10
    rate = rospy.Rate(freq)

    planner = Planner()

    request = "Rest"

    sequences = {
        "Rest"    : np.array([2048, 2816, 2048, 2048, 2816, 2048]),
        "Heart"   : np.array([2048, 1023, 1536, 2048, 1023, 1536]), # 180 90 145 180 90 145
        "Dance"   : np.array([2048, 1024, 2048, 2048, 2048, 2048]),
        "Victory" : np.array([2048, 2048, 1024, 2048, 2048, 2048]),
        "Salute"  : np.array([2048, 2048, 2048, 2048, 2048, 2048])
    }    

    while not rospy.is_shutdown():

        try:
            request = raw_input("Sequence: ")

            planner.SequenceClient(sequences[request])

            if planner.service_result == False:

                print("Sequence already active, please wait.")

            else:
                print("Sent activation for " + request + " sequence")

        except KeyError:

            print("No sequence with name " + request + ", try again.")

        rate.sleep()

if __name__ == '__main__':
    main()