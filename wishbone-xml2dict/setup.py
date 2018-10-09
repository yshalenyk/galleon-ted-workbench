import setuptools


VERSION = '0.1'
DESCRIPTION = """
Wishbone process module to transform data from xml to dict using xmltodict library
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
    'wishbone',
    'xmltodict'
]
TEST_REQUIRES = [
    'pytest',
    'pytest-cov'
]
EXTRA = {
    "test": TEST_REQUIRES
}
ENTRY_POINTS = {
    'wishbone.module.process': [
        'xml2dict = wishbone_xml2dict:Xml2DictModule'
    ],
}

setuptools.setup(
    name="wishbone_xml2dict",
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
