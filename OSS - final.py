#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy
from IPython.display import display
from statistics import mean
import schedule
processNum = int(input('Hello! Welcome to your scheduler,\n Please enter the number of processes:'))


# In[47]:


arrival = []
burst = []
p = []
tat1_avg = 0
tat2_avg = 0 
tat3_avg = 0
wt1_avg = 0
wt2_avg = 0
at3_avg = 0
rt1_avg = 0 
rt2_avg = 0 
rt3_avg  = 0
util1 = 0
util2 = 0
util3 = 0
t1 = 0
t2 = 0
t3 = 0
for i in range(0,processNum):
    arrival.append(int(input('Process {0} Arrival Time:'.format(i+1))))
    burst.append(int(input('Process {0} Burst Time:'.format(i+1))))
    p.append('P{0}'.format(i+1))
    print("")
    i+=1


# In[48]:



data = {'Process' : p,
        'Arrival Time': arrival,
        'Burst Time' : burst
       }


# In[49]:


df = pd.DataFrame(data)


# In[50]:


df


# In[51]:



def fcfs():
        df1 = df.sort_values(by='Arrival Time')
        df1 = df1.reset_index(drop = True)
        arrival = df1['Arrival Time']
        burst = df1['Burst Time']
        tat =[]
        wt = []
        rt = []
        start = []
        comp = []
        idle_time = 0
        for i in range(len(p)):
            if(i==0):
                start.append(arrival[i])
                comp.append(burst[i] + arrival[i])
                idle_time = start[i]
                
            else:
                if(arrival[i]<comp[i-1]):
                    start.append(comp[i-1])
                    comp.append(comp[i-1] + burst[i])
                else:
                    start.append(arrival[i])
                    comp.append(arrival[i] + burst[i])
            
            tat.append(comp[i]-arrival[i])
            wt.append(tat[i]-burst[i])
            rt.append(start[i]-arrival[i])
            if(i>0):
                idle_time += (start[i] - comp[i-1])
            i+=1
        tat1_avg = mean(tat)
        wt1_avg = mean(wt)
        rt1_avg = mean(rt)
        util1 = (comp[len(p)-1] - idle_time)/comp[len(p)-1] * 100
        t1 = len(p)/(comp[len(p)-1] - start[0])
        arrival = df['Arrival Time']
        burst = df['Burst Time']
        df1['Start Time'] = start
        df1['Compeletion Time'] = comp
        df1['Turn Around Time'] = tat
        df1['Waiting Time'] = wt
        df1['Response Time'] = rt
        print("FCFS algorithm will be:\n")
        display(df1)
        tat_avg = mean(tat)
        
        


# In[52]:


print(fcfs())


# In[ ]:


def sjf():
    df2 = df
    n = len(p)
    tat =[0]*n
    wt = [0]*n
    rt = [0]*n
    start = [0]*n
    comp = [0]*n
    is_compeleted = [0]*n
    compeleted = 0
    current_time = 0
    idle = 0
    total_tat = 0
    total_wt = 0
    total_rt = 0
    total_idle = 0
    while(compeleted!=len(p)):
        index1 = -1
        minimum = 100000
        for i in range(len(p)):
            if(arrival[i]<=current_time) & (is_compeleted[i]==0):
                if burst[i]<minimum:
                    minimum = burst[i]
                    index = i
                    i+=1
            elif (burst[i]==minimum):
                if arrival[i]<arrival[index1]:
                    minimum = burst[i]
                    index = i
                    i+=1
                        
    

        if index1!= -1:
            start[index1] = current_time
            comp[index1] = start[index1] + burst[index1]
            tat[index1] = comp[index1] - arrival[index1]
            wt[index1] = tat[index1] - burst[index1]
            rt[index1] = start[index1] - arrival[index1]
            total_tat += tat[index1]
            total_wt += wt[index1]
            total_rt += rt[index1]
            total_idle = start[index1] - idle
            
            
            is_compeleted[index1] = 1
            compeleted+=1
            current_time = comp[index1]
            idle = current_time
            
        else:
            current_time+=1
            
            
    df2['Start Time'] = start
    df2['Compeletion Time'] = comp
    df2['Turn Around Time'] = tat
    df2['Waiting Time'] = wt
    df2['Response Time'] = rt
    display(df2)
            
            
            
        

    
        
    
    


# In[ ]:


print(sjf())


# In[ ]:




