import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return dict(package=stubs)


setup(
    name="open3d-stubs",
    maintainer="open3d Developers",
    maintainer_email="example@python.org",
    description="PEP 561 type stubs for open3d",
    version="1.0",
    packages=["open3d-stubs"],
    # PEP 561 requires these
    install_requires=["open3d", "typing_extensions"],
    package_data=find_stubs("open3d-stubs"),
)
