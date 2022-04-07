from cProfile import label
import numpy as np
import matplotlib.pyplot as plt



with plt.style.context(['science', 'muted']):
    fig, ax = plt.subplots()
    data = [[30, 25, 50, 20],
            [40, 23, 51, 17],
            [35, 22, 45, 19]]
    x_labels = ["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"]
    x = np.array([i for i in range(len(x_labels))])
    ax.set_xticks([i for i in range(len(x_labels))])
    ax.set_xticklabels(x_labels, rotation = 30)
    ax.bar(x, data[0], width = 0.5, hatch='/', label='bar1')
    ax.bar(x, data[1], bottom=data[0], width = 0.5, hatch='\\', label='bar2')
    ax.bar(x, data[2], bottom=data[1], width = 0.5, hatch='-', label='bar3')
    ax.legend()
    ax.autoscale(tight=True) 
    ax.set_xlabel('Memory Usage (MB)')
    # Set the y axis label of the current axis.
    ax.set_ylabel('F1 Score')
    fig.savefig('figs/examples/bars_stack.pdf')