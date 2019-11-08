import seaborn as sns

def plot_1(x, y, kind, hue, data):
    '''Function returns a seaborn catplot.
       Input: All strings plot_1(x, y, hue, kind of plot, dataframe)
       Returns a seaborn plot object.'''
    sns.set(style='whitegrid')
    ax = sns.catplot(x=x, y=y
                    , kind=kind, hue=hue, legend=False
                    , data=data)
    ax.add_legend(title=(str(hue)))
    ax.fig.suptitle('Sleep pattern by ' +str(hue))
    ax.fig.set_size_inches(9.5, 3.5)
    return ax