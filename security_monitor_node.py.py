import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SecurityMonitorNode(Node):
    """
    Bu node, 'security_status' başlığını (topic) dinleyen ve gelen güvenlik
    loglarını terminale basan geçici (dummy) bir ROS2 izleme node'udur.
    """
    def __init__(self):
        # Node ismi 'security_monitor_node' olarak başlatılır
        super().__init__('security_monitor_node')
        
        # 'security_status' konusunu dinleyen subscriber oluşturulur
        # Yayınlanan her yeni mesaj 'listener_callback' fonksiyonuna yönlendirilir
        self.subscription = self.create_subscription(
            String,
            'security_status',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # Yayıncıdan gelen veri yakalandığında terminale basılır
        self.get_logger().info(f'Alindi: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SecurityMonitorNode()
    rclpy.spin(node) # Node sonlandırılana kadar çalışmaya devam eder
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()