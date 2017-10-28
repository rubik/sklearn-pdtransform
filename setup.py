import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fobj:
    readme = fobj.read()

setup(name='pdtransform',
      version='0.2',
      author='Michele Lacchia',
      author_email='michelelacchia@gmail.com',
      url='http://signal-to-noise.xyz/why-you-should-use-scikit-learns-pipeline-object.html',
      license='MIT',
      description='Sklearn transformers that work with Pandas dataframes',
      platforms='any',
      long_description=readme,
      packages=find_packages(),
      install_requires=['scikit-learn', 'pandas'],
      keywords='sklearn pandas transformers pipeline',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ]
)
