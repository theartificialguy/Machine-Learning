import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import random

# X = np.array([1,2,3,4,5,6],dtype='float64')
# y = np.array([5,4,6,5,6,7],dtype='float64')

def createDataset(samples,variance,step=2,correlation=False):
	val = 1
	y = []
	for _ in range(samples):
		point = val + random.randrange(-variance,variance)
		y.append(point)
		if correlation == "pos":
			val+=step
		elif correlation == "neg":
			val-=step
	X = []
	for x in range(len(y)):
		X.append(x)

	X = np.array(X,dtype="float64")
	y = np.array(y,dtype="float64")

	return X,y

X,y = createDataset(50,50,correlation="pos")

def fit(X,y):

	slope = (((mean(X) * mean(y)) - mean(X * y)) / 
		(mean(X)**2 - mean(X**2)))

	intercept = (mean(y) - slope * mean(X))

	return round(slope,2), intercept

def squarredError(yPred,y):
	return sum((yPred-y)**2)

def coefficient_of_determination(y,yPred):
	y_meanLine = []
	for y_ in y:
		y_meanLine.append(mean(y))

	squarred_error_of_regLine = squarredError(yPred,y)
	squarred_error_of_meanLine = squarredError(y_meanLine,y)
	return round(1 - (squarred_error_of_regLine / squarred_error_of_meanLine),2)

m, b = fit(X,y)
print("slope:",m,"\nintercept:",b)

#creating regression line:
# for x in X:
# 	regressionLine.append((m*x)+b)

regressionLine = [(m*x)+b for x in X] #this will generate a list of y predicted coordinates
#print(regressionLine)

rSquarred = coefficient_of_determination(y,regressionLine)
print("coefficient_of_determination:",rSquarred)

#predicting a y value corressponding to a new x value
new_x = 8
predicted_y = (m*new_x)+b 

style.use('fivethirtyeight')
plt.scatter(X,y)
plt.scatter(new_x,predicted_y,s=100,color='red')
plt.plot(X,regressionLine)
plt.show()