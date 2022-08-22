from setuptools import find_packages, setup
from reorder import __version__

setup(
    name='reorder',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='Demo repository implementing an end-to-end MLOps workflow on Databricks. Project derived from dbx '
                'basic python template',
    authors='Joseph Bradley, Rafi Kurlansik, Matthew Thomson, Niall Turbitt'
)
