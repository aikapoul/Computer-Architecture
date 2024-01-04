import matplotlib.pyplot as plt
import os
import numpy as np

# Δημιουργία φακέλου για τα γραφήματα
output_folder = 'plot_Icache'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Δεδομένα

benchmarks_specbzip = ["specbzip_0", "specbzip_1", "specbzip_2", "specbzip_3", "specbzip_4", "specbzip_5"]
benchmarks_specmcf = ["specmcf_0", "specmcf_1", "specmcf_2", "specmcf_3", "specmcf_4", "specmcf_5"]
benchmarks_spechmmer = ["spechmmer_0", "spechmmer_1", "spechmmer_2", "spechmmer_3", "spechmmer_4", "spechmmer_5"]
benchmarks_specsjeng = ["specsjeng_0", "specsjeng_1", "specsjeng_2", "specsjeng_3", "specsjeng_4"]
benchmarks_speclibm = ["speclibm_0", "speclibm_1", "speclibm_2", "speclibm_3", "speclibm_4"]


icache_overall_miss_rate_specbzip = [0.000077, 0.000077, 0.000077, 0.000077, 0.000077, 0.000077]
icache_overall_miss_rate_specmcf = [0.023612, 0.000018, 0.000018, 0.000018, 0.000018, 0.000018]
icache_overall_miss_rate_spechmmer = [0.000221, 0.000221, 0.000212, 0.000210, 0.000208, 0.000184]
icache_overall_miss_rate_specsjeng = [0.000020, 0.000020, 0.000020, 0.000020, 0.000015]
icache_overall_miss_rate_speclibm = [0.000094, 0.000094, 0.000094, 0.000094, 0.000112]



# Κατασκευή γραφήματος
fig, axs = plt.subplots(5, 1, figsize=(8, 12))

axs[0].bar(benchmarks_specbzip, icache_overall_miss_rate_specbzip, color='blue')
axs[0].set_title('Icache_overall_miss_rate for specbzip Benchmarks')
axs[0].set_xlabel('Benchmark')
axs[0].set_ylabel('icache_overall_miss_rate')

axs[1].bar(benchmarks_specmcf, icache_overall_miss_rate_specmcf, color='green')
axs[1].set_title('Icache_overall_miss_rate for specmcf Benchmarks')
axs[1].set_xlabel('Benchmark')
axs[1].set_ylabel('icache_overall_miss_rate')

axs[2].bar(benchmarks_spechmmer, icache_overall_miss_rate_spechmmer, color='orange')
axs[2].set_title('Icache_overall_miss_rate for spechmmer Benchmarks')
axs[2].set_xlabel('Benchmark')
axs[2].set_ylabel('icache_overall_miss_rate')

axs[3].bar(benchmarks_specsjeng, icache_overall_miss_rate_specsjeng, color='red')
axs[3].set_title('Icache_overall_miss_rate for specsjeng Benchmarks')
axs[3].set_xlabel('Benchmark')
axs[3].set_ylabel('icache_overall_miss_rate')

axs[4].bar(benchmarks_speclibm, icache_overall_miss_rate_speclibm, color='purple')
axs[4].set_title('Icache_overall_miss_rate for speclibm Benchmarks')
axs[4].set_xlabel('Benchmark')
axs[4].set_ylabel('icache_overall_miss_rate')

# Εμφάνιση γραφημάτων
output_file = os.path.join(output_folder, "Icache_plot.png")
plt.tight_layout()
plt.savefig(output_file)
plt.show()
