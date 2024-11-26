from setuptools import Extension, setup

module = Extension('msilib._msi',
    libraries = ['Msi','Rpcrt4', 'Cabinet'],
    sources = ['src/_msi.c'],
)

setup(
    name="msilib",
    version="1.0.0",
    description = 'msilib replacement',
    author = 'Trevor Hamm',
    author_email = 'alohaeh@gmail.com',
    ext_modules=[module],
)

