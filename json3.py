# This program extracts specific information from a json file
#It was written as part of a proficiency test for an employment application.
#Demonstrated here is comfortability with data manipulation and familiarity with JSON formatting.

import json

with open('test_data.json') as json_file:
    json_data = json.load(json_file)


users = []

for i in json_data:
    if i["user_id"] == None:
        i["user_id"] = 0
    elif i["user_id"] not in users:
        users.append(i["user_id"])

user_dict = {}
for user in users:
    user_count = 0
    for i in json_data:
        if i["user_id"]== user:
            user_count+= 1
            user_dict.update({i["user_id"]:user_count})


sort_vals = sorted(user_dict.values())
top_vals = sort_vals[-5:]

top_dict = {}
for val in top_vals:
    for user, count in user_dict.items():
        if count == val:
            top_dict.update({user:val})

#print(sorted(top_dict.items()))

#Question 10.
import numpy as np

def time_difference(start, end):
    if start== None:
        return 0
    elif end == None:
        return 0
    else:
        return end-start

times = []
for i in json_data:
    if i["status"]== 8951:
        diff = time_difference(i["start_time"], i["end_time"])
        times.append(diff)

for j in times:
    if j == 0:
        times.remove(j)
        
#print(np.mean(times))


#Question 11.

#initialize lists 
error_ids = []
double_error_ids = []


for i in json_data:
    #Find the statuses ending in 3
    if i["status"] % 10 ==3:
        if i["piece_id"] not in error_ids:
            error_ids.append(i["piece_id"])

        if i["piece_id"] in error_ids:
            if i["piece_id"] not in double_error_ids:
                double_error_ids.append(i["piece_id"])

percentage = str((len(double_error_ids)/len(json_data))*100) + '%'

#print(percentage)


# Question 12
from statistics import mode

def get_pieces(data):
    pieces = []
    for i in data:
        if i["piece_id"] not in pieces:
            pieces.append(i["piece_id"])
            
    return pieces

piece_ids = get_pieces(json_data)

path_list = []


for piece in piece_ids:
    statuses = ''
    for j in json_data:
        if j["piece_id"] == piece:
            statuses += str(j["status"]) + ' '
    path_list.append(statuses)



print(mode(path_list))
        
