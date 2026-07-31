# Classification template
# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
# from sklearn.model_selection import train_test_split
import os
# # Packages for analysis
# from natsort import natsorted
import numpy as np
# importing Statistics module
import statistics
from collections import Counter
import math
# import metrics
from matplotlib import pyplot as plt
import seaborn as sns
#############################################################################################################################


def plot_bar_belt_seat():
    Belt_Seat_90_10 = [94.96,	95,	95,	95]  # number of wesites that have more than 100 samples
    Belt_Seat_80_20 = [95.8,	96,	96,	96]  # number of wesites that have more than 100 samples

    Belt_Seat_70_30 = [96.12,	96,	96,	96]  # number of wesites that have more than 100 samples
    Belt_Seat_60_40 = [96.08,	96,	96,	96]  # number of wesites that have more than 100 samples

    Accuracy = [94.96, 95.8, 96.12,  96.08]
    Precision =[95,96,96,96]
    Recall = [95,96,96,96]
    F1_score =[95,96,96,96]

    # set width of bar
    barWidth = 0.12
    fig = plt.subplots(figsize=(9, 8))
    # Set position of bar on X axis
    br1 = np.arange(len(Accuracy))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    # Make the plot
    # colors = ['pink', 'lightgreen', 'lightblue','pink', 'lightgreen', 'lightblue']
    plt.bar(br1, Accuracy, width=barWidth, color='lightblue', edgecolor='black', label='Accuracy', hatch='\\')
    plt.bar(br2, Precision, width=barWidth, color='orange', edgecolor='black', label='Precision' , hatch='o')
    plt.bar(br3, Recall, width=barWidth, color='pink', edgecolor='black', label= 'Recall', hatch='///')
    plt.bar(br4, F1_score, width=barWidth, color='lightgreen', edgecolor='black', label='F1-score', hatch='*')
    # plt.bar(br5, W_s_above_100_f3, width=barWidth, color='lightgreen', edgecolor='black', label='F3(S > 100)', hatch='\\')
    # plt.bar(br6, W_s_less_100_f3, width=barWidth, color='lightgreen', edgecolor='black', label='F3(S < 100)',hatch='o')

    plt.grid()

    # Adding Xticks
    plt.xlabel('Train/Test split ratios', fontsize=22)
    plt.ylabel('Performance Percentage [%]', fontsize=22)
    plt.xticks([r + barWidth for r in range(4)], [ '90/10', '80/20', '70/30' , '60/40'], fontsize=18)
    plt.yticks(fontsize=16)
    # plt.title("Fusion of Belt and Seat pressure data",fontsize=22)
    # for i, v in enumerate(y):
    #     plt.text(xlocs[i] - 0.25, v + 0.01, str(v))
    plt.legend(fontsize=18)
    plt.ylim(80,100)
    plt.show()
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Training_testing_times_plot_for Belt and Seat



def plot_authentication_time_Belt():
    Tr_LR = [75.80739999, 79.47,97.00799998, 107.0404]
    Ts_LR = [7.429299993,6.2301,6.175899995, 6.091699994]
    Tr_RF = [4610.4885, 5156.2866, 5682.0133, 6098.119]
    Ts_RF = [536.3063, 512.1129, 476.568, 439.091]
    fig, ax = plt.subplots(figsize=(9, 10))
    Rounds = ['60/40','70/30','80/20','90/10']
    labels_list=['Train using RF', 'Test using RF', 'Train using LR', 'Test using LR']
    color_list= ['red', 'black', 'blue', 'green']
    linestyle_list = ['-','--','-','--','-','--']
    plt.plot(Rounds, Tr_RF, linestyle=linestyle_list[0], marker='^', color=color_list[2], lw=3, label=labels_list[0],clip_on=False)
    plt.plot(Rounds, Ts_RF, linestyle=linestyle_list[1], marker='*', color=color_list[3], lw=3, label=labels_list[1],clip_on=False)
    plt.plot(Rounds, Tr_LR , linestyle=linestyle_list[0], marker='^', color=color_list[0], lw=3,label=labels_list[2] , clip_on=False)
    plt.plot(Rounds, Ts_LR, linestyle=linestyle_list[1], marker='*', color=color_list[1], lw=3,label=labels_list[3] , clip_on=False)

    plt.xlabel('Train/Test split ratios', fontsize=22)
    plt.ylabel('Time in milliseconds (ms)', fontsize=22)
    # plt.title('Time distribution for location identification' , fontsize = 16)
    plt.legend(loc="best", fontsize = 20)
    plt.grid(linestyle='--', linewidth='0.2', color='black')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax.set_yscale('log')
    plt.show()


