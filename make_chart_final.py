import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.expanduser('~/Downloads/surface_by_period_final.csv'))
df = df.sort_values('pct_surface', ascending=True)

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(df['period'], df['pct_surface'], color='steelblue')
ax.set_xlabel('% of Global Land Surface')
ax.set_title('Global Land Surface Exposure by Geologic Period\n(148.3M km2 mapped, USGS World Geology + SGMC, PostGIS)')
ax.bar_label(bars, fmt='%.1f%%', padding=3)
plt.tight_layout()
plt.savefig(os.path.expanduser('~/Downloads/surface_by_period_final.png'), dpi=150)
print("Done")
