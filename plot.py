import matplotlib.pyplot as plt

# Data
x = [10, 20, 30, 40]
y = [
    [0.054195801,0.161803246,0.230094592,0.269569238], #Bakery
    [0.128906329,0.579144637,1.141999006,1.479686419], #MarketBasket
    [0.120554527,0.631753842,1.799550931,3.309235096], #OnlineRetail
    [0.035054684,0.140363693,0.272323608,0.474229336], #RetailScanner
    [0.15321966,152.2377353,158276.9496,162075596.4]  #Average brute force
]

# Define colors and labels for each y row
row_colors = ['C0', 'C1', 'C2', 'C3', 'C4']
labels1 = ["Bakery-AP", "MarketBasket-AP", "OnlineRetail-AP", "RetailScanner-AP", "Brute Force"]

def plot_data(ax, x, y, labels, row_colors):
    legend_handles = []

    for y_list, color, label in zip(y, row_colors, labels):
        line, = ax.plot(x, y_list, color=color, linestyle='-', marker='', alpha=0.6)  # Drawing lines without markers
        for xi, yi in zip(x, y_list):
            scatter = ax.scatter(xi, yi, s=10*yi**(1/3), alpha=0.6, edgecolors="w", linewidth=0.5, c=color)
        legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label))

    ax.set_yscale('log')
    ax.legend(handles=legend_handles, loc='upper left')


fig, ax1 = plt.subplots(figsize=(6,5))  # Adjusted size for single plot

plot_data(ax1, x, y, labels1, row_colors)

ax1.set_xlabel('Number Of Unit Item')
ax1.set_ylabel('Time (second)')
ax1.set_title('Brute Force VS Apriori', fontsize=16)

plt.tight_layout()
plt.savefig('BF_AP_Time_Compare.png')
plt.show()
