#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "root"
#define HOST_NAME                "runner-5q3rco021-project-67998188-concurrent-0"
#define SYSTEM                   "Linux-5.14.0-626.el9.x86_64"
#define CMAKE_VERSION            "4.1.2"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "release"
#define CONFIGURATION_TIME       "2025-11-17 04:05:27.666242+00:00"

#define FORTRAN_COMPILER_ID      "GNU"
#define FORTRAN_COMPILER         "/usr/bin/mpif90"
#define FORTRAN_COMPILER_VERSION "13.3.0"
#define FORTRAN_COMPILER_FLAGS   " -O3 -march=native -g -fcray-pointer -fbacktrace -fno-range-check -DVAR_GFORTRAN -DVAR_MFDS -fallow-argument-mismatch  -fopenmp -fno-lto"

#define C_COMPILER_ID            "GNU"
#define C_COMPILER               "/usr/bin/mpicc"
#define C_COMPILER_VERSION       "13.3.0"
#define C_COMPILER_FLAGS         " -O3 -march=native -g  -fopenmp -fno-lto"

#define CXX_COMPILER_ID          "GNU"
#define CXX_COMPILER             "/usr/bin/mpicxx"
#define CXX_COMPILER_VERSION     "13.3.0"
#define CXX_COMPILER_FLAGS       " -O3 -march=native -g -Wall -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused  -fopenmp -fno-lto"

#define STATIC_LINKING           "False"
#define ENABLE_64BIT_INTEGERS    "False"
#define ENABLE_MPI               "True"
#define MPI_LAUNCHER             "/usr/bin/mpiexec"

#define MATH_LIBS                "unknown"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "-L/opt/openblas32/lib -lopenblas"

#define ENABLE_EXATENSOR         "OFF"
#define EXATENSOR_REPO           "unknown"
#define EXATENSOR_CONFIG         "unknown"
#define EXATENSOR_HASH           "unknown"

#define DEFINITIONS              "HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT"

#endif /* BUILD_INFO_H_INCLUDED */
