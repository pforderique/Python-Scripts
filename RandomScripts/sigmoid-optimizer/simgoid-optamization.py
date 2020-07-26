        # #returns the best degree of polynomial for this model NOT FUNCTIONAL
        # def getBestDegree(train_x, train_y, test_x, test_y)
        #     r2scores = {}
        #     degreeRange = 10 #get rid of this
        #     numoftries = 5
        #     clf = linear_model.LinearRegression()
        #     for n in range(0,degreeRange+1)
        #         scores = []
        #         for i in range(1,numoftries+1)
        #             #creates regression of degree n
        #             poly = PolynomialFeatures(degree=n)
        #             train_x_poly = poly.fit_transform(train_x)
        #             train_y_ = clf.fit(train_x_poly, train_y)
        #             #gets r2 score based on outside data
        #             test_x_poly = poly.fit_transform(test_x)
        #             test_y_ = clf.predict(test_x_poly)
        #             scores.append(r2_score(test_y_,test_y))
        #         #save average of tries in dict
        #         r2scores[sum(scores)numoftries] = n
        #         # r2scores[r2_score(test_y_,test_y)] = n
        #     return r2scores[max(r2scores, key=r2scores.get)]

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def sigmoid(p,x)
    x0,y0,c,k=p
    y = c  (1 + np.exp(-k(x-x0))) + y0
    return y

def residuals(p,x,y)
    return y - sigmoid(p,x)

def resize(arr,lower=0.0,upper=1.0)
    arr=arr.copy()
    if lowerupper lower,upper=upper,lower
    arr -= arr.min()
    arr = (upper-lower)arr.max()
    arr += lower
    return arr

# raw data
x = np.array([821,576,473,377,326],dtype='float')
y = np.array([255,235,208,166,157],dtype='float')

x=resize(x,lower=0.3)
y=resize(y,lower=0.3)
print(x)
print(y)

p_guess=(np.median(x),np.median(y),1.0,1.0)
p, cov, infodict, mesg, ier = scipy.optimize.leastsq(residuals,p_guess,args=(x,y),full_output=1)  

x0,y0,c,k=p
print('''
x0 = {x0}
y0 = {y0}
c = {c}
k = {k}
'''.format(x0=x0,y0=y0,c=c,k=k))

xp = np.linspace(0, 1.1, 1500)
pxp = sigmoid(p,xp)

# Plot the results
plt.plot(x, y, '.', xp, pxp, '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal') 
plt.grid(True)
plt.show()