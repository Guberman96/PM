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

    #Start plotting the graph
    fig, ax = plt.figure() #Instantiate graph class, now called fig.
    fig, ax = fig.add_subplot(111) #Use the class method add subplot, call it ax.
    ax = ax.xaxis_date() #Wrong right now: xticks do not plot on the correct dates.
    ax = plt.hlines (df.Name, df.Start, df.End)
    plt.xticks(rotation=45)
    
    fig.autofmt_xdate()
    plt.grid(True)
    plt.show()