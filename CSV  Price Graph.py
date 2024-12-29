import csv
import matplotlib.pyplot as plt 

datachoice =input('What data would you like to graph (High,Low,Open,Close): ').title()
filename = input('File name (with .csv): ')
graph_title = input('Title of the Graph: ')

#Writes csv data into lists

try:
    date = []
    data = []
    with open(f'{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date.append(row['Date'])
            data.append(float(row[datachoice].replace(',','')))
    date.reverse(), data.reverse()
except:
    print('File not found')
#setting up the intervals for x ticks on the graph
if len(date)<9:    
    i = 0 
    xvar = []
    while i < len(date):
        xvar.append(date[i])
        i+=1
else:
    subdivs = int(len(date)/9) 

    i = 0
    xvar = []
    while i < 10:
        xvar.append(date[0 + subdivs*i])
        i+=1    

#classify each section for color 
i=1
corresponding_color = []
while i<len(data):
    if data[i]>= data[i-1]:
        corresponding_color.append('green')
        i+=1
    else:
        corresponding_color.append('red')
        i+=1

plt.rc('xtick', labelsize=6) #Resize xtick labels
fig, ax = plt.subplots()

#While loop which creates different segments on the graph, each with their corresponding color
i=1
while i<len(data):
    ax.plot(date[i-1:i+1],data[i-1:i+1], color=corresponding_color[i-1]) 
    i+=1

#Various edits to the plot
ax.set(xlim=(date[0],date[len(date)-1]), xticks=xvar, xlabel='Date', ylabel='Price',title= graph_title) 
plt.show()
