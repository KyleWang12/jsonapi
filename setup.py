from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='0.0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author='Yinghan Wang',
    author_email='test.test@test.com',
    description='A JSON encoder and decoder with extended functionalities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KyleWang12/jsonapi'
)