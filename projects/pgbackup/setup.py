from setuptools import find_packages, setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	author='José Manuel Ciges',
	author_email='jmanuel@ciges.net',
	description='A utility for backup up PostgreSQL databases',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url="http://tech.ciges.net",
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=['boto3'],
        python_requires='>=3.6',
        entry_points={
            'console_scripts': [
                'pgbackup=pgbackup.cli:main'
            ],
        }
)
