# Numpy is a Python library for creating and 
# manipulating matrices, the main data structure
# used by ML algorithms. Matrices are mathematical 
# objects used to store values in rows and columns.

# Python calls matrices lists, NumPy calls them arrays 
# and TensorFlow calls them tensors. Python represents 
# matrices with the list data type.

# This Colab is not an exhaustive tutorial on NumPy. 
# Rather, this Colab teaches you just enough to use 
# NumPy in the Colab exercises of Machine Learning Crash 
# Course.


# import numpy
import numpy as np 


# Call np.array to create a NumPy array with your 
# own hand-picked values. For example, the following 
# call to np.array creates an 8-element array:

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
# print(one_dimensional_array)
# Output: [1.2 2.4 3.5 4.7 6.1 7.2 8.3 9.5]

# You can also use np.array to create a two-dimensional 
# array. To create a two-dimensional array specify an 
# extra layer of square brackets. For example, the 
# following call creates a 3x2 array:

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
# print(two_dimensional_array)
# Output: [[ 6  5]
#          [11  7]
#          [ 4  8]]

# To populate an array with all zeroes, call np.zeros. 
# To populate an array with all ones, call np.ones.

# Populate arrays with sequences of numbers
# You can populate an array with a sequence of numbers:

sequence_of_integers = np.arange(5, 12)
# print(sequence_of_integers)
# Output: [ 5  6  7  8  9 10 11]

# Notice that `np.arange` generates a sequence that 
# includes the lower bound (5) but not the upper bound (12). 


# Populate arrays with random numbers
# NumPy provides various functions to populate arrays 
# with random numbers across certain ranges. For 
# example, np.random.randint generates random integers
# between a low and high value. The following call 
# populates a 6-element array with random integers 
# between 50 and 100.

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
# print(random_integers_between_50_and_100)
# Output: [95 71 56 76 51 52]

# Note that the highest generated integer 
# np.random.randint is one less than the high argument.

# To create random floating-point values between 0.0 
# and 1.0, call np.random.random. For example:
random_floats_between_0_and_1 = np.random.random([6])
# print(random_floats_between_0_and_1) 
# Output: [0.91081218 0.91214823 0.31465157 0.74228894 0.08369342 0.44483257] 


# Mathematical Operations on NumPy Operands
# If you want to add or subtract two arrays, linear 
# algebra requires that the two operands have the same 
# dimensions. Furthermore, if you want to multiply two 
# arrays, linear algebra imposes strict rules on the 
# dimensional compatibility of operands. Fortunately, 
# NumPy uses a trick called broadcasting to virtually 
# expand the smaller operand to dimensions compatible 
# for linear algebra. For example, the following 
# operation uses broadcasting to add 2.0 to the value 
# of every item in the array created in the previous 
# code cell: 

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
# print(random_floats_between_2_and_3)
# Output: [2.14686145 2.34400734 2.69371782 2.761088   2.0091542  2.04882031]

# The following operation also relies on 
# broadcasting to multiply each cell in an array by 3:
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
# print(random_integers_between_150_and_300)
# Output: [243 159 186 234 210 219]

# TODO: Task 1: Create a Linear Dataset
# Your goal is to create a simple dataset 
# consisting of a single feature and a label as follows:

# Assign a sequence of integers from 6 to 20 (inclusive)
# to a NumPy array named feature.
# Assign 15 values to a NumPy array named label such that:
# label = (3)(feature) + 4
# For example, the first value for label should be:
#   label = (3)(6) + 4 = 22

# feature = ? # write your code here
# print(feature)
# label = ?   # write your code here
# print(label)

feature = np.arange(6, 21)
# print(feature)
# Output: [ 6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
label = (feature * 3) + 4
# print(label)
# Output: [22 25 28 31 34 37 40 43 46 49 52 55 58 61 64]

# TODO: Task 2: Add Some Noise to the Dataset
# To make your dataset a little more realistic, insert 
# a little random noise into each element of the label 
# array you already created. To be more precise, modify 
# each value assigned to label by adding a different 
# random floating-point value between -2 and +2.

# Don't rely on broadcasting. Instead, create a noise 
# array having the same dimension as label.

# noise = ?    # write your code here
# print(noise)
# label = ?    # write your code here
# print(label)

noise = (np.random.random([15]) * 4) - 2
# print(noise)
# Output: [-0.57286733 -1.54071922  1.90290374  0.89007916 -0.35851424  0.21016587
#   1.01035309  0.51888606 -1.24231287 -0.06836385  0.28768558 -0.47147641
#   1.92840661  1.33250521  0.23311039]
label = label + noise 
# print(label)
# Output: [21.30285586 23.28862293 28.44127106 29.57518709 32.08478037 36.23294035
#  39.83827781 42.71429219 45.03027209 47.62804772 53.80952978 55.00693561
#  58.68051156 59.89639972 64.63640595]