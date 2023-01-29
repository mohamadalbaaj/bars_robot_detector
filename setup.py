import os
import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'drobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'meshes'),  glob.glob('meshes/*.dae')),
        (os.path.join('share', package_name, 'meshes'),  glob.glob('meshes/*.stl')),
        (os.path.join('share', package_name, 'urdf'),   glob.glob('urdf/bars_detector_robot.urdf')),
        (os.path.join('share', package_name, 'launch'), glob.glob('launch/drobot_launch.py')),
        (os.path.join('share', package_name, 'rviz'),   glob.glob('rviz/config.rviz'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mohamad',
    maintainer_email='mohamad@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['joystick = drobot.joystick:main',
                            'wall = drobot.wall:main',
                            'distance_calculator = drobot.distance_calculator:main',
                            'bar = drobot.bar:main',

        ],
    },
)