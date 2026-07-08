import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SecureLogNode(Node):
    """
    Bu node, güvenlik loglarını simüle eden ve 'security_status' başlığına (topic)
    periyodik olarak mesaj yayınlayan geçici (dummy) bir ROS2 node'udur.
    """
    def __init__(self):
        # Node ismi 'secure_log_node' olarak başlatılır
        super().__init__('secure_log_node')
        
        # 'security_status' konusu üzerinden String tipinde mesaj yayınlayan publisher oluşturulur
        self.publisher_ = self.create_publisher(String, 'security_status', 10)
        
        # Her 2.0 saniyede bir 'timer_callback' fonksiyonunu tetikleyen zamanlayıcı
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        # Yayınlanacak mesaj hazırlanır
        msg = String()
        msg.data = 'secure_log_node aktif: Haberlesme testi basarili.'
        
        # Mesaj ilgili konuma (topic) gönderilir
        self.publisher_.publish(msg)
        
        # Terminale bilgi çıktısı basılır
        self.get_logger().info(f'Yayinlandi: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SecureLogNode()
    rclpy.spin(node) # Node sonlandırılana kadar çalışmaya devam eder
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()