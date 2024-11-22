import setuptools
import os, shutil

def copy():
    target_path = '/data/data/com.termux/files/usr/bin/facex'
    source_path = os.path.join(os.path.dirname(__file__), 'facez/facez/facez')

    if not os.path.exists(target_path):
        shutil.copy(source_path, target_path)



setuptools.setup(
    author= 'Ipan (zelvdsk)',
    description= 'Facebook Bruteforce Attack.',
    entry_points= {'console_scripts': ['facez=facez:Start']},
    install_requires= [
        'requests', 
        'bs4'
    ],
    long_description= open("README.md").read(),
    long_description_content_type= "text/markdown",
    url= "https://github.com/jepluk/facez",
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    name= 'facez',
    packages=setuptools.find_packages(),
    cmdclass={
        'install': copy,
    },
    version='1.0.0'
)
