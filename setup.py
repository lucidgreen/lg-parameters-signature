import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lg_parameters_signature",
    version="0.0.1",
    author="foundertherapy",
    author_email="support@foundertherapy.co",
    description="Provides unified methodology to evaluate and validate auth key from a set of parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucidgreen/lg-parameters-signature",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
