from setuptools import setup, find_packages

setup(
    name='snapshot',
    version='1.0',
    author="Yauheni Matveichyk",
    author_email="yauheni_matveichyk@epam.com",
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    include_package_data=True
)
