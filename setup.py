from setuptools import Extension, setup

module = Extension('msilib._msi',
    libraries = ['Msi','Rpcrt4', 'Cabinet'],
    sources = ['src/_msi.c'],
)

setup(
    name="pymsilib",
    version="1.0.0",
    description = 'msilib replacement',
    long_description_content_type = 'text/x-rst',
    author = 'Trevor Hamm',
    author_email = 'alohaeh@gmail.com',
    ext_modules=[module],
)

