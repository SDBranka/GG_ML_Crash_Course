# The dataset
# As in the previous exercise, this exercise uses the 
# California Housing dataset to predict the 
# median_house_value at the city block level. Like many 
# "famous" datasets, the 
# California Housing Dataset(https://developers.google.com/machine-learning/crash-course/california-housing-data-description)
# actually consists of two separate datasets, each living in 
# separate .csv files:

# The training set is in california_housing_train.csv.
# The test set is in california_housing_test.csv.
# You'll create the validation set by dividing the downloaded 
# training set into two parts:
# a smaller training set
# a validation set



import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format


# Load the datasets from the internet
# The following code loads the 
# separate .csv files and creates the 
# following two pandas DataFrames:

# train_df, which contains the training 
# set.
# test_df, which contains the test set.

train_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
test_df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_test.csv")


# Scale the label values
# The following code scales the median_house_value. 
# See the previous pandas_UltraQuick_Tutorial exercise 
# for details.

scale_factor = 1000.0

# Scale the training set's label.
train_df["median_house_value"] /= scale_factor 

# Scale the test set's label
test_df["median_house_value"] /= scale_factor


# Load the functions that build and train a model
# The following code cell defines two functions:
#    build_model, which defines the model's topography.
#    train_model, which will ultimately train the model, 
#       outputting not only the loss value for the training 
#       set but also the loss value for the validation set.

#Define the functions that build and train a model
def build_model(my_learning_rate):
    # Create and compile a simple linear regression model.
    # Most simple tf.keras models are sequential.
    model = tf.keras.models.Sequential()

    # Add one linear layer to the model to yield a simple 
    # linear regressor.
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))

    # Compile the model topography into code that TensorFlow 
    # can efficiently execute. Configure training to minimize
    # the model's mean squared error. 
    model.compile(optimizer=tf.keras.optimizers.experimental.RMSprop(learning_rate=my_learning_rate),
                loss="mean_squared_error",
                metrics=[tf.keras.metrics.RootMeanSquaredError()])

    return model               


def train_model(model, df, feature, label, my_epochs, 
                my_batch_size=None, my_validation_split=0.1):
    # Feed a dataset into the model in order to train it.
    history = model.fit(x=df[feature],
                        y=df[label],
                        batch_size=my_batch_size,
                        epochs=my_epochs,
                        validation_split=my_validation_split)

    # Gather the model's trained weight and bias.
    trained_weight = model.get_weights()[0]
    trained_bias = model.get_weights()[1]

    # The list of epochs is stored separately from the 
    # rest of history.
    epochs = history.epoch
    
    # Isolate the root mean squared error for each epoch.
    hist = pd.DataFrame(history.history)
    rmse = hist["root_mean_squared_error"]

    return epochs, rmse, history.history   

# print("Defined the build_model and train_model functions.")


# Define plotting functions
# The plot_the_loss_curve function plots loss vs. epochs 
# for both the training set and the validation set.

#Define the plotting function
def plot_the_loss_curve(epochs, mae_training, mae_validation):
    # Plot a curve of loss vs. epoch.
    plt.figure()
    plt.xlabel("Epoch")
    plt.ylabel("Root Mean Squared Error")

    plt.plot(epochs[1:], mae_training[1:], label="Training Loss")
    plt.plot(epochs[1:], mae_validation[1:], label="Validation Loss")
    plt.legend()

    # We're not going to plot the first epoch, since the 
    # loss on the first epoch is often substantially 
    # greater than the loss for other epochs.
    merged_mae_lists = mae_training[1:] + mae_validation[1:]
    highest_loss = max(merged_mae_lists)
    lowest_loss = min(merged_mae_lists)
    delta = highest_loss - lowest_loss
    print(delta)

    top_of_y_axis = highest_loss + (delta * 0.05)
    bottom_of_y_axis = lowest_loss - (delta * 0.05)

    plt.ylim([bottom_of_y_axis, top_of_y_axis])
    plt.show()  

