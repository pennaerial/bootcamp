import rospy
from std_msgs.msg import String

def main():
    pub=rospy.Publisher('tutorialTopic', String, queue_size=10)
    rospy.init_node('publisherNode')
    r=rospy.Rate(10)
    while not rospy.is_shutdown():
        text=raw_input("input text:")
        pub.publish(text)
        r.sleep()

if __name__ == '__main__':
    main()
