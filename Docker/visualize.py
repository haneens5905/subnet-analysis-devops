# visualize.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('subnet_report.csv')

plt.bar(df['CIDR Notation'], df['Usable Hosts'])
plt.xlabel('CIDR Notation')
plt.ylabel('Usable Hosts')
plt.title('Usable Hosts per Subnet')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.savefig('network_plot.png')

print("Visualization saved as network_plot.png")