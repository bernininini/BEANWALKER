# BEANWALKER - Modular Assistive Wheelchair System

A modular assistive wheelchair system designed for people with mobility challenges, featuring terrain-aware navigation, smart docking, and comprehensive feedback systems.

## Core Features

- Terrain-aware obstacle detection using TF-Luna lidar
- Magnetic docking with neodymium locking
- NeoPixel Light Strip for night visibility
- Bluetooth speaker for audio signals and feedback
- GPS tracking via NEO-8M
- LED strip for status indication
- Color TFT display for system information

## Hardware Components

- ESP32 (Control Hub)
- TF-Luna LiDAR
- NEO-8M GPS Module
- NeoPixel LED Strip
- TFT Display (2.8 inch)
- MPU6050 (Motion Sensor)
- Bluetooth Speaker
- Rechargeable Battery
- Neodymium Magnets

## Project Structure

```
beanwalker/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   └── sensor_manager.py
│   ├── hardware/
│   │   ├── __init__.py
│   │   ├── lidar.py
│   │   ├── gps.py
│   │   ├── display.py
│   │   └── led_controller.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Simulation

The project includes a Python-based simulation environment to test and visualize the system's functionality. Run the simulation with:

```bash
python src/simulation.py
```

## License

MIT License # BEANWALKER
