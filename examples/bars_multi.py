from sympy import rotations
from howplot import *


rcParams.update(bar_params)

data1 = [30, 25, 50, 50]
data2 = [20, 25, 80, 10]
data3 = [10, 25, 30, 30]

x_labels = ["AAA", "BBB", "CC", "DD"]
BAR_WIDTH = 0.25
CLASS_NUM = 3 # data 1, 2, 3
index = np.arange(len(x_labels))
xticks(ticks=index + CLASS_NUM * BAR_WIDTH / CLASS_NUM, labels=x_labels, rotation=0)
bar(index, data1, width=BAR_WIDTH, hatch='//', label='data1')
bar(index+BAR_WIDTH, data2, width=BAR_WIDTH, hatch='\\\\', label='data2')
bar(index+BAR_WIDTH*2, data3, width=BAR_WIDTH, hatch='--', label='data3')
legend()
xlabel('Memory Usage (MB)')
# Set the y axis label of the current axis.
ylabel('F1 Score')
savefig('figs/examples/bars_multi.pdf')