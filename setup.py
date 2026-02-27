from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fragpipe-speclib',
    version='0.1.58',
    description='FragPipe-SpecLib: Simple library generation for FragPipe',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Nesvilab/FragPipe-SpecLib",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=['numba==0.62.1','Click==8.3.1','numpy==1.26.4','scipy==1.16.3','scikit-learn==1.7.2','statsmodels==0.14.6','pandas==2.3.3','biopython==1.86','pyopenms==3.3.0','matplotlib==3.10.7','seaborn==0.13.2', 'tqdm==4.67.1'],
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    package_data={  # Optional
        'easypqp': ['data/unimod.xml'],
    },
    entry_points={
        'console_scripts': [
            'fragpipe-speclib=easypqp.main:cli',
        ],
    },
    extras_require={
        'PyProphet': ['pyprophet'],
    },
)
