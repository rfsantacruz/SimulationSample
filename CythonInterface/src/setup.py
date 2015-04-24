# setup.py file
import sys
import os
import shutil

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# build "pyCPPEngine.so" python extension to be added to "PYTHONPATH" afterwards...
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("pyCPPEngine", 
                  sources=["./src/pyCPPEngine.pyx"],
                  libraries=["CPPEngine"],          # refers to "libCPPEngine.so"
                  runtime_library_dirs=['/home/rfsantacruz/Documents/Wokspaces/EclipsePython/SimulationSample/trunk/libs/'],
                  language="c++",                   # remove this if C and not C++
                  extra_compile_args=["-I./headers", "-fopenmp", "-O3"], #-Ipath to headers
                  extra_link_args=["-DSOME_DEFINE_OPT", "-L./libs"] #-L path to libs.so                  
             )
        ]
)           
