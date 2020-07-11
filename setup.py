#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="João Vitor F. Cavalcante",
    author_email='jvfe@ufrn.edu.br',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python wrapper around the clinicaltrials.gov API",
    install_requires=["requests"],
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pytrials',
    name='pytrials',
    packages=find_packages(include=['pytrials', 'pytrials.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jvfe/pytrials',
    version='0.1.2',
    zip_safe=False,
)
