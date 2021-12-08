from setuptools import setup, find_packages


def import_requirements(filename) -> list:
    with open(filename, 'r') as file:
        requirements = file.read().split("\n")
    return requirements


setup(
    name='dagsim',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/uio-bmi/dagsim',
    license='AGPL-3.0 License',
    author='Ghadi Al Hajj',
    author_email='ghadia@uio.no.com',
    description='A framework and specification language for simulating data based on user-defined graphical models',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["graphviz>=0.16",
                      "numpy>=1.20.2",
                      "pandas>=1.2.4",
                      "python-igraph>=0.9.6",
                      "scikit-learn>=0.24.2",
                      "ipython>=7.27.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
