import re
import time
from datetime import datetime as dt
from datetime import timedelta
from datetime import date
import csv
import datetime as dt

class ReqEvent:
    def __init__ (self, ReqEventName: str, ReqEventStart: dt, ReqEventEnd: dt):
        self.ReqEventName=ReqEventName
        self.ReqEventStart=ReqEventStart
        self.ReqEventEnd=ReqEventEnd

class Requirement: #Create a class Requirements to store information on project requirements.
    "This class is meant to record requirements for a given project"
    def __init__ (self, Reqnum: int, Reqname: str, Source:str, Deadline: dt, Milestones: [ReqEvent]): #i think it would be better ot have this as a list of tuples with duration:milestone
        self.Requirement_number = Reqnum
        self.Source = Source
        self.Requirement_name = Reqname
        self.Deadline = Deadline
        self.Milestones = Milestones

class Project: #Create a project class, which is a list of requirements.
    "This class is meant to record projects"
    def  __init__ (self, Requirements: [Requirement]):
        self.Requirements = Requirements

    def addProjectsComplexity(self, Requirement):
        self.Requirements.append(Requirement)

reqlist = [] #create a list where we'll store every requirement.

with open ('Requirements_and_Milestones.csv', 'r') as PMfile:
    REQAGAIN = csv.reader(PMfile, delimiter=',')
    next(REQAGAIN)
    for row in REQAGAIN: #iterate over every row in the CSV. Each row is a requirement.
        ReqEvent_List = [] #for each row, create a list of ReqEvents
        Event_Name_List = []
        Event_Start_List = []
        Event_Finish_List = []

        for t in range (4, len(row), 3): #iterate over every third cell in every row, starting  at index 4.
            Event_Start_List.append(row[t])
        for r in range (5, len(row), 3): #iterate over every third cell in every row, starting  at index 5.
            Event_Finish_List.append(row[r])
        for z in range (6, len(row), 3): #iterate over every third cell in every row, starting  at index 6.
            Event_Name_List.append(row[z])
        
        req = Requirement(row[0], row[1], row[2], row[3], ReqEvent_List)
        reqlist.append(req)
        for i in range(len(Event_Name_List)):
            Event = ReqEvent(Event_Name_List[i], Event_Start_List[i], Event_Finish_List[i])
            ReqEvent_List.append(Event)