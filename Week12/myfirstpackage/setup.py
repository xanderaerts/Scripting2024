from setuptools import setup, find_packages

setup(name="XanderPackage",
      version="1.0",
      description="nice first package",
      author="Xander",
      license="MIT",
      packages=find_packages(include=['mypackage']),
      )