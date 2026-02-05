import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Cachy",
    version="1.1",
    author="Akari-Codes",
    author_email="akari+cachy@astil-industries.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akari-Codes/Cachy-Python-Module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
from distutils.core import setup
setup(
  name = 'Cachy',         # How you named your package folder (MyLib)
  packages = ['Cachy'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '',   # Give a short description about your library
  author = 'Akari',                   # Type in your name
  author_email = 'akari@astil-industries.com',      # Type in your E-Mail
  url = 'https://github.com/Akari-Codes/Cachy-Python-Module/',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['Cache', 'Efficent', 'Useful'],   # Keywords that define your package best
  install_requires=['pathlib', 'joblib'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
