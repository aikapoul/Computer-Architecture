import matplotlib.pyplot as plt
import os
import numpy as np


output_folder = 'plot_CPI'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)



benchmarks_specbzip = ["specbzip_0", "specbzip_1", "specbzip_2", "specbzip_3", "specbzip_4", "specbzip_5"]
benchmarks_specmcf = ["specmcf_0", "specmcf_1", "specmcf_2", "specmcf_3", "specmcf_4", "specmcf_5"]
benchmarks_spechmmer = ["spechmmer_0", "spechmmer_1", "spechmmer_2", "spechmmer_3", "spechmmer_4", "spechmmer_5"]
benchmarks_specsjeng = ["specsjeng_0", "specsjeng_1", "specsjeng_2", "specsjeng_3", "specsjeng_4"]
benchmarks_speclibm = ["speclibm_0", "speclibm_1", "speclibm_2", "speclibm_3", "speclibm_4"]


cpi_specbzip = [1.712208, 1.682914, 1.649604, 1.624885, 1.617195, 1.610993]
cpi_specmcf = [1.303750, 1.160209, 1.155606, 1.155199, 1.155043, 1.155043]
cpi_spechmmer = [1.191346, 1.187917, 1.186170, 1.185883, 1.185423, 1.191663]
cpi_specsjeng = [10.270554, 10.270520, 10.265530, 10.265417, 6.794691]
cpi_speclibm = [3.493415, 3.493415, 3.489639, 3.489639, 2.576667]




fig, axs = plt.subplots(5, 1, figsize=(8, 12))

axs[0].bar(benchmarks_specbzip, cpi_specbzip, color='blue')
axs[0].set_title('CPI for specbzip Benchmarks')
axs[0].set_xlabel('Benchmark')
axs[0].set_ylabel('CPI')

axs[1].bar(benchmarks_specmcf, cpi_specmcf, color='green')
axs[1].set_title('CPI for specmcf Benchmarks')
axs[1].set_xlabel('Benchmark')
axs[1].set_ylabel('CPI')

axs[2].bar(benchmarks_spechmmer, cpi_spechmmer, color='orange')
axs[2].set_title('CPI for spechmmer Benchmarks')
axs[2].set_xlabel('Benchmark')
axs[2].set_ylabel('CPI')

axs[3].bar(benchmarks_specsjeng, cpi_specsjeng, color='red')
axs[3].set_title('CPI for specsjeng Benchmarks')
axs[3].set_xlabel('Benchmark')
axs[3].set_ylabel('CPI')

axs[4].bar(benchmarks_speclibm, cpi_speclibm, color='purple')
axs[4].set_title('CPI for speclibm Benchmarks')
axs[4].set_xlabel('Benchmark')
axs[4].set_ylabel('CPI')


output_file = os.path.join(output_folder, "CPI_plot.png")
plt.tight_layout()
plt.savefig(output_file)
plt.show()
