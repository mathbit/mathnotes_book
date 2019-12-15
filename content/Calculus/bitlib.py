def formatAxes(ax):
    '''
    Axes as crosses, adds arrows and and x and y.
    '''

    #-- Set axis spines at 0
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')

    # Hide the other spines...
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    #-- Decorate the spins
    arrow_length = 2 # In points

    # X-axis arrow
    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(arrow_length, 0), textcoords='offset points',
                ha='left', va='center',
                arrowprops=dict(arrowstyle='<|-', fc='black'))

    # Y-axis arrow
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(0, arrow_length), textcoords='offset points',
                ha='center', va='bottom',
                arrowprops=dict(arrowstyle='<|-', fc='black'))
