import matplotlib.pyplot as plt
import os
import numpy as np

# Δημιουργία φακέλου για τα γραφήματα
output_folder = 'plot_Dcache'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Δεδομένα

benchmarks_specbzip = ["specbzip_0", "specbzip_1", "specbzip_2", "specbzip_3", "specbzip_4", "specbzip_5"]
benchmarks_specmcf = ["specmcf_0", "specmcf_1", "specmcf_2", "specmcf_3", "specmcf_4", "specmcf_5"]
benchmarks_spechmmer = ["spechmmer_0", "spechmmer_1", "spechmmer_2", "spechmmer_3", "spechmmer_4", "spechmmer_5"]
benchmarks_specsjeng = ["specsjeng_0", "specsjeng_1", "specsjeng_2", "specsjeng_3", "specsjeng_4"]
benchmarks_speclibm = ["speclibm_0", "speclibm_1", "speclibm_2", "speclibm_3", "speclibm_4"]


dcache_overall_miss_rate_specbzip = [0.014794, 0.011743, 0.011742, 0.011739, 0.010945, 0.010268]
dcache_overall_miss_rate_specmcf = [0.002108, 0.002108, 0.002108, 0.002108, 0.002108, 0.002108]
dcache_overall_miss_rate_spechmmer = [0.002359, 0.001637, 0.000701, 0.000669, 0.000550, 0.001022]
dcache_overall_miss_rate_specsjeng = [0.121831, 0.121831, 0.121831, 0.121831, 0.060918]
dcache_overall_miss_rate_speclibm = [0.060972, 0.060972, 0.060972, 0.060972, 0.030487]



# Κατασκευή γραφήματος
fig, axs = plt.subplots(5, 1, figsize=(8, 12))

axs[0].bar(benchmarks_specbzip, dcache_overall_miss_rate_specbzip, color='blue')
axs[0].set_title('Dcache_overall_miss_rate for specbzip Benchmarks')
axs[0].set_xlabel('Benchmark')
axs[0].set_ylabel('Dcache_overall_miss_rate')

axs[1].bar(benchmarks_specmcf, dcache_overall_miss_rate_specmcf, color='green')
axs[1].set_title('Dcache_overall_miss_rate for specmcf Benchmarks')
axs[1].set_xlabel('Benchmark')
axs[1].set_ylabel('Dcache_overall_miss_rate')

axs[2].bar(benchmarks_spechmmer, dcache_overall_miss_rate_spechmmer, color='orange')
axs[2].set_title('Dcache_overall_miss_rate for spechmmer Benchmarks')
axs[2].set_xlabel('Benchmark')
axs[2].set_ylabel('Dcache_overall_miss_rate')

axs[3].bar(benchmarks_specsjeng, dcache_overall_miss_rate_specsjeng, color='red')
axs[3].set_title('Dcache_overall_miss_rate for specsjeng Benchmarks')
axs[3].set_xlabel('Benchmark')
axs[3].set_ylabel('Dcache_overall_miss_rate')

axs[4].bar(benchmarks_speclibm, dcache_overall_miss_rate_speclibm, color='purple')
axs[4].set_title('Dcache_overall_miss_rate for speclibm Benchmarks')
axs[4].set_xlabel('Benchmark')
axs[4].set_ylabel('Dcache_overall_miss_rate')

# Εμφάνιση γραφημάτων
output_file = os.path.join(output_folder, "Dcache_plot.png")
plt.tight_layout()
plt.savefig(output_file)
plt.show()
