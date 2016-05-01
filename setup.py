from setuptools import setup

setup(
    name='to-do application',
    version='0.1',
    py_modules=['main'],
    include_package_data=True,
    install_requires=[
        'click',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        main=main:cli
    ''',
)