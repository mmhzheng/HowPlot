from howplot import *

data = [[30, 25, 50, 20],
    [40, 23, 51, 17],
    [35, 22, 45, 19]]
X = np.arange(4)
bar(X, data[0], width = 0.25, hatch='/',  label='bar1')
bar(X+1, data[1], width = 0.25, hatch='\\', label='bar2')
bar(X+1, data[2], width = 0.25, hatch='-',  label='bar3')
legend()
xlabel('Memory Usage (MB)')
# Set the y axis label of the current axis.
ylabel('F1 Score')
savefig('figs/examples/bars.pdf')