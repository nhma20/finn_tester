import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
import os


class FinnTesterNode(Node):

	def __init__(self):
		super().__init__('finn_tester_node')
		self.publisher_ = self.create_publisher(Image, '/test_image', 10)
		timer_period = 5  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.bridge = CvBridge()
		self.i = 0
		self.path = "/home/mp4d/test_images"
		self.filenames = os.listdir(self.path)

	def timer_callback(self):
		filename = self.filenames[self.i]
		# img = cv2.imread(os.path.join(self.path,filename),1)
		img = cv2.imread(os.path.join(self.path,"0000002989380.jpg"),1)
		#img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)
		msg = self.bridge.cv2_to_imgmsg(np.array(img), "bgr8")
		msg.header.frame_id = "camera"
		self.publisher_.publish(msg)
		self.i = (self.i + 1) % len(self.filenames)

def main(args=None):
	rclpy.init(args=args)

	minimal_publisher = FinnTesterNode()

	rclpy.spin(minimal_publisher)

	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	minimal_publisher.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
