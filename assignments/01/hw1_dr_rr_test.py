#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import custom_quantizers_copy as cq


k = 2
num_means = 100
num_samples = 5000

def test_quantizer(k, num_means, num_samples):

    mse_dr = np.zeros(num_means)
    bias_dr = np.zeros(num_means)
    mse_rr = np.zeros(num_means)
    bias_rr = np.zeros(num_means)

    mean_diff_vec = np.linspace(start=0, stop = 1.0, num=num_means)

    for i in range(num_means):
        mean_vec = mean_diff_vec[i] * np.ones(num_samples)
        x = mean_vec.copy()

        quantized_vec = cq.quantize_samples_deterministic_rounding(x, k)
        reconst_vec = cq.reconstruct_samples_deterministic_rounding(quantized_vec, k)
        bias_dr[i] = np.sum(reconst_vec - mean_vec)/num_samples
        mse_dr[i] = np.sum(((reconst_vec-mean_vec)**2))/num_samples

        quantized_vec = cq.quantize_samples_randomized_rounding(x, k)
        reconst_vec = cq.reconstruct_samples_randomized_rounding(quantized_vec, k)
        bias_rr[i] = np.sum(reconst_vec - mean_vec)/num_samples
        mse_rr[i] = np.sum(((reconst_vec-mean_vec)**2))/num_samples

    print(bias_dr,mse_dr)
    print(bias_rr,mse_rr)
    fig, ax = plt.subplots()
    ax.plot(mean_diff_vec,bias_dr,'r',label='Deterministic rounding')
    ax.plot(mean_diff_vec,bias_rr,'b--',label='Randomized rounding')
    plt.grid(True)
    plt.title('Avg bias for k = '+str(k))
    plt.xlabel('x')
    plt.ylabel('Average Bias')
    legend = ax.legend(loc='upper right', shadow=True)
    # Put a nicer background color on the legend.
    legend.get_frame().set_facecolor('C0')
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(mean_diff_vec,mse_dr,'r',label='Deterministic rounding')
    ax.plot(mean_diff_vec,mse_rr,'b--',label='Randomized rounding')
    plt.grid(True)
    plt.title('Avg SE for k = '+str(k))
    plt.xlabel('x')
    plt.ylabel('Average SE')
    legend = ax.legend(loc='upper right', shadow=True)
    # Put a nicer background color on the legend.
    legend.get_frame().set_facecolor('C0')
    plt.show()

test_quantizer(k,num_means,num_samples)
