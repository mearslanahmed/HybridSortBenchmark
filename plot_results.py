import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")
plt.figure(figsize=(10,6))
plt.plot(df['s'], df['time_ms'], marker='o')
plt.xlabel('s (insertion threshold)')
plt.ylabel('Time to sort (ms)')
plt.title('Hybrid MergeSort: threshold s vs time')
plt.grid(True)
plt.tight_layout()
plt.savefig('hybrid_sort_plot.png', dpi=300)
print("Saved hybrid_sort_plot.png")
plt.show()