# print("Defined the plot_the_loss_curve function.")


# TODO: Task 1: Experiment with the validation split
# In the following code cell, you'll see a variable named 
# validation_split, which we've initialized at 0.2. The 
# validation_split variable specifies the proportion of 
# the original training set that will serve as the 
# validation set. The original training set contains 
# 17,000 examples. 

# Therefore, a validation_split of 0.2 means that:
# 17,000 * 0.2 ~= 3,400 examples will become the validation 
#    set.
# 17,000 * 0.8 ~= 13,600 examples will become the new 
#    training set.

# The following code builds a model, trains it on the 
#    training set, and evaluates the built model on both:
#       The training set.
#       And the validation set.

# If the data in the training set is similar to the data 
# in the validation set, then the two loss curves and the
# final loss values should be almost identical. However, 
# the loss curves and final loss values are not almost 
# identical. Hmm, that's odd.

# Experiment with two or three different values of 
# validation_split. Do different values of validation_split 
# fix the problem?

# The following variables are the hyperparameters.
learning_rate = 0.08
epochs = 30
batch_size = 100

# Split the original training set into a reduced training 
# set and a validation set. 
validation_split = 0.2
# validation_split = 0.42

# Identify the feature and the label.
my_feature = "median_income"    # the median income on a specific city block.
my_label = "median_house_value" # the median house value on a specific city block.
# That is, you're going to create a model that predicts 
# house value based solely on the neighborhood's median income.  

# Invoke the functions to build and train the model.
my_model = build_model(learning_rate)
# original function call
# epochs, rmse, history = train_model(my_model, train_df, my_feature, 
                                    # my_label, epochs, batch_size, 
                                    # validation_split)


# from task 3
shuffled_train_df = train_df.reindex(np.random.permutation(train_df.index))
epochs, rmse, history = train_model(my_model, shuffled_train_df, my_feature, 
                                    my_label, epochs, batch_size, 
                                    validation_split)


plot_the_loss_curve(epochs, history["root_mean_squared_error"], 
                    history["val_root_mean_squared_error"])


# TODO: Task 2: Determine why the loss curves differ
# No matter how you split the training set and the validation
# set, the loss curves differ significantly. Evidently, 
# the data in the training set isn't similar enough to the 
# data in the validation set. Counterintuitive? Yes, but 
# this problem is actually pretty common in machine learning.

# Your task is to determine why the loss curves aren't highly
# similar. As with most issues in machine learning, the 
# problem is rooted in the data itself. To solve this mystery
# of why the training set and validation set aren't almost 
# identical, write a line or two of pandas code in the 
# following code cell. Here are a couple of hints:

# The previous code cell split the original training set 
# into:
#    a reduced training set (the original training set - 
#       the validation set)
#    the validation set

# By default, the pandas head method outputs the first 5 
# rows of the DataFrame. To see more of the training set, 
# specify the n argument to head and assign a large positive
# integer to n.

# Examine examples 0 through 4 and examples 995 through 999
# of the training set
# The original training set is sorted by longitude. 
# Apparently, longitude influences the relationship of
# total_rooms to median_house_value.

train_df.head(n=10000)


# TODO: Task 3. Fix the problem
# To fix the problem, shuffle the examples in the training 
# set before splitting the examples into a training set and 
# validation set. To do so, take the following steps:

# Shuffle the data in the training set by adding the 
# following line anywhere before you call train_model 
# (in the code cell associated with Task 1):
#   shuffled_train_df = train_df.reindex(np.random.permutation(train_df.index))

# Pass shuffled_train_df (instead of train_df) as the second
# argument to train_model (in the code call associated with 
# Task 1) so that the call becomes as follows:
#   epochs, rmse, history = train_model(my_model, shuffled_train_df, my_feature, 
#                                       my_label, epochs, batch_size, 
#                                       validation_split)







































