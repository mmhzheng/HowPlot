import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)  
from howplot import *


rcParams.update(bar_params)


WIDTH = 0.6

data1 = [30, 25, 50, 50]
data2 = [20, 25, 80, 10]
data3 = [10, 25, 30, 30]

x_labels = ["AAA", "BBB", "CC", "DD"]
index = np.arange(len(x_labels))
xticks(ticks=index, labels=x_labels, rotation=0)
bar(index, data1,  width=WIDTH, hatch='//', label='data1')
bar(index, data2, bottom=np.array(data1), width=WIDTH, hatch='\\\\', label='data2')
bar(index, data3, bottom=np.array(data1) + np.array(data2), width=WIDTH, hatch='--', label='data3')

legend()
xlabel('Memory Usage (MB)')
# Set the y axis label of the current axis.
ylabel('F1 Score')
savefig('figs/examples/bars_stack.pdf')