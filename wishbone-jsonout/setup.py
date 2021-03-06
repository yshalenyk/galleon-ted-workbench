import setuptools


VERSION = '0.1'
DESCRIPTION = """
Wishbone output module to dumpt passed data into json file
"""
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]
INSTALL_REQUIRES = [
    'setuptools',
    'wishbone>=3.0',
    'simplejson'
]
TEST_REQUIRES = [
    'pytest',
    'pytest-cov'
]
EXTRA = {
    "test": TEST_REQUIRES
}
ENTRY_POINTS = {
    'wishbone.module.output': [
        'jsonfile = wishbone_jsonout:FileOut'
    ],
}

setuptools.setup(
    name="wishbone_jsonout",
    version=VERSION,
    url="-",
    author="yshalenyk",
    author_email="yshalenyk@quintagroup.com",
    description=DESCRIPTION,
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA,
    setup_requires=['pytest-runner'],
    entry_points=ENTRY_POINTS,
    classifiers=CLASSIFIERS
)
