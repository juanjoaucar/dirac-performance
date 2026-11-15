#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "root"
#define HOST_NAME                "runner-5q3rco021-project-67998188-concurrent-0"
#define SYSTEM                   "Linux-5.14.0-626.el9.x86_64"
#define CMAKE_VERSION            "4.1.2"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "release"
#define CONFIGURATION_TIME       "2025-11-18 00:51:15.260138+00:00"

#define FORTRAN_COMPILER_ID      "GNU"
#define FORTRAN_COMPILER         "/mpich64-long/bin/mpif90"
#define FORTRAN_COMPILER_VERSION "13.3.0"
#define FORTRAN_COMPILER_FLAGS   " -O3 -march=native -g -fcray-pointer -fbacktrace -fno-range-check -DVAR_GFORTRAN -DVAR_MFDS -fallow-argument-mismatch  -fopenmp -fdefault-integer-8 -fno-lto"

#define C_COMPILER_ID            "GNU"
#define C_COMPILER               "/mpich64-long/bin/mpicc"
#define C_COMPILER_VERSION       "13.3.0"
#define C_COMPILER_FLAGS         " -O3 -march=native -g  -fopenmp -fno-lto"

#define CXX_COMPILER_ID          "GNU"
#define CXX_COMPILER             "/mpich64-long/bin/mpicxx"
#define CXX_COMPILER_VERSION     "13.3.0"
#define CXX_COMPILER_FLAGS       " -O3 -march=native -g -Wall -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused  -fopenmp -fno-lto"

#define STATIC_LINKING           "False"
#define ENABLE_64BIT_INTEGERS    "True"
#define ENABLE_MPI               "True"
#define MPI_LAUNCHER             "/mpich64-long/bin/mpiexec"

#define MATH_LIBS                "unknown"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "-L/opt/openblas64/lib -lopenblas"

#define ENABLE_EXATENSOR         "OFF"
#define EXATENSOR_REPO           "unknown"
#define EXATENSOR_CONFIG         "unknown"
#define EXATENSOR_HASH           "unknown"

#define DEFINITIONS              "HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INT_STAR8;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT"

#endif /* BUILD_INFO_H_INCLUDED */
