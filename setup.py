#!/usr/bin/env python3.6

from setuptools import setup, find_packages

setup(
    name='Crappy QR',
    version='1.0',
    description='',
    author='Tag',
    author_email='tagadvance+Crappy-QR@gmail.com',
    url='https://github.com/tagadvance/Crappy-QR',
    packages=find_packages(),
    install_requires=[
        'qrcode[pil]',
        'nose',
        'coverage'
    ]
)
