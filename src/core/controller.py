from datetime import datetime
import threading
import time

class BeanWalkerController:
    def __init__(self):
        self.components = {}
        self.running = False
        self.status = "Initializing"
        self.battery_level = 100
        self.gps_data = {"lat": 0.0, "lon": 0.0}
        self.lidar_data = []
        self.mpu_data = {"accel": [0, 0, 0], "gyro": [0, 0, 0]}
        self.led_status = "off"
        self.display_content = {}
        
    def initialize_components(self):
        """Initialize all hardware components"""
        try:
            # Initialize components (simulated)
            self.components = {
                "lidar": {"status": "ready", "data": []},
                "gps": {"status": "ready", "data": {"lat": 0.0, "lon": 0.0}},
                "display": {"status": "ready", "content": {}},
                "leds": {"status": "ready", "mode": "off"},
                "speaker": {"status": "ready", "volume": 50},
                "mpu": {"status": "ready", "data": {"accel": [0, 0, 0], "gyro": [0, 0, 0]}}
            }
            self.status = "System Ready"
            return True
        except Exception as e:
            self.status = f"Initialization Error: {str(e)}"
            return False
            
    def start_system(self):
        """Start all system components and monitoring"""
        if not self.running:
            self.running = True
            # Start monitoring threads
            self.monitor_thread = threading.Thread(target=self._monitor_system)
            self.monitor_thread.daemon = True
            self.monitor_thread.start()
            
            # Start component update threads
            self.update_thread = threading.Thread(target=self._update_components)
            self.update_thread.daemon = True
            self.update_thread.start()
            
    def stop_system(self):
        """Stop all system components"""
        self.running = False
        self.status = "System Stopped"
        
    def _monitor_system(self):
        """Monitor system health and status"""
        while self.running:
            # Check battery level
            self.battery_level = max(0, self.battery_level - 0.01)
            
            # Check component status
            for component, data in self.components.items():
                if data["status"] != "ready":
                    self.status = f"Warning: {component} not ready"
                    
            time.sleep(1)
            
    def _update_components(self):
        """Update component data"""
        while self.running:
            # Update GPS data (simulated)
            self.gps_data["lat"] += 0.0001
            self.gps_data["lon"] += 0.0001
            
            # Update LiDAR data (simulated)
            self.lidar_data = [(100, 0), (150, 45), (200, 90)]
            
            # Update MPU data (simulated)
            self.mpu_data["accel"] = [0.1, 0.2, 9.8]
            self.mpu_data["gyro"] = [0.1, 0.2, 0.3]
            
            # Update display content
            self.display_content = {
                "time": datetime.now().strftime("%H:%M:%S"),
                "battery": f"{self.battery_level:.1f}%",
                "gps": f"Lat: {self.gps_data['lat']:.4f}, Lon: {self.gps_data['lon']:.4f}",
                "status": self.status
            }
            
            time.sleep(0.1)
            
    def set_led_mode(self, mode):
        """Set LED strip mode"""
        if mode in ["off", "on", "blink", "pulse"]:
            self.led_status = mode
            self.components["leds"]["mode"] = mode
            
    def play_audio_feedback(self, tone_type):
        """Play audio feedback"""
        if tone_type in ["warning", "success", "error"]:
            # Simulate audio feedback
            print(f"Playing {tone_type} tone")
            
    def get_system_status(self):
        """Get current system status"""
        return {
            "status": self.status,
            "battery": self.battery_level,
            "gps": self.gps_data,
            "lidar": self.lidar_data,
            "mpu": self.mpu_data,
            "led_mode": self.led_status,
            "display": self.display_content
        } 