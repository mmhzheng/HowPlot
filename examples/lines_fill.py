import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)  
from howplot import *

rcParams.update(line_params)

def perc(data):
    median = np.zeros(data.shape[1])
    perc_25 = np.zeros(data.shape[1])
    perc_75 = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
        perc_25[i] = np.percentile(data[:, i], 25)
        perc_75[i] = np.percentile(data[:, i], 75)
    return median, perc_25, perc_75

x = [10,20,30,40,50,60,70,80,90,100]
# There can be many data for each xi, here we only list three, x, upper and lower.
y = np.array([20,40,10,20,40,10,20,40,10,90])
upper = y + 35
lower = y - 35

data = np.array([y, upper, lower])
med_low_mut, perc_25_low_mut, perc_75_low_mut = perc(data)

plot(x, y, label="line1")
fill_between(x, perc_25_low_mut, perc_75_low_mut, alpha=0.25, linewidth=0, color='#B22400') # '#006BB2'


# xlim(0.0, 9.0)
# ylim(0.0, 30.) 
xlabel("Memory Usage (MB)")
ylabel("F1 Score")
legend(loc='best')
# Make the minor ticks and gridlines show.
minorticks_on()
savefig('figs/examples/lines_fill.pdf')