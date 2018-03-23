

#----------------------------------------------------------------------------#
#Matrix form
from numpy import *

#Define the sigmoid functions
f= lambda x:    1/(1+exp(-x))
df = lambda x: 1/(1+exp(-x)) * (1-1./(1+exp(-x)))

#Inputs
x1 = 0.4
x2 = 0.7

#Outputs
t1 = 0
t2 = 1

#Weights
w1 = 0.2
w2 = 0.8
w3 = 0.5
w4 = 0.7
w5 = 0.9
w6 = 0.1
w7 = 0.4
w8 = 0.3
w9 = 0.2
w10 = 0.6
w11 = 0.0
w12 = 0.8

#Input vector
x = array([[1],[x1],[x2]])
#Target vector
t = array([[t1],[t2]])
#Input to hidden layer weight matrix
W1 = array([[w1,w2],[w3,w4],[w5,w6]])
#Hidden to output layer weight matrix
W2 = array([[w7,w8],[w9,w10],[w11,w12]])

print('x=')
print(x)
print('t=')
print(t)
print('W1=')
print(W1)
print('W2=')
print(W2)

#Propagate from input layer to hidden layer
y = f(dot(W1.T,x))
#add the bias neuron
y = reshape(insert(y,0,1), (3,1))
print('y=')
print(y)


#Propagate from hidden layer to the output layer
z = f(dot(W2.T,y))
print('z=')
print(z)

#Compute the error
e = t-z
J = 0.5*(dot(e.T,e))
print('J = %.2f' % J)
print('')

#Compute the derivatives and place them along a matrix diagonal
D2 = df(dot(W2.T,y))
D2 = diag(D2[:,0])
print('D2=')
print(D2)
print('')

#Compute the sensitivity vector for the output layer
d2 = dot(D2,e)
print('d2=')
print(d2)
print('')

#Compute the updates for the hidden to output layer weights
dW2 = dot(y,d2.T)
print('dW2=')
print(dW2)
print('')

#Compute the derivatives and place them along a matrix diagonal
D1 = df(dot(W1.T,x))
D1 = diag(D1[:,0])
print('D1=')
print(D1)
print('')

#Compute the sensitivity vector for the hidden layer
d1 = dot(D1, dot(W2[1:,:],d2))
print('d1=')
print(d1)
print('')

#Compute the updates for the input to hidden layer weights
dW1 = dot(x,d1.T)
print('dW1=')
print(dW1)
print('')

#Update weights
W1 = W1 + dW1
W2 = W2 + dW2
print('W1=')
print(W1)
print('W2=')
print(W2)