# setup.py

from setuptools import setup, find_packages

setup(
    name="rk_mylib_test",  # The name of your library
    version="0.1",
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[],  # External libraries your package depends on
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple math library for addition and subtraction",
    url="https://github.com/your_username/mymathlib",  # Optional: URL to your repository
    license="MIT",
)
