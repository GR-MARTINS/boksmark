from setuptools import setup, find_packages
"""
para instalar, execute o comando 'pip install -e .'
"""

def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="app_name",
    version="0.1.0",
    description="app_description",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
