import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df[(df['value'] < df['value'].quantile(0.975)) & (df['value'] > df['value'].quantile(0.025))] 


def draw_line_plot():
    # Draw line plot
    fig = df.plot()

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/201')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.legend(['Value in millions'])
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean().unstack()
    df_bar.rename(columns={1:'January',
                               2:'February',
                               3:'March',
                               4:'April',
                               5:'May',
                               6:'June',
                               7:'July',
                               8:'August',
                               9:'September',
                               10:'October',
                               11:'November',
                               12:'December'}, inplace=True)

    # Draw bar plot
    fig = grouped.plot(kind='bar', figsize=(10, 6))
    # Set plot title and axis labels
    fig.set_title('Average Daily Page Views per Month (2016-2021)')
    fig.set_xlabel('Years')
    fig.set_ylabel('Average Page Views')
    
    # Set legend title and position
    fig.legend(title='Months', loc='upper left')
    
    # Show plot
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt1 =sns.boxplot(x = "year", y = "value", data = df_box)
    plt1.set_title("Year-wise Box Plot (Trend)")
    plt1.set_xlabel('Year')
    plt1.set_ylabel('Page Views')

    plt2=sns.boxplot(x='month',y='value',data=df_box)
    plt2.set_title("Month-wise Box Plot (Trend)")
    plt2.set_xlabel('Month')
    plt2.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
