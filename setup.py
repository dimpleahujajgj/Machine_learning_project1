from setuptools import setup
from typing import List



#Declaring variables for setup function
PROJECT_NAME="House-Predictor"
VERSION="0.0.1"
AUTHOR="Dimple Ahuja"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of packages which 
    are supposed to be installed
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    DESCRIPTION="This is my first Machine Learning Project",
    packages=["housing"],
    install_requires=get_requirements_list()
)

