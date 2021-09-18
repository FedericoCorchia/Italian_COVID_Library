from setuptools import find_packages, setup
import os

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='itacovidlib',
    packages=find_packages(),
    version='0.1.0'
    description='Python library for COVID-19 data analysis referred to Italy',
    author='Federico Corchia'
    license='',
    keywords='COVID-19 cases vaccines Italy'
    url='https://github.com/FedericoCorchia/Italian_COVID_Library'
    long_description=read('README.md')
    install_requires=['pandas', 'requests'],
)
