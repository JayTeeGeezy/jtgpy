from setuptools import setup


def read_text(filename):
	with open(filename) as f:
		return f.read()


setup(
	name='jtgpy',
	version='0.0.2',
	description='JTG\'s Common Python Code',
	long_description=read_text('README.rst'),
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: No Input/Output (Daemon)',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.4',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	keywords='common Python code',
	url='https://github.com/JayTeeGeezy/jtgpy',
	author='Jason Green',
	author_email='JayTeeGeezy@outlook.com',
	license='MIT',
	packages=[
		'jtgpy'
	],
	scripts=[
	],
	entry_points={
		'console_scripts': [
		]
	},
	install_requires=[
	],
	test_suite='nose.collector',
	tests_require=[
		'nose'
	],
	dependency_links=[
	],
	include_package_data=True,
	zip_safe=False
	)