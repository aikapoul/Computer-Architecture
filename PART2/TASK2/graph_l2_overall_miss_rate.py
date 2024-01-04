import matplotlib.pyplot as plt
import os
import numpy as np

# Δημιουργία φακέλου για τα γραφήματα
output_folder = 'plot_L2'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Δεδομένα

benchmarks_specbzip = ["specbzip_0", "specbzip_1", "specbzip_2", "specbzip_3", "specbzip_4", "specbzip_5"]
benchmarks_specmcf = ["specmcf_0", "specmcf_1", "specmcf_2", "specmcf_3", "specmcf_4", "specmcf_5"]
benchmarks_spechmmer = ["spechmmer_0", "spechmmer_1", "spechmmer_2", "spechmmer_3", "spechmmer_4", "spechmmer_5"]
benchmarks_specsjeng = ["specsjeng_0", "specsjeng_1", "specsjeng_2", "specsjeng_3", "specsjeng_4"]
benchmarks_speclibm = ["speclibm_0", "speclibm_1", "speclibm_2", "speclibm_3", "speclibm_4"]


l2_overall_miss_rate_specbzip = [0.322489, 0.414964, 0.363010, 0.324116, 0.350311, 0.376199]
l2_overall_miss_rate_specmcf = [0.059346, 0.767534, 0.711878, 0.706414, 0.706527, 0.706527]
l2_overall_miss_rate_spechmmer = [0.054065, 0.077760, 0.179990, 0.191371, 0.234873, 0.254200]
l2_overall_miss_rate_specsjeng = [0.999972, 0.999976, 0.999976, 0.999979, 0.999952]
l2_overall_miss_rate_speclibm = [0.999944, 0.999944, 0.999944, 0.999945, 0.999800]



# Κατασκευή γραφήματος
fig, axs = plt.subplots(5, 1, figsize=(8, 12))

axs[0].bar(benchmarks_specbzip, l2_overall_miss_rate_specbzip, color='blue')
axs[0].set_title('L2_overall_miss_rate for specbzip Benchmarks')
axs[0].set_xlabel('Benchmark')
axs[0].set_ylabel('l2_overall_miss_rate')

axs[1].bar(benchmarks_specmcf, l2_overall_miss_rate_specmcf, color='green')
axs[1].set_title('L2_overall_miss_rate for specmcf Benchmarks')
axs[1].set_xlabel('Benchmark')
axs[1].set_ylabel('l2_overall_miss_rate')

axs[2].bar(benchmarks_spechmmer, l2_overall_miss_rate_spechmmer, color='orange')
axs[2].set_title('L2_overall_miss_rate for spechmmer Benchmarks')
axs[2].set_xlabel('Benchmark')
axs[2].set_ylabel('l2_overall_miss_rate')

axs[3].bar(benchmarks_specsjeng, l2_overall_miss_rate_specsjeng, color='red')
axs[3].set_title('L2_overall_miss_rate for specsjeng Benchmarks')
axs[3].set_xlabel('Benchmark')
axs[3].set_ylabel('l2_overall_miss_rate')

axs[4].bar(benchmarks_speclibm, l2_overall_miss_rate_speclibm, color='purple')
axs[4].set_title('L2_overall_miss_rate for speclibm Benchmarks')
axs[4].set_xlabel('Benchmark')
axs[4].set_ylabel('l2_overall_miss_rate')

# Εμφάνιση γραφημάτων
output_file = os.path.join(output_folder, "L2_plot.png")
plt.tight_layout()
plt.savefig(output_file)
plt.show()
