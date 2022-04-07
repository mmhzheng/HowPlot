from howplot import *

rcParams.update(line_params)

x = [10,20,30,40,50,60,70,80,90,100]
y1 = [20,40,10,20,40,10,20,40,10,90] 
y2 = [40,10,30,40,10,30,40,10,30,40]
plot(x, y1, label="line1")
plot(x, y2, label="line2")
# xlim(0.0, 9.0)
# ylim(0.0, 30.) 
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='upper center', bbox_to_anchor=(0.5, 1.20), ncol=2)
savefig('figs/examples/lines_out.pdf')


