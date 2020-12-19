from geopy.distance import great_circle
import gmplot
import sys
import webbrowser
import csv

apikey = '' # (your API key here)
coordinates = []
startcor = []
randomcor = input('Starting Point: ')
coordinates.append(randomcor)
middlecor = input('Rest of the coordinates: ')
middlecor = middlecor.split()
middlecor = list(map(str, middlecor))
middlecor2 = []
cpycor = []
path = sys.path[0]
num = 1
for i in middlecor:
  cpycor.append(i)
sortcoor = []
f = 0
a=[]
c=0
main_path=[]
x = 0
y = 1
inte = 1

def calc(middle,mini):
  #print (middle,mini)
  mini_sort=[]
  for yd in middle:
    dist = great_circle(mini, yd).km
    mini_sort.append(dist)
  #print (mini_sort)
  path=middle[mini_sort.index(min(mini_sort))]
  #print (path)
  return path

def corform(start, start2):
    for i in start:
        start = i.split(',')
        for j in start:
            j = "".join(j.split())
            j.strip()
            float(j)
            start2.append(j)

    return start2

def conver_to_float(test_string):
    res = [float(ele) for ele in test_string]
    return res

for i in coordinates:
  for j in middlecor:
    dist = great_circle(i, j).km
    sortcoor.append(dist)
    c = c + 1
    if c==len(middlecor):
      #print (sortcoor)
      main_path.append(middlecor[sortcoor.index(min(sortcoor))])
      next_path=middlecor.pop(sortcoor.index(min(sortcoor)))
      #print (main_path,next_path)
      for s in range(len(middlecor)):
        next_path=calc(middlecor,next_path)
        #print (next_path)
        #print (middlecor)
        main_path.append(next_path)
        #print (main_path)
        middlecor.remove(next_path)
        if len(middlecor)==0:
          break

start = corform(main_path, middlecor2)
# print(start)
res = conver_to_float(start)
# print(res)
start2 = corform(coordinates, startcor)
res2 = conver_to_float(start2)
gmap = gmplot.GoogleMapPlotter(res2[0],res2[1], 13, apikey=apikey, map_type='hybrid')
gmap.marker(res2[0], res2[1], color='red', title=f'{res2[0]}, {res2[1]}: No - 0')
for i in range(len(res)//2):
    # print(res[x])
    # print(res[y])
    gmap.marker(res[x], res[y], color='red', title=f'{res[x]}, {res[y]}: No - {num}')
    x+=2
    y+=2
    num+=1
gmap.draw('map.html')

if sys.platform  == 'win32':
	path = path.replace('d', 'D', 1)
path = path.replace(' ', '%20')
path = 'file:///' + path
path = path + '/map.html'
print(path)
webbrowser.open(path)
print('Sorted coordinates to go in order: ', end=' ')
for i in main_path:
    print(i, end=' ')

with open('result.csv', 'w') as new_file:
    #csv_writer =csv.writer(new_file)

    new_file.write("RouteMap Coordinates" + "," + "Route Sequence" + "\n")

    for line in main_path:
        #csv_writer.writerow(line + '')
        new_file.write('"' + line + '"' + "," + f"{inte}" + "\n")
        inte+=1