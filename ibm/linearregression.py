import matplotlib.pyplot as plt
from statistics import mean
from matplotlib import style
import numpy as np


def calculate_slope_intersect(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))
    b = mean(ys) - m * mean(xs)
    return m, b


def linear_Regression():
    regression_line = [(m * x) + b for x in xvalues]
    style.use('ggplot')
    plt.title("Training data and regression line")
    plt.scatter(xvalues, yvalues, color='#003F72', label='Training DATA')
    plt.plot(xvalues, regression_line, label="Reg line")
    plt.legend(loc='best')
    plt.show()


def test_data():
    predict_xvalue = 7
    predict_yvalue = (m * predict_xvalue) + b
    print('Test Data for x :', predict_xvalue, 'Test data for y :', predict_yvalue)
    plt.title("Train reg line & test values")
    plt.scatter(xvalues, yvalues, color='#003F72', label='data')
    plt.scatter(predict_xvalue, predict_yvalue, label='predicted value ', color='#ff0000')
    plt.legend(loc='best') # where to put legend
    plt.show()

    pass


# testing

def validate_results():
    predict_xvalues = np.array([2.5, 3.5, 4.5, 5.5, 6.5], dtype=np.float64)
    predict_yvalues = [(m * x) + b for x in predict_xvalues]
    print("validation data set")
    print("X values : ",predict_xvalues)
    print("y values : ", predict_yvalues)

    pass


# driver code
yvalues = np.array([5, 4, 6, 5, 6], dtype=np.float64)
xvalues = np.array([1, 2, 3, 4, 5], dtype=np.float64)

m, b = calculate_slope_intersect(xvalues, yvalues)
print("slope :", m, "\t intercept : ", b)
# plotting

linear_Regression()
test_data()
# validate
validate_results()
