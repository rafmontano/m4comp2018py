from setuptools import setup, find_packages

setup(
    name='m4comp2018py',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests',
        'pyreadr',
        'h5py',
        'numpy',
        'rpy2>=3.5.1',  # Required for R integration
    ],
    author='Your Name',
    description='Python loader and interface for the M4comp2018 R dataset',
    include_package_data=True,
)