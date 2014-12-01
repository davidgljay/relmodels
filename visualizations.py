import matplotlib.pyplot as plt
import numpy as np

def landscapemap(l, title=""):
    xset=[]
    yset=[]
    for i in xrange(0,len(l.model)-1):
        for j in xrange(0,len(l.model[i])-1):
            if (l.model[i][j]):
                xset.append(i)
                yset.append(j)
    fig, axes = plt.subplots(figsize=(12,12))
    axes.scatter(xset, yset)
    axes.set_xlim([-1,max(xset)+1])
    axes.set_ylim([-1,max(yset)+1])
    axes.set_title(title)
    return axes

def linegraph(nums, title=""):
    fig, axes = plt.subplots(figsize=(16,8))
    axes.plot(xrange(0,len(nums)), nums)
    axes.set_title(title)

from itertools import cycle

def getx(xy):
    return xy[0]

def gety(xy):
    return xy[1]

def phasespacemap(values, dividers, title="", sort = True, mode="delta"):
    if mode == "delta":
        sets = [[]]
    elif mode=="equals":
        sets = []
    for d in dividers:
        sets.append([])
    
    if (mode == "delta"):
        #Assign points to sets based on which divider they're a part of
        for i in xrange(0,len(values)-1):
            if sort:
                values[i].sort()
            for j in xrange(0,len(values[i])-1):
                for k in xrange(0,len(dividers)):
                    val = values[i][j]
                    if k == len(dividers):
                        if val > dividers[-1]:
                            sets[k].append((i,j))
                    elif k == 0:
                        if val < dividers[k]:
                            sets[k].append((i,j))
                    elif val <= dividers[k] and val >= dividers[k-1]:
                        sets[k].append((i,j))
    elif (mode=="equals"):
        for i in xrange(0,len(values)-1):
            if sort:
                values[i].sort()
            for j in xrange(0,len(values[i])-1):
                for k in xrange(0,len(dividers)):
                    val = values[i][j]
                    if val == dividers[k]:
                            sets[k].append((i,j))
                            
    #Set up an array of colors
    colors=cycle(["b","g","r","m","c","y","k","grey", "black"])
    
    fig, axes = plt.subplots(figsize=(15,15))
    axes.set_title(title)
    #Plot each set as s different color
    maxx = 0
    maxy = 0
    for i in xrange(0,len(sets)-1):
        xset = []
        yset = []
        if len(sets[i]) > 0:
            xset=map(getx,sets[i])
            yset=map(gety,sets[i])
            c = colors.next()
            if mode == "delta":
                if i < len(dividers):
                    lbl = "< " + str(dividers[i])
                else:
                    lbl = "> " + str(dividers[-1])
            elif mode == "equals":
                 lbl = str(dividers[i])
            axes.scatter(xset, yset, color=c, label=lbl, marker=',', s=1 )
            axes.legend(loc=1)
            maxx = max([maxx, max(xset)])
            maxy = max([maxy, max(yset)])
    axes.set_xlim([-1,maxx+1])
    axes.set_ylim([-1,maxy+1])
    plt.show()

