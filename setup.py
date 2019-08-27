from setuptools import setup
import os

setup(
    name = "airsim_gym",
    version = "0.1",
    packages = ['airsim_gym'],
    author = "Konstantinos Kamaropoulos",
    author_email = "k@kamaropoulos.com",
    description = ("An OpenAI Gym environment for Microsoft's AirSim Multirotor simulator"),
    license = "MIT",
    keywords = "AirSim, OpenAI Gym, Gym, reinforcement learning, multirotor",
    url = "https://github.com/Kamaropoulos/AirSim_Gym",
    download_url = 'https://github.com/Kamaropoulos/AirSim_Gym/archive/0.1.tar.gz',
    install_requires=['gym', 'opencv-python', 'eventlet', 'airsim', 'matplotlib', 'Pillow']
)
