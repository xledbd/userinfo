from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="userinfo",
    version='0.1.0',
    author='Siarhei Audzeichyk',
    author_email='siarhei.audzeichyk@gmail.com',
    description='A tool for exporting user information into JSON or CSV format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xledbd/userinfo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7'
)