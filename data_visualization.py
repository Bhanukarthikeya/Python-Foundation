import seaborn as sns
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# matplotlib basics

x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y)
plt.title("Hello")
plt.xlabel("chacha")
plt.ylabel("chachi")
plt.show()

# subplots

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.subplot(2, 2, 2)
plt.plot(x*2, y+3)
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.subplot(2, 2, 4)
plt.show()

# object oriented way

fig = plt.figure(figsize=(20, 8), dpi=100)
axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # this provide canvas as we wanted
axis1.plot(x, y)
axis2 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # this provide canvas as we wanted
# when you are studying change the values of 0.1 and 0.8 to check what they do
axis2.plot(x, y)

# types of plots

plt.scatter(x, y)  # regression
plt.hist(x)
plt.boxplot(x)

# saving plots

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)
plt.savefig("basicplot.png")

# working with images

img = mpimg.imread("images.jpeg")
plt.imshow(img)
plt.axis("off")

# distribution plots

# distributive plots are used to visualize quantitative data
# types of plots - histplot,jointplot,pairplot,rugplot


df = sns.load_dataset("tips")
df['size'].unique()

plt.subplot(1, 2, 1)
sns.displot(df['total_bill'], bins=20, kde=True)  # kurnal density estimate
plt.subplot(1, 2, 2)
sns.displot(df['tips'], bins=20, kde=True)

# jointplot

sns.jointplot("total_bill", 'tips', data=df, kind='scatter')
sns.jointplot("total_bill", 'tips', data=df, kind='kde')
sns.jointplot("total_bill", 'tips', data=df, kind='hex')
sns.jointplot("total_bill", 'tips', data=df, kind='reg')

# pair plot

sns.pairplot(df, hue="sex", pallets="rainbow")  # covariance and coorelation

# rugplot

sns.rugplot(df['total_bill'])

# categorical plots

sns.countplot(df["sex"],hue = df['smoker'])
sns.barplot(x = df['sex'],y = df['total_bill'],estimator=np.sum) # for bar plot we need to give x-axis and y-axis
# x-axis = categorical and y-axis = quantitative

sns.boxplot(x = 'tip',y = 'day',data = df)
sns.violinplot(x = df['day'],y = df['total_bill'])

sns.stripplot(x = 'day',y = 'total_bill',data = df)
sns.swarmplot(x = 'day',y = 'total_bill',data = df)

# combining swarm and violin

sns.violinplot('tip','day',data=df)
sns.swarmplot('tip','day',data=df)

# matrix plot

# heat map
# cluster map
# pivot table heat map


# heat map
flights = sns.load_dataset("flights")
tips = sns.load_dataset("tips")

tipscorr = tips[['total_bill','tip','size']]

tipscorr.corr()
sns.heatmap(tipscorr.corr(),annot=True)

sns.clustermap(tipscorr())

pvtflight = flights.pivot_table(values = 'passengers',index = 'months',columns = 'year')

sns.heatmap(pvtflight)


# regression plots

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,hue = 'sex')



# Plot	What it shows
# histplot()	Frequency within intervals
# kdeplot()	Smooth estimated density
# rugplot()	Individual observations as ticks
# jointplot()	Relationship between two variables
# pairplot()	Relationships across several variables









