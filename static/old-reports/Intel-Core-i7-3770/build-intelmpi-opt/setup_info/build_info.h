#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "root"
#define HOST_NAME                "runner-5q3rco021-project-67998188-concurrent-0"
#define SYSTEM                   "Linux-5.14.0-626.el9.x86_64"
#define CMAKE_VERSION            "4.1.2"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "release"
#define CONFIGURATION_TIME       "2025-11-17 04:27:22.123719+00:00"

#define FORTRAN_COMPILER_ID      "IntelLLVM"
#define FORTRAN_COMPILER         "/opt/intel/oneapi/mpi/2021.17/bin/mpiifx"
#define FORTRAN_COMPILER_VERSION "2025.3.0"
#define FORTRAN_COMPILER_FLAGS   " -qopenmp -O3 -xHost -w -assume byterecl -g -traceback -DVAR_IFX  -fiopenmp"

#define C_COMPILER_ID            "IntelLLVM"
#define C_COMPILER               "/opt/intel/oneapi/mpi/2021.17/bin/mpiicx"
#define C_COMPILER_VERSION       "2025.3.0"
#define C_COMPILER_FLAGS         " -qopenmp -O3 -xHost -g  -fiopenmp"

#define CXX_COMPILER_ID          "IntelLLVM"
#define CXX_COMPILER             "/opt/intel/oneapi/mpi/2021.17/bin/mpiicpx"
#define CXX_COMPILER_VERSION     "2025.3.0"
#define CXX_COMPILER_FLAGS       " -qopenmp -O3 -xHost -Wno-unknown-pragmas  -fiopenmp"

#define STATIC_LINKING           "False"
#define ENABLE_64BIT_INTEGERS    "False"
#define ENABLE_MPI               "True"
#define MPI_LAUNCHER             "/opt/intel/oneapi/mpi/2021.17/bin/mpiexec"

#define MATH_LIBS                "-Wl,--start-group;/opt/intel/oneapi/mkl/2025.3/lib/intel64/libmkl_lapack95_lp64.a;/opt/intel/oneapi/mkl/2025.3/lib/intel64/libmkl_intel_lp64.so;-qopenmp;-Wl,--end-group;-Wl,--start-group;/opt/intel/oneapi/mkl/2025.3/lib/intel64/libmkl_intel_lp64.so;/opt/intel/oneapi/mkl/2025.3/lib/intel64/libmkl_intel_thread.so;/opt/intel/oneapi/mkl/2025.3/lib/intel64/libmkl_core.so;/usr/lib/x86_64-linux-gnu/libpthread.a;/usr/lib/x86_64-linux-gnu/libm.so;-qopenmp;-Wl,--end-group"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "unknown"

#define ENABLE_EXATENSOR         "OFF"
#define EXATENSOR_REPO           "unknown"
#define EXATENSOR_CONFIG         "unknown"
#define EXATENSOR_HASH           "unknown"

#define DEFINITIONS              "HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;HAVE_OPENMP;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;HAS_PELIB;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT"

#endif /* BUILD_INFO_H_INCLUDED */
