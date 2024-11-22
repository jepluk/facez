import setuptools
import os
import shutil
from setuptools.command.install import install

# Buat kelas custom yang menggantikan install
class PostInstallCommand(install):
    def run(self):
        # Jalankan instalasi terlebih dahulu
        install.run(self)
        
        # Tentukan path untuk file facex
        target_path = '/data/data/com.termux/files/usr/bin/facex'
        # Tentukan path sumber file facex.py
        source_path = os.path.join(os.path.dirname(__file__), 'facez/facez/facez.py')
        
        # Salin file ke target path jika belum ada
        if not os.path.exists(target_path):
            shutil.copy(source_path, target_path)
            print(f"File facex.py berhasil disalin ke {target_path}")
        else:
            print("File facex.py sudah ada di path tujuan.")

# Setup untuk menginstal paket
setuptools.setup(
    author='Ipan (zelvdsk)',
    description='Facebook Bruteforce Attack.',
    entry_points={'console_scripts': ['facez=facez:Start']},
    install_requires=[
        'requests',
        'bs4'
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jepluk/facez",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    name='facez',
    packages=setuptools.find_packages(),
    cmdclass={
        'install': PostInstallCommand,  # Menggunakan kelas custom untuk post-install
    },
    version='1.0.0'
)

