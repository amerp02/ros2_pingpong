from setuptools import setup

package_name = 'py_pingpong'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pehlica2',
    maintainer_email='pehlica2@vcu.edu',
    description='Ping Pong program using minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pingpong.publisher_member_function:main',
            'listener = py_pingpong.subscriber_member_function:main',
            'talker2 = py_pingpong.pong_function:main',
            'listener2 = py_pingpong.ping_function:main',
        ],
    },
)
