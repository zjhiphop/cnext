
import os.path
import lxml
import sys

from setuptools import setup
from numpy import get_include
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize


def find_libxml2_include():
    include_dirs = []
    for d in ['/usr/include/libxml2', '/usr/local/include/libxml2']:
        if os.path.exists(os.path.join(d, 'libxml/tree.h')):
            include_dirs.append(d)
    return include_dirs

ext_modules = [
    Extension('cnext.blocks',
              sources=["extractor/blocks.pyx"],
              include_dirs=(lxml.get_include() + find_libxml2_include()),
              language="c++",
              libraries=['xml2'])
]

setup(
    name='cnext',
    version='0.0.1',
    description='Extract chinese content from a web page',
    author='Jade Zhang',
    author_email='zjhiphop@gmail.com',
    url='http://github.com/zjhiphop/extractor',
    license='MIT',
    platforms='Posix; MacOS X',
    keywords='automatic content extraction, web page dechroming, HTML parsing',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['cnext'],
    package_dir={'cnext': 'extractor'},
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(ext_modules, gdb_debug=True),
    install_requires=[
        'Cython>=0.21.1',
        'lxml',
        'scikit-learn>=0.15.2,<=0.20',
        'numpy',
        'scipy',
        'ftfy>=4.1.0,<5.0.0'
    ]
)
