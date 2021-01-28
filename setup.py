import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="src",
    version="0.0.1",
    author="deacona",
    # author_email="",
    description="Football + Data science",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/findmypast/the-ball-is-round",
    packages=setuptools.find_packages(),
    package_data={
        "src": [
            "config.ini",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.6",
)
