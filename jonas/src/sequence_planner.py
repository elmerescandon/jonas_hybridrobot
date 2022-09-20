#!/usr/bin/env python

# --- Import libraries

import rospy

import numpy as np
import time
import actionlib

from std_msgs.msg import Int16MultiArray, Bool

from jonas.srv import sequence, sequenceResponse


# ----------- Classes

class Planner(object):

    # ------------------- General Variables

    sequence_active = True

    motors_moving = False

    msg = Int16MultiArray()


    def __init__(self):

        # ------------------------------------- Create publisher

        self.jointPublisher = rospy.Publisher("joint_value",Int16MultiArray, queue_size=10)
        
        rospy.sleep(0.005)

        # ------------------------------------- Create subscriber

        self.motorSubscriber = rospy.Subscriber("motors_status",Bool, self.UpdateStatus)
        
        rospy.sleep(0.005)


    def UpdateStatus(self,msg):

        # -------------------------- Recieves a motor status from topic.

        self.motors_moving =  msg.data


    def SequenceClient(self,joint_values):

        # ------------------------------------- Publish joint values

        self.msg.data = joint_values.tolist()
        self.jointPublisher.publish(self.msg)

        rospy.wait_for_service("sequence_service")

        self.client = rospy.ServiceProxy("sequence_service", sequence)
        self.service = self.client(self.sequence_active)


def main():

    rospy.init_node("planner_node")

    freq = 10
    rate = rospy.Rate(freq)

    planner = Planner()

    request = "Rest"

    # -------------------------- Diferent positions for robot.

    poses = {
        "Rest"       : np.array([180, 90, 180, 180, 90, 180]),
        "Heart"      : np.array([0, 90, 135, 360, 90, 135]), 
        "Serve"      : np.array([90, 90, 180, 270, 90, 180]),
        "Victory"    : np.array([0, 135, 180, 360, 135, 180]),
        "Salute"     : np.array([45, 90, 135, 180, 90, 180]),

        "Walking 1"  : np.array([135, 90, 180, 135, 90, 180]),
        "Walking 2"  : np.array([225, 90, 180, 225, 90, 180]),

        "Dance 1"    : np.array([0, 135, 225, 180, 135, 225]),
        "Dance 2"    : np.array([180, 135, 225, 360, 135, 225]),

        "Hug 1"      : np.array([90, 135, 180, 270, 135, 180]),
        "Hug 2"      : np.array([90, 90, 135, 270, 90, 135]),

        "Curl 1"      : np.array([0, 180, 135, 360, 180, 135]),
        "Curl 2"      : np.array([0, 90, 135, 360, 90, 135]),

    }

    sequences = {
        "Walking" : np.array(["Rest","Walking 1", "Walking 2", "Walking 1", "Walking 2", "Walking 1", "Walking 2", "Rest"]),
        "Dance"   : np.array(["Rest","Dance 1", "Dance 2", "Dance 1", "Dance 2", "Dance 1", "Dance 2", "Rest"]),
        "Hug"     : np.array(["Rest","Hug 1", "Hug 2", "Hug 1", "Hug 2", "Hug 1", "Hug 2", "Rest"]),
        "Curl"     : np.array(["Rest","Curl 1", "Curl 2", "Curl 1", "Curl 2", "Curl 1", "Curl 2", "Rest"])
    }



    while not rospy.is_shutdown():

        if planner.motors_moving == False:

                request = raw_input("Sequence: ")

                try: 
                    order = sequences[request]
                    print("Sent activation for " + request + " sequence.")

                    for i in order:

                        while planner.motors_moving == True:
                            pass

                        planner.SequenceClient(poses[i]/0.088)
                        
                        rospy.sleep(0.5)

                except KeyError:

                    try:
                        planner.SequenceClient(poses[request]/0.088)
                        print("Sent activation for " + request + " pose.")
                        rospy.sleep(0.5)

                    except KeyError:
                        print("Neither pose nor sequence exists with name " + request + ", try again.")


                
                


        rate.sleep()

if __name__ == '__main__':
    main()