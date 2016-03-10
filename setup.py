from setuptools import setup, find_packages

'''
setup.py -
classifiers help PyPI in searching.
We want to exclude our docs and tests in the built distribution
when python finds packages. The exclusions would be inlcuded in
in a source distro.
When installing with pip it will look at install_requires and
satisfy those deps first. Requirements.txt is for devs
Package data is for any extra data. Say a data file including zip codes.
'''


setup(
        name='sample_package',
        version='0.0.1',
        description='Example package for demo purposes',
        long_description='Displayed on PyPI project page',
        url='https://github.com/dgeene/python_packaging',
        author='David Geene',
        author_email='myemail@gmail.com',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3'
        ],
        keywords='example project packaging',
        packages=find_packages(exclude=['docs', 'tests*'],
        install_requires=['requests'],
        package_data={
            'sample': ['package_data.dat']
        },
        data_files=None,
        # scripts= , # runnable but use entry_points instead.
        entry_points={
            'console_scripts': [
                'hello=sample:say_hello', # creates a really small wrapper exe
            ],
        }
)
