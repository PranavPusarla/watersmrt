import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt

def add(x):
    x[6] += x[5] + x[4] + x[3] + x[2] + x[1] + x[0]
    x[5] += x[4] + x[3] + x[2] + x[1] + x[0]
    x[4] += x[3] + x[2] + x[1] + x[0]
    x[3] += x[2] + x[1] + x[0]
    x[2] += x[1] + x[0]
    x[1] += x[0]

def linear_reg(x, y):
    add(y);

    #placeholders for training data
    X = tf.placeholder("float")
    Y = tf.placeholder("float")

    #create variables for weights and biases
    W = tf.Variable(np.random.rand, name='W')
    b = tf.Variable(np.random.rand, name='b')

    #parameters
    learning_rate = 0.01
    training_epoch = 2000

    #7 days of the week
    n = 7

    #Hypothesis
    y_pred = tf.add(tf.multiply(X,W),b)

    #cost function
    cost = tf.reduce_mean(tf.pow(y_pred-Y, 2)) / (2*n)

    #create gradient descent optimizer
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())

        for epoch in range(training_epoch):

            for (tx, ty) in zip(x, y):
                session.run(optimizer, feed_dict = {X:tx, Y:ty})

            if (epoch % 100 == 0):
                ct = session.run(cost, feed_dict = {X:x, Y:y})
                print("Epoch: ", epoch, "Cost: ", ct, "Weight: ", session.run(W), "Bias: ", session.run(b))

        training_cost = session.run(cost, feed_dict = {X:x, Y:y})
        weight = session.run(W)
        bias = session.run(b)

    result = weight*x+bias
    prediction = weight*14 + bias
    # print("Predicted value at 2 weeks: ", prediction)
    # plt.plot(x, y, 'ro', label='Original data')
    # plt.plot(x, result, label='Fitted line')
    # plt.title('Linear Regression Result')
    # plt.legend()
    # plt.show()
    return prediction

# x = np.array([1,2,3,4,5,6,7])
# y = np.array([2,4,1,5,3,2,2])
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Training Data")
# plt.show()
# linear_reg(x,y)