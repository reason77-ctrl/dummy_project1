from setuptools import setup

setup(
    include_package_data= True,
    name = "package_reason_scraping",
    version= "2.8.0",
    description= "Package_reason calculator module",
    url = '',
    author= 'Reason',
    author_email= 'reasonregmi25@hotmail.com',
    packages= ['package_reason','package_file_handle', 'package_web_scraping'],
    install_requires = [],
    long_description= 'This is a dummy project for setup.py and modules of python',
    long_description_content_type= 'text/markdown',
)