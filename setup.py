from setuptools import setup
from glob import glob
import os

package_name = 'laser_cartographer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/**')),
        (os.path.join('share', package_name, 'launch'), glob('launch/**')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Y250HT',
    maintainer_email='1501483814@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "laser_x2=laser_driver.laser_x2:main"
        ],
    },
)
