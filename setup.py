import os

from distutils.core import setup

from setuptools import find_packages


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('minecraft_data/data/data')

setup(
    name='minecraft-data-latest',
    description='Provide easy access to minecraft data in python',
    license='MIT',
    long_description=open('README.rst').read(),
    version='0.1.1',
    maintainer='Rodrigo Silva (MestreLion)',
    maintainer_email='minecraft@rodrigosilva.com',
    url='https://github.com/MestreLion/python-minecraft-data-latest',
    packages=find_packages(),
    package_data={'minecraft_data': extra_files},
    install_requires=[],
    keywords=['minecraft'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
