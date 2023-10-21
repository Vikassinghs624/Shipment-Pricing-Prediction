from setuptools import setup
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="shipment-price-predictor"
VERSION="0.0.1"
AUTHOR="Vikas Singh Sikarwar"
DESCRIPTION="This is first Machine Learning Project for Resume "
PACKAGES=["Shipment"]
REQUIREMENT_FILE="requirements.txt"


def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requirement mentioned in the
    requirements.txt file

    return: This function is goin going to return a list whihc contain name of libraries
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE) as requirements_file:
        return requirements_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
    )
