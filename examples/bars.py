from sympy import rotations
from howplot import *


rcParams.update(bar_params)

data = [30, 25, 50, 73]
x_labels = ["AAA", "BBB", "CC", "DD"]
WIDTH = 0.6
xticks(ticks=range(len(x_labels)), labels=x_labels, rotation=0)
bar(range(len(x_labels)), data, width=WIDTH, hatch='//', label='bar1')
legend()
xlabel('Memory Usage (MB)')
# Set the y axis label of the current axis.
ylabel('F1 Score')
savefig('figs/examples/bars.pdf')