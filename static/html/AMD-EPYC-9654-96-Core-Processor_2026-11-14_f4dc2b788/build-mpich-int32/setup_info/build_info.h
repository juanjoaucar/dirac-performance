#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "juanau"
#define HOST_NAME                "nn6"
#define SYSTEM                   "Linux-5.14.0-687.10.1.el9_8.0.1.x86_64"
#define CMAKE_VERSION            "4.2.1"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "Release"
#define CONFIGURATION_TIME       "2026-11-15 17:29:52.192260+00:00"

#define FORTRAN_COMPILER_ID      "GNU"
#define FORTRAN_COMPILER         "/opt/eb/software/MPICH/5.0.1-GCC-15.2.0/bin/mpifort"
#define FORTRAN_COMPILER_VERSION "15.2.0"
#define FORTRAN_COMPILER_FLAGS   "-O3 -march=native -g -fcray-pointer -fbacktrace -fno-range-check -ffree-line-length-none -DVAR_GFORTRAN -DVAR_MFDS -fallow-argument-mismatch  -fno-lto"

#define C_COMPILER_ID            "GNU"
#define C_COMPILER               "/opt/eb/software/MPICH/5.0.1-GCC-15.2.0/bin/mpicc"
#define C_COMPILER_VERSION       "15.2.0"
#define C_COMPILER_FLAGS         "-O3 -march=native -g  -fno-lto"

#define CXX_COMPILER_ID          "GNU"
#define CXX_COMPILER             "/opt/eb/software/MPICH/5.0.1-GCC-15.2.0/bin/mpicxx"
#define CXX_COMPILER_VERSION     "15.2.0"
#define CXX_COMPILER_FLAGS       "-O3 -march=native -g -Wall -Wno-unknown-pragmas -Wno-sign-compare -Woverloaded-virtual -Wwrite-strings -Wno-unused  -fno-lto"

#define STATIC_LINKING           "OFF"
#define ENABLE_64BIT_INTEGERS    "OFF"
#define ENABLE_MPI               "True"
#define MPI_LAUNCHER             "/opt/eb/software/MPICH/5.0.1-GCC-15.2.0/bin/mpiexec"

#define MATH_LIBS                "-lopenblas -lgfortran"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "unknown"

#define ENABLE_EXATENSOR         "False"
#define EXATENSOR_REPO           "unknown"
#define EXATENSOR_CONFIG         "unknown"
#define EXATENSOR_HASH           "unknown"

#define DEFINITIONS              "HAVE_MPI;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT"

#endif /* BUILD_INFO_H_INCLUDED */
