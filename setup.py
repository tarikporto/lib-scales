from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Project used to generate musical scales while enhancing my own familiarity with python :)'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="scalechords", 
        version=VERSION,
        author="Tarik Porto",
        author_email="tariklemos1511@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python','music','scale','chord'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)
