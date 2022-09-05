from scrape import avg
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#This is the main file of the 'Expansion' (Rewrite) of the original radish.ai https://github.com/konuketo/radish.ai

averages = list(avg(float(input()), float(input())))
color = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']

print(averages[0])
print(averages[3])
# CITY, CARROTS, CABBAGE, WHEAT, CORN, COTTON, LETTUCE, 
xvals = [averages[0], 12.7778, 15.5556, 21, 29.4444, 21, 13]
yvals = [averages[3]*4, 3.6296, 3.5710, 2.7390, 1.7397, 7.112, 3.5714]

labels = ['City', 'Carrots', 'Cabbage', 'Wheat', 'Corn', 'Cotton', 'Lettuce']

custom = [ Line2D([], [], marker='.', color=i, linestyle='None', markersize=15) for i in color]

plt.scatter(xvals, yvals, s=50, c=color)
plt.legend(custom, labels, fontsize=10)

plt.xlim((0, 40))
plt.ylim((0, 10))

plt.show()