from setuptools import setup

setup(name='hello_world',
      version='0.0.1',
      description='Shows how to use setup.py',
      url='https://www.customprogrammingsolutions.com',
      author='Janis Lesinskis',
      license='GPLv3',
      packages=['hello_world'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='tutorial',
      include_package_data = True,
)
