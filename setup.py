import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_content = fh.read()

setuptools.setup(
    name="dipamkara",
    version='0.3.9',
    author="vortezwohl",
    author_email="vortez.wohl@gmail.com",
    description="A light-weight vector database engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license_content,
    url="https://github.com/vortezwohl/Dipamkara",
    project_urls={
        "Bug Tracker": "https://github.com/vortezwohl/Dipamkara/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
    install_requires=[
        'numpy'
    ],
    entry_points={},
    include_package_data=False
)
