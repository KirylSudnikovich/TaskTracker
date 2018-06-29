from setuptools import setup, find_packages

root = 'lib'
packages = [root] + [root + '.' + item for item in find_packages(root)]
setup(
    name='lib',
    version='0.1',
    author='sad_snitch',
    author_email='0311snitch@gmail.com',
    packages=packages,
    install_requires=["logging", "sqlite3", "enum", "os"],
    description='library part of Takinata',
    include_package_data=False,
)
