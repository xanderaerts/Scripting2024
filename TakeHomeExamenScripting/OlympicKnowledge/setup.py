from setuptools import setup, find_packages

setup(name='OlympicKnowledge',
      version='1.5',
      description='Package to get all info about water polo on the olympics',
      author='Xander Aerts',
      license='MIT',
      packages=find_packages(include=['OlympicKnowledge']),
      install_requires=[
          'beautifulsoup4',
        'CairoSVG',
        'cssselect2',
        'requests',
        'reportlab'
      ]
      )