from setuptools import Extension, setup

module = Extension('pymsilib._msi',
    libraries = ['Msi','Rpcrt4', 'Cabinet'],
    sources = ['src/_msi.c'],
)

setup(
    ext_modules=[module]
)

