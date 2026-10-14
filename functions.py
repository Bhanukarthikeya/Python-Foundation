# def say_hello():
#     print("hello")
# say_hello()
# say_hello()
# say_hello()
#--------------------------------------------------------------------------------------------
# def greet(name):
#     print(f"hello {name}")
# greet("bhanu")
# greet("karthik")
#---------------------------------------------------------------------------------------
# def greet(name="bhanu"):
#     print(f"hello {name}")
# greet()
# greet("karthik")

# def greet(name,salutation=''):
#     print(f"hello {salutation}{name}")
# greet("bhanu","Mr.")
#-------------------------------------------------------------------------------------
# def addition(a,b):
#     total = a + b
#     print(f"{a} + {b} = {total}")
#     return total
# x = addition(5,5)
# y = addition(5,6)
# z = addition(10,5)
# print(x,y,z)
#---------------------------------------------------------------------------------------------------------------
# materials = ["concrete" , "steel" , "glass" ,"wood" , "brick" ]
# count = 0

# for mat in materials:
#     count += 1
#     print(count,mat)

# for n,mat in enumerate(materials,1):
#     print(n,mat)
#---------------------------------------------------------------------------------------------
# x = 4
# if isinstance(x,int):
#     print(x**2)

# if isinstance(x,(int,float)):
#     print(x**3)
#----------------------------------------------------------------------------
# print(list(range(5)))
# print(list(range(2,7)))
# print(list(range(2,10,2)))
#-------------------------------------------------------------------------------------------
# numbers = [5,2,3,6,8,7,9,0]
# print(sorted(numbers)) #[0,2,3,5,6,7,8,9]
# print(sorted(numbers,reverse = True)) #[9,8,7,6,5,3,2,0]
 
# alpha = [a,f,v,r,g,h]
# print(sorted(alpha)) #[a,g,h,f,r,v]
#---------------------------------------------------------------------------------
# materials = {'steel':120,
#              'concrete':75,
#              'wood':40,
#              'brick':95}

# def get_value(item):
#     return item[1]

# sorted_materials = sorted(materials.item(),key = get_value)
#-----------------------------------------------------------------------------------------
# materials = ['concrete','steel','wood']
# strength = [25,50,15]
# zip_materials = zip(materials,strength)
# materials_strength = list(zip_materials)
# print(materials_strength)
#------------------------------------------------------------------------------------
