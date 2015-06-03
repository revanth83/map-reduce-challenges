#!/usr/bin/env python
import sys
# current_handle = None
# cat input.txt | ./map.py | sort | ./reduce.py > output
counter = 0
dict_list=[]
for line in sys.stdin:
     counter=counter+1
     dict_list.append(eval(line))

newlist=[]
counter = 0
for i in range(len(dict_list)):
      if dict_list[i]['type'] == "customer":
         for j in range(len(dict_list)):
              if dict_list[j]['type'] == "purchase" and dict_list[j]['name']==dict_list[i]['name']:
                 temp={}
                 temp=dict_list[j]
                 temp['age']=dict_list[i]['age']
                 newlist.append(temp)        
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

print uniq(newlist)

# print dict_list[7]['type']
     # try: 
     #    print dict_list[counter]['type']
     # except:
     #    pass
    # print counter
    # line = line.strip()
    # if current_handle is None:
    #     current_handle = line
    #     continue
    # if line == current_handle:
    #     counter += 1
    # else:
    #     print current_handle, counter
    #     current_handle = line
    #     counter = 1
    # print current_handle, counter
