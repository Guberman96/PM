import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.dates
import numpy
from matplotlib.dates import DAILY, DateFormatter, rrulewrapper, RRuleLocator
from Requirements_and_Projects import Milestone_List, task_end_dates, task_start_dates, tasks_duration, graph, reqlist, req

def CreateGantt():
    fdate = []
    sdate = []
    mdate = []

    for i in range(len(task_end_dates)):
        fdate.append(matplotlib.dates.date2num(task_end_dates[i])) #do this with the datetime.datetime objects instead(?)

    for i in range (len(task_start_dates)):
        sdate.append(matplotlib.dates.date2num(task_start_dates[i]))

    for i in range(len(fdate) and len(sdate)):
        mmdate = fdate[i]-sdate[i]
        mdate.append(mmdate)

    # Data
    # pos = numpy.arange(0.5,5.5,0.5) # pick up here
    pos = numpy.arange(len(Milestone_List))

    ylabels=req.Milestones
    customDates = mdate
    
    task_dates = {}
    for i,task in enumerate(Milestone_List):
        task_dates[task] = customDates[i]
 

    # Initialise plot
    fig= plt.figure(figsize=(20,6))
    ax = fig.add_subplot(111) #here, we want to be able to add as well a function  that 
    # creates n number of subplots for the number of milestones.
    
    # Plot the data
    for i in range(len(ylabels)): #pick up here and here
        ax.barh((i*1.0)+0.05, (mdate[i]), left=sdate[i], height=0.2, align='center', color='blue', alpha = 0.75)
        # ax.barh((i*pos), (mdate[i]), left=sdate[i], height=0.3, align='center', color='blue', alpha = 0.75)

    # Format the y-axis
    # ytick_spacing=len(Milestone_List)
    labelsy = plt.yticks(pos,ylabels)
    plt.setp(labelsy, rotation=30, fontsize = 7)
    
    # Format the x-axis
    ax.axis('tight')
    ax.set_ylim(ymin = -0.1, ymax = 4.5)
    ax.grid(color = 'g', linestyle = ':', )
    
    ax.xaxis_date() #Tell matplotlib that these are dates...
    
    rule = rrulewrapper(DAILY, interval=1)
    loc = RRuleLocator(rule)
    formatter = DateFormatter("%b %d %Y")
    
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_major_formatter(formatter)
    labelsx = ax.get_xticklabels(mdate)
    plt.setp(labelsx, rotation=30, fontsize=9)

    # Format the legend
    
    font = font_manager.FontProperties(size='small')
    ax.legend(loc=1,prop=font)
    
    # Finish up
    ax.invert_yaxis()
    fig.autofmt_xdate()
    plt.savefig('gantt.svg')
    plt.show()

# Data
# pos = numpy.arange(0.5,5.5,0.5) # pick up here
# pos = numpy.arange(len(Milestone_List))

# # ylabels=req.Milestones
# # customDates = mdate

# task_dates = {}
# for i,task in enumerate(req.Milestones):
#     task_dates[task] = customDates[i]

# figlist=[]
# # Initialise plot
# for i in range(len(reqlist)):
#     fig= plt.figure(figsize=(20,6))
#     figlist.append(fig)
#     ax = fig.add_subplot(111)

#     for fig in figlist:
#         # Format the y-axis
#         ytick_spacing=len(Milestone_List)
#         locsy, labelsy = plt.yticks(pos,ylabels)
#         plt.setp(labelsy, rotation=30, fontsize = 7)

#         # Format the x-axis
#         ax.axis('tight')
#         ax.set_ylim(ymin = -0.1, ymax = 4.5)
#         ax.grid(color = 'g', linestyle = ':', )

#         ax.xaxis_date() #Tell matplotlib that these are dates...

#         rule = rrulewrapper(DAILY, interval=1)
#         loc = RRuleLocator(rule)
#         formatter = DateFormatter("%b %d %Y")

#         ax.xaxis.set_major_locator(loc)
#         ax.xaxis.set_major_formatter(formatter)
#         labelsx = ax.get_xticklabels(mdate)
#         plt.setp(labelsx, rotation=30, fontsize=9)
#     # Plot the data
#         for i in range(len(ylabels)): 
#             ax.barh((i*1.0)+0.05, (mdate[i]), left=sdate[i], height=0.2, align='center', color='blue', alpha = 0.75)
#                 # ax.barh((i*pos), (mdate[i]), left=sdate[i], height=0.3, align='center', color='blue', alpha = 0.75)



    # Format the legend

# font = font_manager.FontProperties(size='small')
# ax.legend(loc=1,prop=font)

# # Finish up
# ax.invert_yaxis()
# fig.autofmt_xdate()
# plt.savefig('gantt.svg')
# plt.show()

# to plot graph, you need a graph friendly way to represent: task duration, beginning and end of tasks, 
# and tasks names corresponding to ylabel.
# initialize graph
# format graph: xaxis, xaxislabels and ticks, yaxis, yaxis labels and ticks, lines in the graph, color and thickness of bars, etc.
# Plot the graph
##Current problem: only the last lign in the CSV (ie the last iteration over the rows, appears in the graph. Important
# to generate all graphs for all different sets of Milestones for every requirement)
