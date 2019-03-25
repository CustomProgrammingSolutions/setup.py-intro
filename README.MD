# Hello world - setup.py version

This repository is a very simple example of Python's packaging capabilities.

Have a look through the code included to see what is involved when a very simple package is installed.

## How this works

There's a folder called "hello_world" that contains the package we are installing with our `setup.py` file.

Here's what the setup.py file looks like:

```python
from setuptools import setup

setup(
      name='hello_world',
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
```

The most relevant things here are the following:

### Name

```python
      name='hello_world',
```

This is the name of the package being installed.

### Version

```python
      version='0.0.1',
```

This specifies the version of the library that is being installed. This version number is used by various pacakaging automation tools so using something like semantic versioning is a good idea in this case.

### packages

The directory our package's files reside in is specified in the `setup` function here:

```python
      packages=['hello_world'],
```

This is needed so that the setup function can find the path to the code that we are installing.

## How this is used

Once you have specified `setup.py` and put all the files at the right locations you can then install this library with pip with:

```sh
pip install .
```
