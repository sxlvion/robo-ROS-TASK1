from setuptools import setup

package_name = 'number_pubsub'

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
    maintainer='parthip',
    maintainer_email='parthip@example.com',
    description='Publisher and subscriber example for random numbers',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'random_publisher = number_pubsub.random_number_publisher:main',
            'even_odd_subscriber = number_pubsub.even_odd_subscriber:main',
        ],
    },
)

