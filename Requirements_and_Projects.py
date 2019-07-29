import re
from datetime import datetime as dt
from datetime import timedelta
from datetime import date
import csv
import datetime as dt
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.dates
import numpy
from matplotlib.dates import DAILY, DateFormatter, rrulewrapper, RRuleLocator

# import Visualization

class Requirement: #Create a class Requirements to hich store information on project requirements.
    "This class is meant to record requirements for a given project"
    def __init__ (self, Reqnum: int, Reqname: str, Source:str, Deadline: dt, Milestones: list):
        self.Requirement_number = Reqnum
        self.Source = Source
        self.Requirement_name = Reqname
        self.Deadline = Deadline
        self.Milestones = Milestones

    def addMilestones (self, Milestone: str):
        self.Milestones.append(Milestone)

class Project: #Create a project class, which is a list of requirements.
    "This class is meant to record projects"
    def  __init__ (self, Requirements: [Requirement]):
        self.Requirements = Requirements

    def addProjectsComplexity(self, Requirement):
        self.Requirements.append(Requirement)

reqlist = [] #create a list where we'll store every requirement.
Project1 = Project(reqlist)

# task_start_dates = []
# task_end_dates = []
# tasks_duration = []

sdate = []
fdate = []
mdate=[]

with open ('Requirements_and_Milestones.csv', 'r') as PMfile:
    REQAGAIN = csv.reader(PMfile, delimiter=',')
    for row in REQAGAIN: #iterate over every row in the CSV. Each row is a requirement.
        Milestone_List = []
        Milestone_Start_List = []
        Milestone_Finish_List = []
        for i in range (4, len(row), 3): #iterate over every third cell in every row, starting  at index 4.
            Milestone_Start_List.append(row[i])
        for i in range (5, len(row), 3): #iterate over every third cell in every row, starting  at index 5.
            Milestone_Finish_List.append(row[i])
        for i in range (6, len(row), 3): #iterate over every third cell in every row, starting  at index 6.
            Milestone_List.append(row[i])
        req = Requirement(row[0], row[1], row[2], row[3], Milestone_List)
        reqlist.append(req)           
        task_start_dates = []
        task_end_dates = []
        tasks_duration = []
        for startdates in Milestone_Start_List:
            if Milestone_Start_List[0] == "M1 Start": #check back
                continue
            task_start_date = dt.datetime.strptime(startdates, '%m-%d-%Y').date()
            task_start_dates.append(task_start_date)
        for enddates in Milestone_Finish_List:
            if Milestone_Finish_List[0] == "M1 Finish":
                continue
            task_end_date = dt.datetime.strptime(enddates, '%m-%d-%Y').date()
            task_end_dates.append(task_end_date)
        for i in range(len(task_end_dates)):
            fdate.append(matplotlib.dates.date2num(task_end_dates[i])) #convert datetime object to matplotlib date. Append to flist.
        for i in range(len(task_start_dates)):
            sdate.append(matplotlib.dates.date2num(task_start_dates[i]))#convert datetime object to matplotlib date. Append to slist.
        for i in range(len(task_end_dates) and len(task_start_dates)):
            tasks_length = task_end_dates[i]- task_start_dates[i]
            tasks_duration.append(tasks_length)
            # print(tasks_length)
        for i in range(len(fdate) and len(sdate)):
            mmdate = fdate[i]-sdate[i]
            mdate.append(mmdate)
        graph = zip(tasks_duration, Milestone_List)
        for req in reqlist:
            ylabels=req.Milestones
            customDates = mdate

# Data
# pos = numpy.arange(0.5,5.5,0.5) # pick up here
pos = numpy.arange(len(Milestone_List))

# ylabels=req.Milestones
# customDates = mdate

task_dates = {}
for i,task in enumerate(req.Milestones):
    task_dates[task] = customDates[i]

figlist=[]
# Initialise plot
for i in range(len(reqlist)):
    fig= plt.figure(figsize=(20,6))
    figlist.append(fig)
    ax = fig.add_subplot(111)
    for fig in figlist:
        # Format the y-axis
        ytick_spacing=len(Milestone_List)
        locsy, labelsy = plt.yticks(pos,ylabels)
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
# Plot the data
        for i in range(len(ylabels)): 
            ax.barh((i*1.0)+0.05, (mdate[i]), left=sdate[i], height=0.2, align='center', color='blue', alpha = 0.75)
            # ax.barh((i*pos), (mdate[i]), left=sdate[i], height=0.3, align='center', color='blue', alpha = 0.75)



    # Format the legend

font = font_manager.FontProperties(size='small')
ax.legend(loc=1,prop=font)

# Finish up
ax.invert_yaxis()
fig.autofmt_xdate()
plt.savefig('gantt.svg')
plt.show()
#next functions: web app(?) where you would be able to visualize the gantt charts, edit the requirement excel sheet (keeping track)
#can practice server and DB design doing this. Send automatic e-mails and reminders, etc, keep track of all milestones, eveents, changes, etc.
#start looking into how you could automatically populate trello boards with this.