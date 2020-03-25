from os import path
from Parse_Requirements import reqlist, ReqEvent
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

for req in reqlist:
    Task = []
    Task_Start = []
    Task_Ends = []
    Task_Length = []
    for ReqEvent in req.Milestones:
        Task.append(ReqEvent.ReqEventName)
        Task_Start.append(ReqEvent.ReqEventStart)
        Task_Ends.append(ReqEvent.ReqEventEnd)
        TL = pd.to_datetime(ReqEvent.ReqEventEnd) - pd.to_datetime(ReqEvent.ReqEventStart)
        Task_Length.append(TL)

    df = pd.DataFrame({'Name': Task, 'Start': Task_Start, 'End': Task_Ends, 'Length': Task_Length})
    print(df)

    # #Start plotting the graph
    DayFormatter = mdt.DateFormatter('%m/%d/%Y')
    outpath = "Users/germanandresguberman/Desktop/Poopalassi"
    fig = plt.figure() #Instantiate graph class, now called fig.
    ax = fig.add_subplot(111) #Use the class method add subplot, call it ax.
    ax.xaxis.set_minor_locator(mdt.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(DayFormatter)
    ax.xaxis.set_major_locator(mdt.DayLocator(interval=3))
    ax = ax.xaxis_date() #Wrong right now: xticks do not plot on the correct dates.
    ax = plt.hlines (df.Name, pd.to_datetime(df.Start), pd.to_datetime(df.End))
    fig.autofmt_xdate()
    plt.xticks(rotation=50)    
    plt.grid(True)
    plt.show()
    # plt.savefig(path.join(outpath, "Req Gantt Chart{0}.png"))

    #It works. Need to figure out how to save it dynamically. 
    #Change some of the colors to make it more appealing.
    #Future: need to figure out how to display on web-app.""