import matplotlib as mpl
#import seaborn as sns

def paper():
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
    fontsize = 18 # Font size
    ticksize = 14
    # Set the above
    mpl.rcParams['axes.titlesize'] = fontsize
    mpl.rcParams['axes.labelsize'] = fontsize
    mpl.rcParams['legend.fontsize'] = fontsize

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
