#TXT FILES


# filename = 'example.txt'

# file = open(filename,'r')
# content = file.read()
# print(content)
# file.close()

# with open(filename,'r') as file:
#     content = file.read()
#     # print(content)

#     for line in enumerate(content.splitlines()):
#         print(line)


# with open(filename,'a') as f:
    
#     f.write("hello world")


# with open(filename,'w') as f:
#     f.write(hello)

import os

# if not os.path.exists(filename):
#     with open(filename,'w') as f:
#         f.write('hello world')
# else:
#     print("file exist")
#     with open(filename,'a') as f:
#         f.write("hello world")

# file = "example2.txt"
# if not os.path.exists(file):
#     with open(file,'w') as f:
#         f.write("hello hello")
# else:
#     print("file exists")


#CSV FILES

import csv 
# filename = "example.csv"
# with open(filename,'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#                             # ['item', 'material', 'costperunit']
#                             # ['wall', 'concrete', '100']
#                             # ['floor', 'wood', '300']
#                             # ['roof', 'tile', '500']
#         # for item in row:
#         #     print(item)

# with open(filename,'a', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerow(['toilet','gold','9999'])


#JSON FILES

import json
filename = "example.json"
# with open(filename,'r') as f:
#     data = json.load(f)
#     print(data)
#     print(type(data))
#     mats = data['materials']

#     for mat in mats:
#         print(mat)
#         print(mat['name'])
#         print(mat['density'])

#append (read + write)

# with open(filename,'r') as f:
#     data = json.load(f)

# new_material = {
#             "id": "M0003",
#             "name": "brick",
#             "density": 4389,
#             "cost": 400
#         }

# #append new materials
# data['materials'].append(new_material)

# #override
# with open(filename, 'w') as p:
#     json.dump(data, p, indent = 4)

