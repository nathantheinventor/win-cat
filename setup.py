import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="win-cat",
    version="0.2.0",
    author="Nathan Collins",
    author_email="nathantheinventor@gmail.com",
    description="An implementation of cat for Windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathantheinventor/win-cat",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'cat=win_cat.cat:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
