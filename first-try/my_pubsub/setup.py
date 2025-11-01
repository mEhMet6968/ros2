from setuptools import setup

package_name = 'my_pubsub'

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
    maintainer='gauss',
    maintainer_email='you@example.com',
    description='Simple ROS 2 Python pub/sub example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_pubsub.talker:main',
            'listener = my_pubsub.listener:main',
        ],
    },
)

