# coding: utf-8


from setuptools import setup  # type: ignore

setup(
    name='arcor2_kinali',
    version='0.1',
    packages=['arcor2_kinali', 'arcor2_kinali.object_types', 'arcor2_kinali.services'],
    package_data={"arcor2_kinali": ["py.typed"]},
    url='',
    license='',
    author='Robo@FIT',
    author_email='imaterna@fit.vutbr.cz',
    description='',
    install_requires=[
    ],
    zip_safe=False,
)
