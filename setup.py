# Modules
import os
import site
import codecs
import pathlib
from glob import glob
from setuptools import setup

# Grab our current path
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding = "utf-8")

# Package finder
def find_packages(dir):
    packs = []
    for p, _, __ in os.walk(dir):
        path = p.replace("\\", "/").replace("/", ".").replace(dir + ".", "")
        if "egg-info" not in path and "__pycache__" not in path:
            if path != dir:
                packs.append(path)

    return packs

# Handle versions (https://github.com/pypa/pip/blob/main/setup.py#L11)
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = "\"" if "\"" in line else "'"
            return line.split(delim)[1]

    else:
        raise RuntimeError("Unable to find version string.")

# Handle setup
setup(
    name = "nitrogenfw",
    version = get_version("src/nitrogen/__init__.py"),
    description = "A framework to build desktop apps with web technologies",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "iiPython",
    author_email = "ben@iipython.cf",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    license = "MIT",
    url = "https://github.com/ii-Python/nitrogen",
    python_requires = ">=3.8, <4",
    install_requires = open("reqs.txt", "r").read().splitlines(),
    package_dir = {"": "src"},
    packages = find_packages("src"),
    data_files = [
        (os.path.join(site.USER_SITE[len(os.path.abspath(os.path.join(site.USER_SITE, "../" * 3))):].strip("/\\"), "nitrogen/js"), glob("src/nitrogen/js/*"))
    ]
)
