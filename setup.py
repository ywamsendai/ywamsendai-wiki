import json
from setuptools import setup, find_packages

# Load package.json contents
with open("package.json") as f:
    package = json.load(f)

# Load list of dependencies
with open("requirements.txt") as f:
    install_requires = [
        line for line in f.read().split("\n")
        if line and not line.startswith("#")
    ]

# Load README contents
with open("README.md", encoding = "utf-8") as f:
    long_description = f.read()

# Package description
setup(
    name = "mkdocs-material",
    version = package["version"],
    url = package["homepage"],
    project_urls = {
        "Source": "https://github.com/squidfunk/mkdocs-material",
    },
    license = package["license"],
    description = package["description"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = package["author"]["name"],
    author_email = package["author"]["email"],
    keywords = package["keywords"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    packages = find_packages(exclude = ["src", "src.*"]),
    include_package_data = True,
    install_requires = install_requires,
    python_requires='>=3.7',
    entry_points = {
        "mkdocs.themes": [
            "material = material"
        ],
        "mkdocs.plugins": [
            "search = material.plugins.search.plugin:SearchPlugin",
            "tags = material.plugins.tags.plugin:TagsPlugin"
        ]
    },
    zip_safe = False
)
