from distutils.core import setup

setup(
    name='awesome_print',
    version='0.1.2',
    author='Stan Mazhara',
    author_email='akmegran@gmail.com',
    packages=['awesome_print', 'awesome_print.test'],
    license='LICENSE',
    description='Awesome print.',
    long_description=open('README.txt').read(),
    url='https://github.com/smazhara/awesome_print',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ]
)
