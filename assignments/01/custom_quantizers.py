#!/usr/bin/env python3


def quantize_samples_deterministic_rounding(x, k):
    # x is a numpy array of reals of length N
    # k is the number of bits used to quantize each sample
    N = np.size(x)


    # quantized_bits should be an N-length numpy array with entries from {0,1,..., 2^k-1}
    return(quantized_bits)

def reconstruct_samples_deterministic_rounding(quantized_values,k):
    # quantized_values is a numpy array with entries from {0,1,...,2^k-1}
    N = np.size(quantized_values)

    #reconstructed_values should be a numpy array of length N
    return(reconstructed_values)

def quantize_samples_randomized_rounding(x, k):
    # x is a numpy array of reals of length N
    # k is the number of bits used to quantize each sample
    N = np.size(x)


    # quantized_bits should be an N-length numpy array with entries from {0,1,..., 2^k-1}
    return(quantized_bits)

def reconstruct_samples_randomized_rounding(quantized_values,k):
    # quantized_values is a numpy array with entries from {0,1,...,2^k-1}
    N = np.size(quantized_values)

    #reconstructed_values should be a numpy array of length N
    return(reconstructed_values)
