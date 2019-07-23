# coding: utf-8


from setuptools import setup  # type: ignore

setup(
    name='arcor2_kinali',
    version='0.1',
    packages=['arcor2_kinali', 'arcor2_kinali.object_types'],
    package_data={"arcor2_kinali": ["py.typed"]},
    url='',
    license='',
    author='Robo@FIT',
    author_email='imaterna@fit.vutbr.cz',
    description='',
    install_requires=[
        # 'arcor2',
        'pymongo'
    ],
    zip_safe=False,
)
