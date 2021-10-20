from setuptools import find_packages, setup
import os

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='itacovidlib',
    packages=find_packages(),
    version='0.1.0'
    description='Python library for COVID-19 infections and vaccinations in Italy data retrieval and analysis',
    author='Federico Corchia'
    license='',
    keywords='COVID-19 infection vaccination Italy'
    url='https://github.com/FedericoCorchia/Italian_COVID_Library'
    long_description=read('README.md')
    install_requires=['numpy', 'pandas', 'geopandas', 'requests', 'epyestim'],
    tests_require=['hypothesis'],
)
