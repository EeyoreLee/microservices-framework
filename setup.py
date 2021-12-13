import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()


# 允许setup.py在任何路径下执行
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name="msf",
    version="0.1.3",
    author="EeyoreLee",
    author_email="li.chunyu0412@outlook.com",
    description="python easy microservices framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EeyoreLee/microservices-framework",
    packages=setuptools.find_packages(include=['msf', 'msf.*']),
    install_requires=['flask>=2.0.2'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.6',
    package_data={
        'msf': ['*']
    }
)