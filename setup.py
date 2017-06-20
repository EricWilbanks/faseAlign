from setuptools import setup

setup(
    name='fase-align',
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
    packages='fase-align',
    install_requires=[
        'sox',
        'audiolabel'
    ],
)