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
  download_url = 'https://github.com/Akari-Codes/Cachy-Python-Module/archive/refs/tags/V1.1.tar.gz',    # I explain this later on
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
