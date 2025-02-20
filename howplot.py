from matplotlib import rcParams
from pylab import *


FIG_WIDTH = 3.3
FIG_HEIGHT= 2.5
FIG_GAP = 0.1

line_params = {
    #--- Figure Size
    'figure.figsize' : [FIG_WIDTH, FIG_HEIGHT],
    'savefig.bbox' : 'tight',
    'savefig.pad_inches' : 0.05,

    #--- ticks
    'xtick.direction' : 'in',
    'xtick.minor.visible' : True,
    'ytick.major.size' : 3,
    'ytick.major.width' : 0.5,
    'ytick.minor.size' : 1.5,
    'ytick.minor.width' : 0.5,
    'ytick.direction' : 'in',
    'ytick.minor.visible' : True,

    #--- grid
    "axes.grid" : True,
    'grid.linewidth' : 0.5,
    'grid.linestyle' : '--',
    'grid.alpha': 0.5,
    'grid.color' : (0.5, 0.5, 0.5, 0.1),

    #--- legend
    'legend.frameon' : True,
    'legend.fancybox': False,
    'legend.framealpha' : 0.5,
    'legend.loc': 'best',

    #--- font
    'font.serif' : 'Times',
    'mathtext.fontset':'dejavuserif',
    'xtick.labelsize' : 12,
    'ytick.labelsize' : 12,
    'axes.titlesize' : 13,
    'axes.labelsize' : 13,
    'legend.fontsize' : 12,
    'legend.title_fontsize' : 8,
    'font.family': 'Times New Roman',
    'pdf.fonttype' : 42,
    'ps.fonttype' : 42,

    #--- axes
    'axes.linewidth' : 1.0,
    'axes.labelweight' : 'bold',
    'lines.linewidth' : 1.8,
    'axes.prop_cycle' : (cycler(color = ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00', '#845B97'])
                       + cycler(ls = ['-', '--', ':', '-.', ''])
                       + cycler('marker', ['o', 's', '^', 'v', '<'])),
    'lines.markersize' : 5,

}
