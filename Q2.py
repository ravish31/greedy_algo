#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
try:
    input_file=open("./inputPS10Q2.txt","r")
except:
    print('Please ensure the input file has the correct name(inputPS10Q2.txt) and present in current working directory')
    sys.exit()
list_lines=input_file.readlines()


# In[2]:


list_of_list=[]
for i in list_lines:
        list_of_list.append(i.split(':')[1].replace(' ','').replace('\n','').split('/'))


# In[3]:


zip_obj=zip(list_of_list[0],[i for i in map(int, list_of_list[1])],[i for i in map(int, list_of_list[2])])
final_list=[i for i in zip_obj]
# sorting first on basis of staging time and then on photography time in case of tie
sorted_list = sorted(final_list,key=lambda x: (x[1], x[2]))                              #O(nlogn)


# In[4]:


#print(final_list)
#print(sorted_list)


# In[5]:


Stage_fin=[sorted_list[0][1]]+[0]*(len(sorted_list)-1)                         #Init staging finish time array
Idle_time=[sorted_list[0][1]]+[0]*(len(sorted_list)-1)                         #Init Idle time array
Photo_start=[sorted_list[0][1]]+[0]*(len(sorted_list)-1)                       #Init photo start time array
for i in range(1,len(sorted_list),1):
    Stage_fin[i]=Stage_fin[i-1]+sorted_list[i][1]
    Photo_start[i]=Photo_start[i-1]+sorted_list[i-1][2]
    if Photo_start[i]>=Stage_fin[i]:                                           # if planned photo start time is greater than staging finish time then xavier doesnt wait
        Idle_time[i]=0
    else:
        Idle_time[i]=Stage_fin[i]-Photo_start[i]                               # if planned photo start time is less than staging finish time then xavier hast to wait
        Photo_start[i]=Stage_fin[i]                                            # photo shoot is delayed  
#print(Stage_fin)
#print(Photo_start)
#print(Idle_time)
Idle_time=sum(Idle_time)


# In[6]:


Product_Sequence=", ".join([i[0] for i in sorted_list])
Total_Time=Photo_start[len(Photo_start)-1]+sorted_list[len(Photo_start)-1][2]
with open('outputPS10Q2.txt', 'w') as f:
    f.write('Product Sequence: {}\nTotal time to complete photoshoot: {} minutes\nIdle time for Xavier: {} minutes'.format(Product_Sequence,Total_Time,Idle_time))

