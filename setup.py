''''setup.py will be responsible in creating my machine learning as a package and that can be you can also install this package in your projects. and even deploy in py right from there anybody can do the installation and anybody can also use it '''

from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name ='Machine Learing Project',
version='0.0.1',
author='Jay',
author_email='jayakrishnagolla15@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)