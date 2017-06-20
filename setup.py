from setuptools import setup, find_packages

setup(
    name='fase-align',

    # Versions should comply with PEP440. For single-sourced versioning, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='1.0.0.dev1',

    description='Command Line python module for Force Aligning Spanish using HTK',
    long_description='long-description-here',

    url='https://github.com/EricWilbanks/fase-align',

    author='Eric Wilbanks',
    author_email='wilbanks.ericw@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],

    keywords='phonetics alignment spanish corpus',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages='fase-align',

    install_requires=[
        'sox',
        'audiolabel'
    ],
)