# import matplotlib as mp

# print(mp.__version__)

# introduction

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2023,2024,2025,2026])
# y =np.array([15,25,35,20])

# plt.plot(x,y)

# plt.show()

# plot customization

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15, 25, 30, 20])
# y2 = np.array([17,23,38,26])
# y3 = np.array([10,33,45,34])

# line_style = dict(marker=".",
#               ms=20,    # markersize
#               mfc="cyan",   # markerfacecolour
#               mec="cyan",  # markeredgecolour
#               ls="solid",  # linestyle
#               lw=4 ,
#               c="black")

# plt.plot(x, y1 , **line_style)
# plt.plot(x, y2, **line_style)
# plt.plot(x, y3, **line_style)


# plt.show()


# labels

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15, 25, 30, 20])
# y2 = np.array([17,23,38,26])
# y3 = np.array([10,33,45,34])

# plt.title("Class Size", fontsize = 25,
#                         family = "Arial",
#                         fontweight = "bold",
#                         color = "darkblue")

# plt.xlabel("Year",fontsize = 20,
#                   family = "Arial",
#                   fontweight = "bold",
#                   color = "cyan")

# plt.ylabel("Students",fontsize = 20,
#                   family = "Arial",
#                   fontweight = "bold",
#                   color = "cyan")


# plt.tick_params(axis = "both",
#                 colors = "blue")

# plt.plot(x, y1 )
# plt.plot(x, y2 )
# plt.plot(x, y3 )

# plt.xticks(x)


# plt.show()

# grid lines


import matplotlib.pyplot as plt
import numpy as np

# grid() = helps make plots easier to read by adding reference lines.

# x = [1,2,3,4,5]
# y = [5,10,15,20,25]

# plt.grid(axis = "y",
#          linewidth = 2,
#          color = "lightgray",
#          linestyle = "dashed")

# plt.plot(x,y)
# plt.show()

# bar chats

# categories = np.array(["grains","fruits","vegetables","protein","dairy","sweets"])

# values = np.array([4,3,2,5,3,1])

# plt.bar(categories,values,color = "skyblue")
# plt.barh(categories,values,color = "skyblue")

# plt.title("Daily Consumptions",fontsize = 25,family = "Arial")

# plt.xlabel("Food")
# plt.ylabel("Quantity")

# plt.show()

# Pie Charts

# categories = np.array(["Freshmen","Sophomores","Juniors","Seniors"])
# values = np.array([300,250,275,225])
# colors = ["red","blue","green","yellow"]

# plt.pie(values, labels = categories,
#                 autopct="%1.1f%%",
#                 colors = colors,
#                 explode = [0,0,0,0.1],
#                 shadow=True,
#                 startangle=90)

# plt.title("Bhanu's college")


# plt.show()

# scatter Graphs

# scatter graph =  shows the relationship between two variables helps to identify a correlation
#                  (+,-,None) ex: study hours vs test scores

# x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])    # hours studied
# y1 = np.array([55, 60,65,62,68,70,75,78,82,85,87])  # Grades


# x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])    # hours studied
# y2 = np.array([56,65,65,45,76,79,76,85,87,89,95])   # Grades


# plt.scatter(x1,y1,color ="skyblue",
#             alpha = 0.5,
#             s = 100,
#             label ="Class A")
# plt.scatter(x2,y2,color ="red",
#             alpha = 0.5,
#             s = 100,
#             label = "Class B")
# plt.title("Test Scores")
# plt.xlabel("Hours Studied")
# plt.ylabel("Grades")

# plt.legend()
# plt.show()

# histograms

# histogram = a visual representation of the distraction of quantitative data.
#             they group values into bins(intervals)
#             and counts how many fall in each range

# scores = np.random.normal(loc=80,scale = 10,size = 100)
# scores = np.clip(scores , 0,100)

# plt.hist(scores,bins = 10,
#          color = "lightgreen",
#          edgecolor = "black")

# plt.title("exam scores")
# plt.xlabel("score")
# plt.ylabel("no of students")

# plt.show()

# subplots
# figure = the entire canvas
# Ax = a single plot(subplot)

# x = np.array([1,2,3,4,5])


# figure, axes = plt.subplots(2,2)

# axes[0,0].plot(x,x*2,color = "red")
# axes[0,0].set_title("x*2")

# axes[0,1].bar(x,x**2,color ="blue")
# axes[0,1].set_title("x**2")

# axes[1,0].bar(x,x**3,color = "green")
# axes[1,0].set_title("x**3")

# axes[1,1].plot(x,x**4,color = "purple")
# axes[1,1].set_title("x**4")


# plt.tight_layout()
# plt.show()

# pandas and matplotlib

import pandas as pd

# df = pd.read_csv("pokemon.csv")
# print(df.to_string())

# type_counts = df["Type1"].value_counts(ascending=True)

# plt.barh(type_counts.index, type_counts.values,color = "cyan",edgecolor = "black")
# plt.title("# of pokemons by primary type")
# plt.xlabel("Count")
# plt.ylabel("Type")
# plt.tight_layout()
# plt.show()
