import setuptools

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
    version='1.0.0'
)
