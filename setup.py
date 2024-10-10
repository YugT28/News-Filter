from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            line=file.readlines()
            for line in line:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError as f:
        print("requirements.txt file not found",f)
    return requirement_list

#print(get_requirements())

setup(
    name='news',
    version='0.0.1',
    author='Yugndhar',
    author_email='thakareyugandhar108@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)