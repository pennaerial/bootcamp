import rospy
from std_msgs.msg import String

def main():
    def callback(data):
        rospy.loginfo("data: %s", data.data)
    rospy.init_node('listenerNode')
    rospy.Subscriber("tutorialTopic", String, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
