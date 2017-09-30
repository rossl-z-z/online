from setuptools import setup, find_packages
from pathlib import Path
import os

print(os.environ['BUILD'])
if os.environ['BUILD']['kind'] == 'Build':
    print("DERPPP")

jre_dir = Path("/opt/app-root/src/jre1.8.0_152")
if jre_dir.is_dir():
  os.system("export JAVA_HOME=~/jre1.8.0_152; export PATH=\"$JAVA_HOME/bin:$PATH\"; java -jar ditaa.jar ditaa_test.txt")
else:
  os.system("wget http://download.java.net/java/jdk8u152/archive/b05/binaries/jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")
  os.system("tar -xvf jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")
  os.system("rm jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")

setup (
    name             = "testapp",
    version          = "0.1",
    description      = "Example application to be deployed.",
    packages         = find_packages(),
    install_requires = ["gunicorn", "libsass >= 0.13", "Mako", "pypugjs"],
)