def plot_authentication_time_Seat():
    Tr_LR = [136.4067, 148.8696,165.3314, 186.3274]
    Ts_LR = [9.076100017,7.714999985,6.890400022,6.3868]
    Tr_RF = [13166.1955,14772.6596,16350.7606, 17717.1758]
    Ts_RF = [1340.454, 1125.1364,1051.7782, 962.6144]
    fig, ax = plt.subplots(figsize=(9, 10))
    Rounds = ['60/40','70/30','80/20','90/10']
    labels_list=['Train using RF', 'Test using RF', 'Train using LR', 'Test using LR']
    color_list= ['red', 'black', 'blue', 'green']
    linestyle_list = ['-','--','-','--','-','--']
    plt.plot(Rounds, Tr_RF, linestyle=linestyle_list[0], marker='^', color=color_list[2], lw=3, label=labels_list[0],clip_on=False)
    plt.plot(Rounds, Ts_RF, linestyle=linestyle_list[1], marker='*', color=color_list[3], lw=3, label=labels_list[1],clip_on=False)
    plt.plot(Rounds, Tr_LR , linestyle=linestyle_list[0], marker='^', color=color_list[0], lw=3,label=labels_list[2] , clip_on=False)
    plt.plot(Rounds, Ts_LR, linestyle=linestyle_list[1], marker='*', color=color_list[1], lw=3,label=labels_list[3] , clip_on=False)

    plt.xlabel('Train/Test split ratios', fontsize=22)
    plt.ylabel('Time in milliseconds (ms)', fontsize=22)
    # plt.title('Time distribution for location identification' , fontsize = 16)
    plt.legend(loc="best", fontsize = 20)
    plt.grid(linestyle='--', linewidth='0.2', color='black')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax.set_yscale('log')
    plt.show()


def plot_authentication_time_Belt_Seat():
    Tr_RF = [19.2383098
,21.0493906
,23.8572451
, 26.0526431
]
    Ts_RF = [2.3278662
,2.2575214
 ,2.1399131
,2.1129995 ]
    fig, ax = plt.subplots(figsize=(9, 10))
    Rounds = ['60/40','70/30','80/20','90/10']
    labels_list=['Train using RF', 'Test using RF']
    color_list= ['red', 'blue']
    linestyle_list = ['-','--','-','--','-','--']
    plt.plot(Rounds, Tr_RF, linestyle=linestyle_list[0], marker='^', color=color_list[0], lw=3, label=labels_list[0],clip_on=False)
    plt.plot(Rounds, Ts_RF, linestyle=linestyle_list[1], marker='*', color=color_list[1], lw=3, label=labels_list[1],clip_on=False)

    plt.xlabel('Train/Test split ratios', fontsize=22)
    plt.ylabel('Time in seconds (s)', fontsize=22)
    # plt.title('Time distribution for location identification' , fontsize = 16)
    plt.legend(loc="best", fontsize = 20)
    plt.grid(linestyle='--', linewidth='0.2', color='black')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    # ax.set_yscale('log')
    plt.show()



if __name__ == '__main__':
    plot_bar_belt_seat()
    # plot_authentication_time_Belt()
    # plot_authentication_time_Seat()
    # plot_authentication_time_Belt_Seat()
