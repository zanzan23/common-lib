from setuptools import setup, find_packages

setup(
    name='portmon.common-lib',
    version='1.0',
    #packages=find_packages(where='src', exclude=("main",)),    
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[ 
        'SQLAlchemy==2.0.23',
    ],
)