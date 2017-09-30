from setuptools import setup, find_packages

import os
os.system("yum install java-1.8.0-openjdk")
os.system("java -jar ditaa.jar ditaa_test.txt")

setup (
    name             = "testapp",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn", "libsass >= 0.13"],
)
