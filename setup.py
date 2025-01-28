from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from the requirements.txt file.
    It also removes the '-e .' entry if it exists.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        
        # Remove '-e .' if present
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name='ml_project',
    version='0.0.2',
    author='Prakhar',
    author_email='prakhardixit2k17@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
