import matplotlib.pyplot as plt
# x = [i for i in range(10)]
# y = [2*i for i in range(10)]

# plt.plot(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")


# plt.scatter(x,y)
# plt.show()

# features and labels------------------------------------------------------------

# no.of features is known as dimension
# Features-attributes,independent variable,input
# label-dependent variable,output
# no.of rows is know as number of instances
# for features we use - X and for labels we use - y


#   save and open  model---------------------------------------------------------

# from sklearn.externals import joblib

# # after training we do saving
# filename = "model.sav"
# joblib.dump(model_name = clf, filename)
# #open
# clf = joblib.load(filename)


# classification------------------------------------------------------------

# 2 features and 3 labels
# plot a graph between x and y

# test train split------------------------------------------------------------------

# from sklearn import datasets
# import numpy as np
# from sklearn.model_selection import train_test_split
# iris = datasets.load_iris()
# # split it in features and labels
# x = iris.data
# y = iris.target
# # print(x,y)
# print(x.shape)
# print(y.shape)

# hours of study vs good/bad grades
# 10 different students
# train with 8
# predict with the remaining 2
# allows for determining the model accuracy
# level of accuracy
# training data must be way larger than testing data

# X_train ,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# what is KNN classification - k nearest neighbors works for both classification and regression

# import numpy as np
# import pandas as pd
# from sklearn import neighbors, metrics
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder

# data = pd.read_csv("car.data")
# # print(data.head())

# X = data[[
#     "buying",
#     "maint",
#     "safety"
# ]].values

# y = data[["class"]]

# # print(X, y)
# # converting the data
# le = LabelEncoder()
# for i in range(len(X[0])):
#     X[:,i] = le.fit_transform(X[:, i])


# # print(X)

# # converting the y

# label_maping = {
#     "unacc": 0,
#     "acc": 1,
#     "good": 2,
#     "vgood": 3
# }
# y["class"] = y["class"].map(label_maping)
# y = np.array(y)
# # print(y)

# # creating the model

# knn = neighbors.KNeighborsClassifier(n_neighbors=25,weights="uniform")
# X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2)

# knn.fit(X_train,y_train)

# predictions = knn.predict(X_test)

# accuracy = metrics.accuracy_score(y_test, predictions)

# print(predictions)
# print(accuracy)

# print("actual value: ",y[20])
# print("predicted: ", knn.predict(X)[20])


# SVM - support vector machine
#       effective high dimentional spaces
#       many kernel functions
#       classification and regression
#       about hyper plain we need to make sure that the boundary will be as big as possible boundary is measured by the 2 * the distance between
#       the data point from both the sides of hyper plain


# from sklearn import datasets
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn import svm
# from sklearn.metrics import accuracy_score

# iris = datasets.load_iris()
# # split it in features and labels
# x = iris.data
# y = iris.target
# # print(x,y)
# print(x.shape)
# print(y.shape)
# classes = ["Iris setosa","Iris Versicolour" ,"Iris Virginica"]


# X_train ,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
# model = svm.SVC()
# model.fit(X_train,y_train)


# print(model)

# predictions = model.predict(X_test)
# acc = accuracy_score(y_test,predictions)

# print("predictions: ",predictions)
# print("actual: ",y_test)
# print("accuracy: ",acc)

# for i in range(len(predictions)):
#     print(classes[predictions[i]])

# liner regression - the boston dataset we use here

# from sklearn import datasets
# from sklearn import linear_model
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# import pandas as pd


# boston = pd.read_csv("BostonHousing.csv")
# # features and labels
# X = boston.drop("medv", axis = 1)
# y = boston["medv"]
# print("X")
# print(X)
# print(X.shape)
# print("y")
# print(y)
# print(y.shape)

# # algorithm
# l_reg = linear_model.LinearRegression()

# plt.scatter(X.iloc[:, 5], y)
# plt.show()


# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)

# # train model

# model = l_reg.fit(X_train,y_train)
# predictions = model.predict(X_test)
# print("predictions: ",predictions)
# print("R*2 value: ", l_reg.score(X,y))
# print("coedd: ",l_reg.coef_)
# print("intercept: ",l_reg.intercept_)

# linear regression vs logistic regression

# KMeans and the math behind

# from sklearn.datasets import load_breast_cancer
# from sklearn.cluster import KMeans
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import scale
# import pandas as pd


# bc = load_breast_cancer()
# # print(bc)
# X = scale(bc.data)
# # print(x)
# y = bc.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = KMeans(n_clusters=2, random_state=0)
# model.fit(X_train)
# predictions = model.predict(X_test)
# labels = model.labels_
# print("Labels: ", labels)
# print("predictions: ", predictions)
# print("accuracy: ", accuracy_score(y_test, predictions))
# print("actual: ", y_test)


# MACHINE LEARNING
# 6 different modules we are studying in this 10 hours of ML course
#
