import os
from setuptools import setup, find_packages

__version__ = version = VERSION = '0.1'

directory = os.path.abspath(os.path.dirname(__file__))

package_data_dict = {}

#package_data_dict[''] = [
#    os.path.join('defaults', 'dswx_hls.yaml'),
#    os.path.join('schemas', 'dswx_hls.yaml')]

setup(
    # basic info
    name='s1_burst_id',
    version=version,
    description='Assign a unique burst id to Sentinel-1 bursts',
    long_description='A prototype for labeling Sentinel-1 bursts',
    url='https://github.com/opera-adt/sentinel1-burst-id',

    classifiers=['Programming Language :: Python', ],
    license='Copyright by the California Institute of Technology. ALL RIGHTS RESERVED.',

    # package discovery
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=['bin/create_burst_id.py'],

    package_data=package_data_dict,
)
