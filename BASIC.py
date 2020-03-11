##	Create a python script (any name) and use your project dataset to generate many figures (10+)
# showing data with at least *3* features at a time, leveraging things like:
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as snb

wine_dataset= pd.read_csv('wine.data', sep =',', header=0)

# a.	multiple plots on the same figure
os.makedirs('visualisation/1-multiple_plot', exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(8,8))

axes[0][0].plot(wine_dataset['Alcohol'], wine_dataset['Malic_acid'])
axes[0][1].plot(wine_dataset['Alcohol'], wine_dataset['Flavanoids'])
axes[1][0].scatter(wine_dataset['Total_phenols'], wine_dataset['Color_intensity'],
                   label=f'Total_phenols to Color_intensity', color='green', marker='o', edgecolors='w', alpha=0.7)
axes[1][1].scatter(wine_dataset['Total_phenols'], wine_dataset['Hue'],
                   label=f'Total_phenols to Hue', color='red', marker='v', edgecolors='r', alpha=0.5)

axes[0][0].set_title(f'Alcohol to Malic Acid, Flavanoids')
axes[0][0].set_xlabel('Alcohol')
axes[0][0].set_ylabel('Malic Acid')
axes[0][1].set_xlabel('Alcohol')
axes[0][1].set_ylabel('Flavanoid')
axes[1][0].set_xlabel('Total_phenols')
axes[1][0].set_ylabel('Color_intensity')
axes[1][1].set_xlabel('Total_phenols')
axes[1][1].set_ylabel('Hue')
#axes.set_title(f'Alcohol comparisons')
#axes.legend()
plt.savefig(f'visualisation/1-multiple_plot/multiplot_subplot.png', dpi=300)
plt.close()


# b.	multiple plots on the same axes
os.makedirs('visualisation/2-multiple_plot_axes', exist_ok=True)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
axes.scatter(wine_dataset['Alcohol'], wine_dataset['Total_phenols'], alpha=0.7, label='Total Phenols')
axes.scatter(wine_dataset['Alcohol'], wine_dataset['Color_intensity'], alpha=0.7, label='Color Intensity')
axes.scatter(wine_dataset['Alcohol'], wine_dataset['Malic_acid'], alpha=0.7, label='Malic Acid')

axes.set_xlabel('Alcohol')
axes.set_ylabel('Total Phenols / Color Intensity')
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(f'visualisation/2-multiple_plot_axes/multiplot_scatter.png', dpi=300)

plt.close()


# c.	colours, markers, sizes, shapes, hue, etc...
# d.	3D visualizations
os.makedirs('visualisation/3-3D_plots', exist_ok=True)

winery_1 = wine_dataset[wine_dataset['Winery'] == 1]
winery_2 = wine_dataset[wine_dataset['Winery'] == 2]
winery_3 = wine_dataset[wine_dataset['Winery'] == 3]
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
line1 = axes.scatter(winery_1['Alcohol'], winery_1['Hue'], winery_1['Color_intensity'])
line2 = axes.scatter(winery_2['Alcohol'], winery_2['Hue'], winery_2['Color_intensity'])
line3 = axes.scatter(winery_3['Alcohol'], winery_3['Hue'], winery_3['Color_intensity'])
axes.legend((line1, line2, line3), ('Winery_1', 'Winery_2', 'Winery_3' ))
axes.set_xlabel('Alcohol')
axes.set_ylabel('Hue')
axes.set_zlabel('Color_intensity')
plt.savefig('visualisation/3-3D_plots/wine_scatter_3d.png')

plt.close()

# e.	use any library you want!
# f.	You can determine how you choose the columns used based on conceptual understanding of your dataset
# or generating all possible combinations!
# g.	push your script and make sure the figures have titles, axis labels, and legends if applicable.
# (Pushing the images is optional, I recommend pushing the most interesting ones at least)
