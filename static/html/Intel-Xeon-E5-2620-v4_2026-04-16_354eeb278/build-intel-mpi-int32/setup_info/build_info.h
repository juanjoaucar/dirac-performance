#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "juanau"
#define HOST_NAME                "nn6"
#define SYSTEM                   "Linux-5.14.0-687.10.1.el9_8.0.1.x86_64"
#define CMAKE_VERSION            "4.2.1"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "Release"
#define CONFIGURATION_TIME       "2026-11-15 17:25:25.948753+00:00"

#define FORTRAN_COMPILER_ID      "IntelLLVM"
#define FORTRAN_COMPILER         "/opt/eb-intel/software/impi/2021.17.2-intel-compilers-2025.3.3/mpi/2021.17/bin/mpiifx"
#define FORTRAN_COMPILER_VERSION "2025.3.3"
#define FORTRAN_COMPILER_FLAGS   "-O3 -xHost -w -assume byterecl -g -traceback -DVAR_IFX  -w -assume byterecl -g -traceback -DVAR_IFX "

#define C_COMPILER_ID            "IntelLLVM"
#define C_COMPILER               "/opt/eb-intel/software/impi/2021.17.2-intel-compilers-2025.3.3/mpi/2021.17/bin/mpiicx"
#define C_COMPILER_VERSION       "2025.3.3"
#define C_COMPILER_FLAGS         "-O3 -xHost -g "

#define CXX_COMPILER_ID          "IntelLLVM"
#define CXX_COMPILER             "/opt/eb-intel/software/impi/2021.17.2-intel-compilers-2025.3.3/mpi/2021.17/bin/mpiicpx"
#define CXX_COMPILER_VERSION     "2025.3.3"
#define CXX_COMPILER_FLAGS       "-O3 -xHost -Wno-unknown-pragmas "

#define STATIC_LINKING           "OFF"
#define ENABLE_64BIT_INTEGERS    "OFF"
#define ENABLE_MPI               "True"
#define MPI_LAUNCHER             "/opt/eb-intel/software/impi/2021.17.2-intel-compilers-2025.3.3/mpi/2021.17/bin/mpiexec"

#define MATH_LIBS                "unknown"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "unknown"

#define ENABLE_EXATENSOR         "False"
#define EXATENSOR_REPO           "unknown"
#define EXATENSOR_CONFIG         "unknown"
#define EXATENSOR_HASH           "unknown"

#define DEFINITIONS              "HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_MPI;VAR_MPI;VAR_MPI2;USE_MPI_MOD_F90;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;BUILD_GEN1INT;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT"

#endif /* BUILD_INFO_H_INCLUDED */
