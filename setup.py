from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Auto data science '
LONG_DESCRIPTION = 'Auto Data science'

# Setting up
setup(
    # the name must match the folder name
    name="auto_ds",
    version=VERSION,
    author="Kaustuv.kunal@gmail.com",
    author_email="<kaustuv.kunal@amail.com>",
    description='Auto Data Science Toolkit',
    long_description='''
A Python tool that automatically creates and optimizes machine learning pipelines .
Contact
=============
If you have any questions or comments about AUTODS, please feel free to mail us at:
kaustuv.kunal@gmail.com
This project is hosted at https://github.com/kaustuvkunal/autods
''',
    packages=find_packages(),
    install_requires=['numpy>=1.16.3',
                      'scipy>=1.3.1',
                      'scikit-learn>=0.22.0',
                      'pandas>=0.24.2',
                      'joblib>=0.13.2',
                      'xgboost>=0.90'],
    extras_require={
    },

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience ::  Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7" ],
    keywords=['pipeline optimization', 'hyperparameter optimization', 'data science', 'machine learning',  'evolutionary computation'],
    )