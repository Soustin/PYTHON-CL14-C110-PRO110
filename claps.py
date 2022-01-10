import plotly.figure_factory as pff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("newdata.csv")
data = df["claps"].to_list()

def mean_our(counter) :
    dataset = []
    for i in range(1, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plotmean(meanlist) :
    df = meanlist
    Fig = pff.create_distplot([df], ["Average"], show_hist = False)
    Fig.show()

def setup() :
    mean_list = []
    for i in range(0, 1000):
        set_of_means = mean_our(30)
        mean_list.append(set_of_means)
        plotmean(mean_list)

setup()