from setuptools import setup
import os

setup(
    name = "airsim_gym",
    version = "0.1",
    author = "Konstantinos Kamaropoulos",
    author_email = "k@kamaropoulos.com",
    description = ("An OpenAI Gym environment for Microsoft's AirSim Multirotor simulator"),
    license = "MIT",
    keywords = "AirSim, OpenAI Gym, Gym, reinforcement learning, multirotor",
    url = "http://packages.python.org/an_example_pypi_project",
    install_requires=['gym', 'opencv-python', 'eventlet', 'airsim', 'matplotlib', 'Pillow'],
)
