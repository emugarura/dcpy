from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    description = f.read()

setup(
      name='dcpy',
      packages=find_packages(),
      version='0.1',
      description=description,
      author='Washim Ahmed',
      url='https://github.com/washim/dcpy',
      download_url='https://github.com/washim/dcpy/releases/tag/v.0.1',
      keywords=['visualization', 'd3', 'crossfilter', 'dc'],
      install_requires=['ipython'],
      python_requires='>=3',
      classifiers=['Development Status :: 3 - Alpha','Intended Audience :: Developers','License :: OSI Approved :: MIT License','Programming Language :: Python :: 3.6']
)