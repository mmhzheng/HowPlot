
from matplotlib import rcParams
from pylab import *


FIG_WIDTH = 3.3
FIG_HEIGHT= 2.5
FIG_GAP = 0.1

params = {
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
    'legend.frameon' : 'False',
    'legend.fancybox': True,

    #--- font
    'font.serif' : 'Times',
    'mathtext.fontset':'dejavuserif',
    'xtick.labelsize' : 12,
    'ytick.labelsize' : 12,
    'axes.titlesize' : 13,
    'axes.labelsize' : 13,
    'legend.fontsize' : 12,
    'legend.title_fontsize' : 12,
    'text.usetex' : True,
    'text.latex.preamble': r'\usepackage{libertine}\usepackage{fixltx2e}',
    'font.family': 'sans-serif',

    #--- axes
    'axes.linewidth' : 1.0,
    'lines.linewidth' : 1.8,
    'axes.prop_cycle' : (cycler(color = ['#CC6677', '#332288', '#DDCC77', '#117733', '#88CCEE']) + cycler(ls = ['-', '--', ':', '-.', ''])),

    #--- scatters
    # Set markers (style, color, no lines)
    # 'axes.prop_cycle' : (cycler('marker', ['o', 's', '^', 'v', '<', '>', 'd']) 
    #                 + cycler('color', ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00', '#845B97', '#474747', '#9e9e9e']) 
    #                 + cycler('ls', [' ', ' ', ' ', ' ', ' ', ' ', ' '])),
    # 'lines.markersize' : 3,
}
rcParams.update(params)