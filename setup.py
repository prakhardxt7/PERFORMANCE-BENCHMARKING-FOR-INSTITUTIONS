from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # This function will return a list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip whitespace/newlines and filter out '-e .'
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != '-e .']
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Prakhar',
    author_email='prakhardixit2k17@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
