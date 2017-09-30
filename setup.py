from setuptools import setup, find_packages

import os
os.system("wget http://download.java.net/java/jdk8u152/archive/b05/binaries/jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz .")
os.system("tar -xvf jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")
os.system("export JAVA_HOME=~/jre1.8.0_152")
os.system("export PATH=\"$JAVA_HOME/bin:$PATH\"")
os.system("java -jar ditaa.jar ditaa_test.txt")

setup (
    name             = "testapp",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn", "libsass >= 0.13", "Mako", "pypugjs"],
)
