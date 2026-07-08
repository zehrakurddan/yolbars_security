from setuptools import find_packages, setup

package_name = 'yolbars_security'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zehra',
    maintainer_email='zehra@todo.todo',
    description='Yolbars security ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'secure_log_node = yolbars_security.secure_log_node:main',
            'security_monitor_node = yolbars_security.security_monitor_node:main',
        ],
    },
)