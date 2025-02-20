
from matplotlib import rcParams, cycler
import numpy as np
FIG_GAP = 0.1

line_params = {
    #--- Figure Size
    'figure.figsize' : (4, 3),
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
    'ytick.minor.visible' : False,

    #--- grid
    "axes.grid" : True,
    'grid.linewidth' : 0.5,
    'grid.linestyle' : '--',
    'grid.alpha': 0.5,
    'grid.color' : (0.5, 0.5, 0.5, 0.1),

    #--- legend
    'legend.frameon' : True,
    'legend.fancybox': False,
    'legend.framealpha' : 0.3,
    'legend.loc': 'best',

    #--- font
    'font.serif' : 'Times',
    'mathtext.fontset':'dejavuserif',
    'xtick.labelsize' : 14,
    'ytick.labelsize' : 14,
    'axes.titlesize' : 15,
    'axes.labelsize' : 15,
    'legend.fontsize' : 15,
    'legend.title_fontsize' : 14,
    'font.family': 'Arial',
    'pdf.fonttype' : 42,
    'ps.fonttype' : 42,

    #--- axes
    'axes.linewidth' : 1.0,
    'axes.labelweight' : 'bold',
    'lines.linewidth' : 1.8,
    'axes.prop_cycle': (
        cycler(color=['#0C5DA5', '#FF2C00', '#FFD700', '#00B945', '#FF9500', '#800080']) +
        cycler(ls=['-',  '-', ':', '--', ':', '-.']) +  # Ensure this has 6 styles
        cycler(marker=['o', 's', '^', 'v', 'D', 'p'])
    ),
    'lines.markersize' : 5,
}


cdf_params = {
    #--- Figure Size
    'figure.figsize' : (4, 3),
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
    'xtick.labelsize' : 11,
    'ytick.labelsize' : 11,
    'axes.titlesize' : 12,
    'axes.labelsize' : 12,
    'legend.fontsize' : 11,
    'legend.title_fontsize' : 8,
    'font.family': 'Arial',
    'pdf.fonttype' : 42,
    'ps.fonttype' : 42,

    #--- axes
    'axes.linewidth' : 1.0,
    'axes.labelweight' : 'bold',
    'lines.linewidth' : 1.8,
    'axes.prop_cycle': (
        cycler(color = ['#00B945', '#FFD700', '#FF9500', '#800080', '#0C5DA5',
                        '#FF2C00', '#008080', '#FF1593', '#000080', '#FF69B4',
                        '#008000', '#FF4500', '#0000FF', '#FF00FF', '#008080',
                        '#800000', '#00FFFF', '#808000', '#800080', '#00FF00']
              ) +
        cycler(ls    = ['-',  '-', ':', '--', ':',
                        '-.', '-',  '-', ':', '--',
                        '-.', '-',  '-', ':', '--',
                        '-.', '-',  '-', ':', '--',
                        ])
    ),
    'lines.markersize' : 5,
}


def cumulative_distribution(data_dict):
    # 提取字典中的值
    values = list(data_dict.values())

    # 计算累计分布
    sorted_values = np.sort(values)
    cumulative = np.cumsum(sorted_values)
    cumulative_percentage = cumulative / cumulative[-1]
    return sorted_values, cumulative_percentage
