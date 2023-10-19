import matplotlib.pyplot as plt
# Data
x = [10, 20, 30, 40]
y = [
    ###################################### plot 1
    [0.250600457, 281.7311803, 311763.8944, 329242195.8], ###Bakery-BF
    [0.087643862, 0.271992207, 0.510766745, 0.515302896],  ###Bakery-AP
    [0.147943139, 127.7346375, 165019.0924,193252510.4],###Groceries-BF
    [0.23379612, 3.043438196, 9.407475948,16.80596232], ###Groceries-AP
    [0.321838021, 318.1824235, 407672.5314, 474769461.2], ###TVShows-BF
    [0.174072981, 0.981793165, 2.050226927, 3.4315238], ###TVShows-AP
    
    ###################################### plot 2
    [0.230966568,215.8093249,271091.2453,308674826.6], ###MarketBasket-BF
    [0.118185997, 0.653516054, 1.247218847,1.691363096], ###MarketBasket-AP
    [0.374132633,467.366833,665317.5665,855210679.7], ###OnlineRetail-BF
    [0.213912964, 1.648180962, 5.721241951,12.38631392],###OnlineRetail-AP
    [1.269995093,1457.855089,1845026.937,2128364646], ###RetailScanner-BF
    [0.200621128, 1.036177874, 2.230133057, 4.227671146]###RetailScanner-AP
]

# Define colors and labels for each y row
row_colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5']
labels1 = ["Bakery-BF", "Bakery-AP", "Groceries-BF", "Groceries-AP", "TVShows-BF", "TVShows-AP"]
labels2 = ["MarketBasket-BF", "MarketBasket-AP", "OnlineRetail-BF", "OnlineRetail-AP", "RetailScanner-BF", "RetailScanner-AP"]
y1 = y[:6]  # First four rows
y2 = y[6:]  # Next rows

def plot_data(ax, x, y, labels, row_colors):
    legend_handles = []

    for y_list, color, label in zip(y, row_colors, labels):
        for xi, yi in zip(x, y_list):
            scatter = ax.scatter(xi, yi, s=10*yi**(1/3), alpha=0.6, edgecolors="w", linewidth=0.5, c=color)
        legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label))

    ax.set_yscale('log')  # Set y-axis to logarithmic scale
    ax.legend(handles=legend_handles, loc='upper left')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

plot_data(ax1, x, y1, labels1, row_colors)
plot_data(ax2, x, y2, labels2, row_colors)

# ax1.set_title('Brute Force VS Apriori')
ax1.set_xlabel('Bakery & Groceries & TV Shows')
ax2.set_xlabel('Market Basket & Online Retail & Retail Scanner')
fig.suptitle('Brute Force VS Apriori', fontsize=16)

plt.tight_layout()
plt.savefig('BF_AP_Time_Compare.png')
plt.show()
