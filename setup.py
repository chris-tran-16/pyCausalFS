import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyCausalFS",
    version="0.1",
    author="Christopher Tran",
    author_email="ctran29@uic.edu",
    description="Fork of pyCausalFS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris-tran-16/pyCausalFS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy'],
    python_requires='>=3.6',
)