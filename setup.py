# encoding=utf8

import codecs
from setuptools import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="gdgajubot",
    version="1.5",
    author="GDG Aracaju",
    url="http://site.gdgaracaju.com.br/",
    description="GDG Aracaju Bot",
    long_description=codecs.open("README.md", 'r', encoding='utf-8').read(),
    license="GPLv2",
    entry_points={
        'console_scripts': [
            'gdgajubot = gdgajubot.__main__:main',
        ],
    },
    packages=['gdgajubot', 'gdgajubot.data'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: Portuguese (Brazilian)",
        "Topic :: Communications :: Chat",
    ],
)
