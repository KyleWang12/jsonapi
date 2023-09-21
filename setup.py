from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'json'
    ],
    author='Yinghan Wang',
    author_email='test.test@test.com',
    description='A JSON encoder and decoder with extended functionalities.',
    readme=open('README.md').read(),
    url='https://github.com/KyleWang12/jsonapi'
)