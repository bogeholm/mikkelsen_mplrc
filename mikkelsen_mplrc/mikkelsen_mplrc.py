import matplotlib as mpl
import numpy as np
from cycler import cycler
import matplotlib.pyplot as plt
import seaborn.xkcd_rgb as xkcd

#import seaborn as sns

def paper(**kwargs):
    # Use seaborn
    import seaborn as sns
    sns.set_style('white')
    sns.set_style('ticks')

    # User can specify most parameters
    titlesize = kwargs.get('titlesize', 14)
    labelsize = kwargs.get('labelsize', 14)
    legendsize = kwargs.get('legendsize', 14)
    ticksize = kwargs.get('fontsize', 12)
    allfontsize = kwargs.get('allfontsize', None)
    if allfontsize is not None:
        titlesize = allfontsize
        labelsize = allfontsize
        legendsize = allfontsize

    # Matplotlib parameters
    # Use TeX
    mpl.rcParams['text.usetex']=True
    mpl.rcParams['text.latex.unicode']=True

    # https://stackoverflow.com/questions/17958485/matplotlib-not-using-latex-font-while-text-usetex-true
    #from matplotlib import rc as mplrc
    #mplrc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
    #mplrc('text', usetex=True)
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'Computer Modern'

    # Set the above
    mpl.rcParams['axes.titlesize'] = titlesize
    mpl.rcParams['axes.labelsize'] = labelsize
    mpl.rcParams['legend.fontsize'] = legendsize

    mpl.rcParams['xtick.labelsize'] = ticksize
    mpl.rcParams['ytick.labelsize'] = ticksize


def presentation():
    # Use seaborn
    import seaborn as sns
    sns.set_style('white')
    sns.set_style('ticks')

    # Matplotlib parameters
    # Use TeX
    mpl.rcParams['text.usetex']=True
    mpl.rcParams['text.latex.unicode']=True

    # https://stackoverflow.com/questions/17958485/matplotlib-not-using-latex-font-while-text-usetex-true
    #from matplotlib import rc as mplrc
    #mplrc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
    #mplrc('text', usetex=True)
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'Computer Modern'

    # Font size of labels and ticklabels
    fontsize = 22
    ticksize = 18
    # Set the above
    mpl.rcParams['axes.titlesize'] = fontsize
    mpl.rcParams['axes.labelsize'] = fontsize
    mpl.rcParams['legend.fontsize'] = fontsize

    mpl.rcParams['xtick.labelsize'] = ticksize
    mpl.rcParams['ytick.labelsize'] = ticksize

def mpldefaults():
    mpl.rcdefaults()

# Color options
def sRGB():
    # Define Apple colors - using sRGB
    blue = np.array([18, 187, 250]) / 255
    pink = np.array([255, 71, 123]) / 255
    orange = np.array([255, 163, 2]) / 255
    green = np.array([113, 221, 70]) / 255
    yellow = np.array([255, 211, 2]) / 255
    purple = np.array([170, 130, 255]) / 255
    black = np.array([0, 0, 0]) / 255

    #return [blue, pink, orange, green, yellow, purple, black]
    return [blue, pink, green, orange, purple, yellow, black]


def genericRGB():
    # Define Apple colors - using generic RGB
    blue = np.array([27, 172, 248]) / 255
    pink = np.array([251, 42, 104]) / 255
    orange = np.array([252, 146, 10]) / 255
    green = np.array([99, 219, 55]) / 255
    yellow = np.array([254, 204, 11]) / 255
    purple = np.array([153, 102, 255]) / 255
    black = np.array([0, 0, 0]) / 255

    #return [blue, pink, orange, green, yellow, purple, black]
    return [blue, pink, green, orange, purple, yellow, black]

def adobeRGB():
    # Define Apple colors - using Adobe RGB
    blue = np.array([106, 185, 248]) / 255
    pink = np.array([221, 73, 121]) / 255
    orange = np.array([223, 162, 38]) / 255
    green = np.array([153, 220, 85]) / 255
    yellow = np.array([243, 210, 50]) / 255
    purple = np.array([159, 129, 251]) / 255
    black = np.array([0, 0, 0]) / 255

    #return [blue, pink, orange, green, yellow, purple, black]
    return [blue, pink, green, orange, purple, yellow, black]

def damped_colors():
    # These are / will be slightly damped
    blue = xkcd['sky blue']
    pink = xkcd['pinkish red']
    green = xkcd['kelly green']
    orange = xkcd['pumpkin orange']
    purple = xkcd['purpley blue']
    yellow = xkcd['bright yellow']
    grey = xkcd['steel grey']

    return [blue, pink, green, orange, purple, yellow, grey]


def mikkelsen_colors():
    # TODO: Add this colormap;
    #   1) Redder red
    #   --> Just as in Hardwiring Happiness
    blue = xkcd['bright blue']
    pink = xkcd['reddish pink']
    green = xkcd['kelly green']
    orange = xkcd['pumpkin orange']
    purple = xkcd['purpley blue']
    yellow = xkcd['bright yellow']
    grey = xkcd['steel grey']

    return [blue, pink, green, orange, purple, yellow, grey]

# Bright darker blue - bright darker green - bright dark red - purple - orange - grey - light blue - light green - pink - yellow - black
def mikl2():
    # bdb - clear, dark blue
    cdb = xkcd['cerulean'] # 'cobalt',
    # cdg - clear, dark green
    cdg = xkcd['grass green'] # 'forest green', 'greenish', 'leaf green', 'apple green', 'medium green'
    # cdr - clear, dark red
    cdr = xkcd['scarlet']
    # prpl - purple
    prpl = xkcd['light purple'] # 'heliotrope',  'pastel purple', 'blue purple', 'purplish blue', 'violet'
    # orng - orange
    orng = xkcd['orange'] #xkcd['tangerine'] # 'yellow orange'
    # grey
    grey = xkcd['steel grey'] # 'steel grey'
    # lb- light blue
    lb = xkcd['baby blue'] # 'azure'
    # lg - light green
    # 'easter green', soft green', 'chartreuse', 'jade', 'faded green', 'teal green', 'pastel green', 'spring green'
    lg = "#2ecc71"# xkcd['easter green'] # 'lighter green', 'emerald', 'medium green', 'dark seafoam green',
    # pink
    pink = xkcd['shocking pink']# 'electric pink', 'pink', 'bright pink', 'hot pink', 'barbie pink'
    # ylw - yellow
    ylw = xkcd['lemon yellow'] # 'yellow', 'bright yellow', 'lemon yellow'
    # black
    black = xkcd['dark blue']# 'black'

    # List of all
    #allcls = [cdb, cdg, grey, cdr, prpl, orng, lb, lg, pink, ylw, black] # original
    allcls = [cdb, cdg, grey, cdr, prpl, orng, lb, pink, lg, ylw, black] # original

    # Return all
    return [c for c in allcls if c is not None]

def set_sRGB():
    plt.rc('axes', prop_cycle=(cycler('color', sRGB())))

def set_genericRGB():
    plt.rc('axes', prop_cycle=(cycler('color', genericRGB())))

def set_adobeRGB():
    plt.rc('axes', prop_cycle=(cycler('color', adobeRGB())))

def set_damped_colors():
    plt.rc('axes', prop_cycle=(cycler('color', damped_colors())))
