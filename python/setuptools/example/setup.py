from setuptools import setup, find_packages

setup(
    	name='My First Setup File',
    	version='1.0',
    	packages=find_packages(),
	entry_points={
        'console_scripts': [
            		'my_start=my_package.__main__:main',
        	]
    	},
	install_requires=[
        	'numpy'
	]
)
