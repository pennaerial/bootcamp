import rospy
from std_msgs.msg import String

def publisher():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('publisher_name')
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
	   pub.publish(raw_input())
	   r.sleep()

if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass