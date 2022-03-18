import setuptools

with open('requirements/package.requirements.txt') as handler:
    install_requires = handler.readlines()

print('dependencies:')
print (install_requires)

setuptools.setup(
    install_requires=install_requires,
    name='hello_pyspark',
    package_dir={'':'src'},
    packages=setuptools.find_packages('src'),
    version=1.0
)