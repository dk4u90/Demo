from gettext import install
from typing import List
from setuptools import find_packages,setup

def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    """
    Assigment write code to read requirements.txt and append each requirements in requirements_list variable.
    """
    return requirements_list
setup(

    name="sensor",
    verson="0.0.1",
    author_email='dk4u90@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)