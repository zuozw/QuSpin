# this header file defines all of the types used in the template classes
# distutils: language=c++


cimport numpy as _np
from libcpp cimport bool


ctypedef _np.int64_t NP_INT64_t
ctypedef _np.int32_t NP_INT32_t
ctypedef _np.int16_t NP_INT16_t
ctypedef _np.int8_t NP_INT8_t

ctypedef _np.uint64_t NP_UINT64_t
ctypedef _np.uint32_t NP_UINT32_t
ctypedef _np.uint16_t NP_UINT16_t
ctypedef _np.uint8_t NP_UINT8_t


ctypedef fused index_type:
	NP_INT32_t
	NP_INT64_t

ctypedef fused basis_type:
	NP_UINT32_t
	NP_UINT64_t

ctypedef fused matrix_type:
	float
	double
	long double
	float complex
	double complex
	long double complex

	
ctypedef unsigned long long state_type
ctypedef long double complex scalar_type
ctypedef long double longdouble

ctypedef state_type (*bitop)(state_type, int, void*)
ctypedef state_type (*shifter)(state_type, int, int, void*)
ctypedef state_type (*ns_type)(state_type, void*)
ctypedef int (*op_type)(index_type, basis_type*, str, NP_INT32_t*,scalar_type,
						index_type*, matrix_type*,void*)





