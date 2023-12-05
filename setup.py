from setuptools import setup, find_packages

setup(
    name='excell_functions',
    version='0.03',
    packages=find_packages(),
    url='https://github.com/A1eksMa/excell_functions',
    license='MIT',
    author='A1eksMa',
    author_email='a1ex_ma@mail.ru',
    description='A Python library for emulation Excell functions',
    long_description=open('README.md').read(),
    install_requires=[
        import numpy as np
        import pandas as pd
        import math
    ],
)
