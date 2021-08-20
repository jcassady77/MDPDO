#Stores all simulation data

import tkinter
from tkinter import *
import time
import csv

#Initializing Variables
simTime = 1000
agentSize = 5
canvasWidth = 500
canvasHeight = 500
sim = tkinter.Tk()
sim.geometry("500x500")
canvas = Canvas(sim, width = canvasWidth, height = canvasHeight)
canvas.pack()

#Agents
agents = [  [[100,100],[0.1,0.1]],
            [[10,10], [0.2,0.2]],
            [[250,250],[0,0.5]]
            ]
with open("positions.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
    for i in range(simTime):
        canvas.delete('all')
        tempArr = []
        for agent in agents:
            tempArr.append([agent[0][0], agent[0][1]])
            canvas.create_oval(agent[0][0]-agentSize, (canvasHeight - agent[0][1])-agentSize, agent[0][0]+agentSize, (canvasHeight - agent[0][1])+agentSize)
            agent[0][0] += agent[1][0]
            agent[0][1] += agent[1][1]
        writer.writerow(tempArr)
        print(tempArr)
        sim.update()
        time.sleep(0.01)
    
sim.mainloop()