# coding: utf-8


from setuptools import setup  # type: ignore

import arcor2_kinali

setup(
    name='arcor2_kinali',
    version=arcor2_kinali.version(),
    packages=['arcor2_kinali', 'arcor2_kinali.object_types', 'arcor2_kinali.services'],
    package_data={"arcor2_kinali": ["py.typed"]},
    url='',
    license='',
    author='Robo@FIT',
    author_email='imaterna@fit.vutbr.cz',
    description='',
    install_requires=[
        'dataclasses',
        'dataclasses-jsonschema[fast-validation]',
        'arcor2==0.2.*'
    ],
    zip_safe=False,
)
