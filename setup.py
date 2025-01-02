from setuptools import setup, find_packages

setup(
    name="PachaMalayalam",
    version="0.1.0",
    description="A Malayalam programming language transpiler that converts .pymal files into Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PachaMalayalam",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pachalang=pachamalayalam.transpiler:main",
        ],
    },
)
