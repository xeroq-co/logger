# filepath: hannibal-logger/setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hannibal-logger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytz",
    ],
    python_requires=">=3.7",
    description="Custom Python logger with color and EST timestamps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hannibal",
    license="MIT",
)