import setuptools
from setuptools import find_packages


setuptools.setup(name='<%= appName %>',
                 version='0.0.1',
                 description='<%= description %>',
                 author='<%= author %>',
                 author_email='<%= email %>',
                 packages=find_packages(),
                 install_requires=[],
                 zip_safe=False,
                 keywords='<%= keywords %>')