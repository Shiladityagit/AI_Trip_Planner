from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found.")
        

    return requirement_list

setup(
    name="AI-TRIP-PLANNER",
    version="0.0.1",
    author="shiladitya mondal",
    author_email="shiladityam178@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)