from setuptools import find_packages, setup
from typing import List

# Global variable for '-e .' requirement
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    ''' 
    This function reads requirements from a file and returns a list of requirements.
    It removes newline characters and '-e .' requirement if present.
    '''
    requirements = []

    # Read requirements from file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' requirement if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Setup function to define package metadata and dependencies
setup(
    name='mlproject',
    version='0.0.1',
    author='Basit',
    author_email='basitshabir2022@gmail.com',
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=get_requirements('requirements.txt')  # Specify requirements from file
)
