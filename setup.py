
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='airfoilshapeopt',
    version='0.0.1',
    author='Rahul Dixit, Pranati Bhatnagar, Ritik Kumar',
    author_email= (
        'dev.rahuldixit@gmail.com, '
        'pranatib1234@gmail.com, '
        'contactritik09@gmail.com'
    ),
    url='https://github.com/Neomech/aerodynamic-shape-optimization',
    description='A Python library for 2D airfoil analysis and shape optimization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
