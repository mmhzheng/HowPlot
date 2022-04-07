from howplot import *

ROW_NUM = 1
COL_NUM = 4
rcParams['figure.figsize'] = [FIG_WIDTH*COL_NUM, FIG_HEIGHT*ROW_NUM]


subplot(ROW_NUM,COL_NUM, 1)
x = [10,20,30,40,50,60,70,80,90,100]
y1 = [20,40,10,20,40,10,20,40,10,90] 
y2 = [40,10,30,40,10,30,40,10,30,40]
plot(x, y1, label="line1")
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')

subplot(ROW_NUM,COL_NUM, 2)
plot(x, y2, label="line2")
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')

subplot(ROW_NUM,COL_NUM, 3)
plot(x, y2, label="line2")
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')

subplot(ROW_NUM,COL_NUM, 4)
plot(x, y2, label="line2")
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')

tight_layout()
# xlim(0.0, 9.0)
# ylim(0.0, 30.) 
savefig('figs/examples/subgraph.pdf')