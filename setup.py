from setuptools import setup

setup(
   name='trade-scanner',
   version='1.0',
   description='A useful module',
   author='Steven Tang',
   author_email='you dont want to know',
   packages=['trade-scanner'],
   install_requires=['requests',
                     'ipython',
                     'schedule']
)