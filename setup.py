from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

exts = [
    Extension(
    	"fibo",  # will create 'fibo.so' ...
    	["fibo.pyx"],  # thanks to 'fibo.pyx'.
    	include_dirs=['libcalcul/headers/'],  # *.h here
    	library_dirs=['libcalcul/libs/'],  # *.so here
    	libraries=["calcul"],  # needs 'libcalcul.so'.
    ),
]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = exts
)
