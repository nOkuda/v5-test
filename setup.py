from setuptools import setup, find_packages

setup(
    name='tisapi',
    version='0.1a1',
    description='API server for Tesserae v5',
    url='https://github.com/tesserae/tisapi',
    author='Nozomu Okuda',
    author_email='Nozomu.Okuda@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Users',
        'Topic :: Digital Humanities :: Classics',
        'Topic :: Digital Humanities :: Text Processing',
        'Topic :: Digital Humanities :: Intertext Matching',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    keywords='text_processing intertext_matching',
    install_requires=[
        'tesserae @ git+https://github.com/tesserae/tesserae-v5@master',
        'apitess @ git+https://github.com/tesserae/apitess@master',
    ],
    entry_points=dict(
        console_scripts=['tisapi=src.main:start_app']
    )
)

