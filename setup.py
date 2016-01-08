#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-modeldict-yplan',
    version='1.4.2',
    author='DISQUS',
    author_email='opensource@disqus.com',
    maintainer='YPlan',
    maintainer_email='adam@yplanapp.com',
    url='http://github.com/YPlan/django-modeldict',
    description='Stores a model as a dictionary',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
