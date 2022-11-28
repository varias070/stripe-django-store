from setuptools import setup, find_packages


setup(
    name='store',
    version='1.0',
    packages=find_packages(),
)
install_requires = [
    'asgiref==3.5.2',
    'certifi==2022.9.24',
    'charset-normalizer==2.1.1',
    'Django==4.1.3',
    'idna==3.4',
    'requests==2.28.1',
    'sqlparse==0.4.3',
    'stripe==5.0.0',
    'urllib3==1.26.12'
]
