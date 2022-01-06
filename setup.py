import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyCausalFS",
    version="0.23",
    author="Christopher Tran",
    author_email="ctran29@uic.edu",
    description="Fork of pyCausalFS - implementation of local structure learning algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris-tran-16/pyCausalFS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy',"pandas", "scipy", "scikit-learn", "networkx", "matplotlib"],
    python_requires='>=3.6',
)