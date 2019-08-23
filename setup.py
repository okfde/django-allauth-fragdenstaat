#!/usr/bin/env python
import io

from setuptools import setup, find_packages


long_description = io.open('README.md', encoding='utf-8').read()

METADATA = dict(
    name='django-allauth-fragdenstaat',
    version='0.0.2',
    author='Stefan Wehrmeyer',
    author_email='stefan.wehrmeyer@okfn.de',
    description='Django applications addressing'
    ' authentication with FragDenStaat.de as a django-allauth module',
    long_description=long_description,
    url='http://github.com/okfde/django-allauth-fragdenstaat',
    keywords='django auth account social oauth fragdenstaat registration',
    tests_require=[],
    install_requires=['django-allauth'],
    include_package_data=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**METADATA)
