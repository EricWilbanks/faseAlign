from setuptools import setup, find_packages

setup(
    name='faseAlign',
    version='1.0.0.dev5',
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
    packages=find_packages(),
    package_data = {'faseAlign' : ['model/*']},
    install_requires=[
        'sox',
        'audiolabel'
    ],
    scripts=['faseAlign/faseAlign','faseAlign/faseAlign.py']
)
