from setuptools import setup
import os 

package_name = 'finn_tester'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/finn_tester.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nm',
    maintainer_email='nhma@mmmi.sdu.dk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'finn_tester = finn_tester.finn_tester_node:main',
        	'finn_tester_sub = finn_tester.finn_tester_node_sub:main',
        ],
    },
)
