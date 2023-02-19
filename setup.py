from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readline()
    requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

    if HYPHEN_E_DOT in requriment_list:
        requriment_list.remove(HYPHEN_E_DOT)
    return requriment_list



setup(name='insurance',
      version='0.0.1',
      description='Insurance project',
      author='Arnab Manna',
      author_email='mannaarnab2001@gmail.com',
      packages=find_packages(),
      install_reqires = get_requirements()
     )