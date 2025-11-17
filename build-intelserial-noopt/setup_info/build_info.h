#ifndef BUILD_INFO_H_INCLUDED
#define BUILD_INFO_H_INCLUDED

#define USER_NAME                "root"
#define HOST_NAME                "runner-vu-uzivwu-project-67998188-concurrent-0"
#define SYSTEM                   "Linux-6.2.0-32-generic"
#define CMAKE_VERSION            "4.1.2"
#define CMAKE_GENERATOR          "Unix Makefiles"
#define CMAKE_BUILD_TYPE         "release"
#define CONFIGURATION_TIME       "2025-10-27 21:46:08.934354+00:00"

#define FORTRAN_COMPILER_ID      "IntelLLVM"
#define FORTRAN_COMPILER         "/opt/intel/oneapi/compiler/2025.3/bin/ifx"
#define FORTRAN_COMPILER_VERSION "2025.3.0"
#define FORTRAN_COMPILER_FLAGS   " -w -assume byterecl -g -traceback -DVAR_IFX -fiopenmp"

#define C_COMPILER_ID            "IntelLLVM"
#define C_COMPILER               "/opt/intel/oneapi/compiler/2025.3/bin/icx"
#define C_COMPILER_VERSION       "2025.3.0"
#define C_COMPILER_FLAGS         " -g -fiopenmp"

#define CXX_COMPILER_ID          "IntelLLVM"
#define CXX_COMPILER             "/opt/intel/oneapi/compiler/2025.3/bin/icpx"
#define CXX_COMPILER_VERSION     "2025.3.0"
#define CXX_COMPILER_FLAGS       " -Wno-unknown-pragmas -fiopenmp"

#define STATIC_LINKING           "False"
#define ENABLE_64BIT_INTEGERS    "False"
#define ENABLE_MPI               "False"
#define MPI_LAUNCHER             "unknown"

#define MATH_LIBS                "unknown"
#define ENABLE_BUILTIN_BLAS      "OFF"
#define ENABLE_BUILTIN_LAPACK    "OFF"
#define EXPLICIT_LIBS            "unknown"

#define ENABLE_EXATENSOR         "ON"
#define EXATENSOR_REPO           "https://github.com/RelMBdev/ExaTENSOR.git"
#define EXATENSOR_CONFIG         "WRAP=NOWRAP BUILD_TYPE=OPT EXA_TALSH_ONLY=YES CMAKE_Fortran_COMPILER=/opt/intel/oneapi/compiler/2025.3/bin/ifx CMAKE_C_COMPILER=/opt/intel/oneapi/compiler/2025.3/bin/icx CMAKE_CXX_COMPILER=/opt/intel/oneapi/compiler/2025.3/bin/icpx TOOLKIT=INTEL EXA_OS=LINUX GPU_CUDA=NOCUDA MPILIB=NONE BLASLIB=NONE     "
#define EXATENSOR_HASH           "a1efa9efdcae13caacdc4776af839c3cd1957e85"

#define DEFINITIONS              "HAVE_MKL_BLAS;HAVE_MKL_LAPACK;HAVE_OPENMP;SYS_LINUX;PRG_DIRAC;INSTALL_WRKMEM=64000000;EXA_TALSH_ONLY;BUILD_GEN1INT;HAS_PELIB;MOD_LAO_REARRANGED;MOD_MCSCF_spinfree;MOD_XAMFI;MOD_ESR;MOD_KRCC;MOD_SRDFT;MOD_EXACORR"

#endif /* BUILD_INFO_H_INCLUDED */
