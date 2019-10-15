from setuptools import setup

setup(
    name='faseAlign',
    version='1.1.10',
    description='Command Line python module for Force Aligning Spanish using HTK',
    url='https://github.com/EricWilbanks/faseAlign',
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
    packages=['faseAlign'],
    package_data = {'faseAlign' : ['model/*']},
    install_requires=[
        'sox',
        'audiolabel'
    ],
    scripts=['bin/faseAlign']
	include_package_data=True,
	zip_safe=False
)
