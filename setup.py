from setuptools import setup
import os


def read(fname):
    """Auxiliary function to read file from current folder."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='ratipl',
      version='1.0 dev',
      description=(
              'Radiation on Tilted Plane (RaTiPl). Calculate the solar '
              'radiation on a tilted plane.'),
      url='tofollow',
      author='Markus Brandt, Francesco Witte',
      author_email='tofollow',
      long_description=read('README.rst'),
      license='GPL-3.0',
      packages=['ratipl'],
      python_requires='>=3',
      install_requires=['numpy >= 1.14.3',
                        'pandas >= 0.24.0'])
