
from howplot import *

x = [10,20,30,40,50,60,70,80,90,100]
y1 = [20,40,10,20,40,10,20,40,10,90] 
y2 = [40,10,30,40,10,30,40,10,30,40]
y3 = [10,30,40,10,30,40,40,40,40,40]
plot(x, y1, label="line1")
plot(x, y2, label="line2")
plot(x, y3, label="line3")
# xlim(0.0, 9.0)
# ylim(0.0, 30.) 
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')
# Make the minor ticks and gridlines show.
minorticks_on()
savefig('figs/examples/lines.pdf')