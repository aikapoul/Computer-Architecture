import pandas as pd
import matplotlib.pyplot as plt
import os

# Τα δεδομένα σας
data = {
    'Benchmark': ['specbzip', 'speclibm', 'spechmmer', 'specmcf', 'specsjeng'],
    'sim_seconds': [0.083982, 0.174671, 0.059396, 0.064955, 0.513528],
    'system.cpu.cpi': [1.679650, 3.493415, 1.187917, 1.299095, 10.270554],
    'system.cpu.dcache.overall_miss_rate::total': [0.014798, 0.060972, 0.001637, 0.002108, 0.121831],
    'system.cpu.icache.overall_miss_rate::total': [0.000077, 0.000094, 0.000221, 0.023612, 0.000020],
    'system.l2.overall_miss_rate::total': [0.282163, 0.999944, 0.077760, 0.055046, 0.999972]
}

# Δημιουργία DataFrame
df = pd.DataFrame(data)

# Δημιουργία φακέλου για τα γραφήματα
output_folder = 'plots'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Κάντε plot ξεχωριστά για sim_seconds και system.cpu.cpi
for metric in ['sim_seconds', 'system.cpu.cpi', 'system.cpu.dcache.overall_miss_rate::total', 'system.cpu.icache.overall_miss_rate::total', 'system.l2.overall_miss_rate::total']:
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.bar(df['Benchmark'], df[metric])
    ax.set_title(metric)
    ax.set_ylabel('Value')
    
    
    output_file = os.path.join(output_folder, f'{metric.replace("::", "_")}.png')

    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

print(f'Τα γραφήματα αποθηκεύτηκαν στον φάκελο: {output_folder}')
