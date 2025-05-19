import pygame
import numpy as np
import time
from datetime import datetime

class BeanWalkerSimulation:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BEANWALKER Simulation")
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        
        # Simulation state
        self.running = True
        self.wheelchair_pos = [width//2, height//2]
        self.obstacles = self.generate_obstacles()
        self.lidar_data = []
        self.gps_data = {"lat": 0.0, "lon": 0.0}
        self.battery_level = 100
        self.status = "System Ready"
        
        # Font setup
        self.font = pygame.font.Font(None, 36)
        
    def generate_obstacles(self):
        """Generate random obstacles for simulation"""
        obstacles = []
        for _ in range(5):
            x = np.random.randint(100, self.width-100)
            y = np.random.randint(100, self.height-100)
            obstacles.append((x, y))
        return obstacles
    
    def update_lidar_data(self):
        """Simulate LiDAR readings"""
        self.lidar_data = []
        for obstacle in self.obstacles:
            dx = obstacle[0] - self.wheelchair_pos[0]
            dy = obstacle[1] - self.wheelchair_pos[1]
            distance = np.sqrt(dx*dx + dy*dy)
            angle = np.arctan2(dy, dx)
            self.lidar_data.append((distance, angle))
    
    def draw_wheelchair(self):
        """Draw the wheelchair representation"""
        pygame.draw.circle(self.screen, self.BLUE, 
                         (int(self.wheelchair_pos[0]), int(self.wheelchair_pos[1])), 20)
        
    def draw_obstacles(self):
        """Draw obstacles in the environment"""
        for obstacle in self.obstacles:
            pygame.draw.circle(self.screen, self.RED, 
                             (int(obstacle[0]), int(obstacle[1])), 10)
            
    def draw_lidar_rays(self):
        """Draw LiDAR detection rays"""
        for distance, angle in self.lidar_data:
            end_x = self.wheelchair_pos[0] + distance * np.cos(angle)
            end_y = self.wheelchair_pos[1] + distance * np.sin(angle)
            pygame.draw.line(self.screen, self.GREEN, 
                           self.wheelchair_pos, (end_x, end_y), 1)
            
    def draw_status_panel(self):
        """Draw status information panel"""
        # Battery level
        battery_text = f"Battery: {self.battery_level}%"
        battery_surface = self.font.render(battery_text, True, self.WHITE)
        self.screen.blit(battery_surface, (10, 10))
        
        # GPS coordinates
        gps_text = f"GPS: {self.gps_data['lat']:.4f}, {self.gps_data['lon']:.4f}"
        gps_surface = self.font.render(gps_text, True, self.WHITE)
        self.screen.blit(gps_surface, (10, 50))
        
        # System status
        status_surface = self.font.render(self.status, True, self.WHITE)
        self.screen.blit(status_surface, (10, 90))
        
        # Time
        time_text = datetime.now().strftime("%H:%M:%S")
        time_surface = self.font.render(time_text, True, self.WHITE)
        self.screen.blit(time_surface, (self.width - 100, 10))
        
    def run(self):
        """Main simulation loop"""
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
            # Handle movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.wheelchair_pos[0] -= 5
            if keys[pygame.K_RIGHT]:
                self.wheelchair_pos[0] += 5
            if keys[pygame.K_UP]:
                self.wheelchair_pos[1] -= 5
            if keys[pygame.K_DOWN]:
                self.wheelchair_pos[1] += 5
                
            # Update simulation
            self.update_lidar_data()
            self.battery_level = max(0, self.battery_level - 0.01)
            
            # Draw everything
            self.screen.fill(self.BLACK)
            self.draw_obstacles()
            self.draw_lidar_rays()
            self.draw_wheelchair()
            self.draw_status_panel()
            
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    simulation = BeanWalkerSimulation()
    simulation.run() 