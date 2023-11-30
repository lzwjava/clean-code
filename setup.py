from setuptools import setup, find_packages

setup(
    name='cleancode',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cleancode = cleancode.cleancode:main'
        ],
    }
)
