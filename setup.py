from setuptools import find_packages, setup

__author__ = 'peter'

install_requires = open('requirements.txt').read().splitlines()

setup(
    # name of application
    name='SHINKAFA',
    # version number goes her
    version='0.0.1',
    # Authors name
    author='Edache Peter',
    # author email address
    author_email='peter.edache@flexisaf.com',

    packages=find_packages(exclude=['tests*']),

    # include additional files into the package
    include_package_data=True,

    # the saf tims hr site
    url="http://flexisaf.net/saftims-hr-demo.html",

    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'hr_setup = scripts.setuphr:main',
        ]
    },
    classifiers=[
        'Private :: Dont upload to any pypi registry'
    ]

)
