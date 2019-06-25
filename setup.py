from setuptools import setup, find_packages

from jobpy import __version__ as version

description = 'Automated tool for scraping job postings.'
url = 'https://github.com/PaulMcInnis/JobPy'
requires = ['beautifulsoup4>=4.6.3',
            'lxml>=4.2.4',
            'requests>=2.19.1',
            'python-dateutil>=2.8.0']

with open('readme.md', 'r') as f:
    readme = f.read()

setup(
    name             = 'JobPy',
    version          = version,
    description      = description,
    long_description = readme,
    author           = 'Paul McInnis, Bradley Kohler, Jose Alarcon',
    author_email     = 'paulmcinnis99@gmail.com',
    url              = url,
    license          = 'MIT License',
    python_requires  = '>=3.6.0',
    install_requires = requires,
    packages         = find_packages(exclude=('test',)),
    entry_points     = {'console_scripts': ['jobpy = jobpy.__main__:main']})