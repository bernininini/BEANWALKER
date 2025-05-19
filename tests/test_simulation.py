import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.controller import BeanWalkerController
from src.simulation import BeanWalkerSimulation

def test_controller_initialization():
    controller = BeanWalkerController()
    assert controller.status == "Initializing"
    assert controller.battery_level == 100
    assert isinstance(controller.gps_data, dict)
    assert isinstance(controller.lidar_data, list)

def test_controller_component_initialization():
    controller = BeanWalkerController()
    success = controller.initialize_components()
    assert success
    assert controller.status == "System Ready"
    assert "lidar" in controller.components
    assert "gps" in controller.components
    assert "display" in controller.components

def test_controller_system_control():
    controller = BeanWalkerController()
    controller.initialize_components()
    
    # Test system start
    controller.start_system()
    assert controller.running
    
    # Test LED control
    controller.set_led_mode("blink")
    assert controller.led_status == "blink"
    
    # Test audio feedback
    controller.play_audio_feedback("warning")
    
    # Test system stop
    controller.stop_system()
    assert not controller.running
    assert controller.status == "System Stopped"

def test_simulation_initialization():
    simulation = BeanWalkerSimulation()
    assert simulation.width == 800
    assert simulation.height == 600
    assert len(simulation.obstacles) == 5
    assert simulation.battery_level == 100

def test_simulation_movement():
    simulation = BeanWalkerSimulation()
    initial_pos = simulation.wheelchair_pos.copy()
    
    # Simulate movement
    simulation.wheelchair_pos[0] += 5
    simulation.wheelchair_pos[1] += 5
    
    assert simulation.wheelchair_pos[0] == initial_pos[0] + 5
    assert simulation.wheelchair_pos[1] == initial_pos[1] + 5

if __name__ == "__main__":
    pytest.main([__file__]) 