try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Toy Robot Simulator',
    'author': 'Jui Chandwaskar',
    'author_email': 'jui.136@gmail.com',
    'version': '1.0',
    'packages': ['toy_robot'],
    'install_requires': [],
    'scripts': [],
    'name': 'toy_robot',
    'entry_points': {
        'console_scripts': [
            'toy_robot = toy_robot.simulator:start_simulation',
        ],
    },
}

setup(**config)
