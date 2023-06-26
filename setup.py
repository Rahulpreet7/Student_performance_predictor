from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    #This function will read the requirements.txt file and return a list of requirements
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    description='End to end machine learning project',
    author="Rahulpreet",
    author_email='rahulpre@ualberta.ca',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements.txt'),
    )
