import os
import re

import numpy as np
import sklearn as sk
# import sklearn.preprocessing as prep
# import sklearn.model_selection as model_selection
# import sklearn.metrics as metrics
# import sklearn.ensemble as ensemble
import pandas as pd
import sklearn.ensemble as ensemble

# import math
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import RepeatedStratifiedKFold
# from numpy import mean
# from numpy import std
# import pandas
# from keras.models import Sequential
# from keras.layers import Dense
# # from keras.wrappers.scikit_learn import KerasClassifier
# # from keras.utils import np_utils
# from scikeras.wrappers import KerasClassifier
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.preprocessing import LabelEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
from helper import *
import matplotlib.pyplot as plt
import timeit
##################################################################################################################

def classifier(X_train, X_test, y_train, y_test):
    from sklearn.linear_model import LogisticRegression
    train_start = timeit.default_timer()
    logreg = LogisticRegression(random_state=12).fit(X_train, y_train)
    train_end = timeit.default_timer()
    Train_elapsed_time = (train_end - train_start)
    print("Training time for the iteration: ", Train_elapsed_time)
    test_start = timeit.default_timer()
    y_pred = logreg.predict(X_test)
    print(logreg.score(X_train, y_train)*100)
    print(logreg.score(X_test, y_test)*100)
    print(y_pred)
    from sklearn import metrics
    cm = metrics.confusion_matrix(y_test, y_pred)
    print(cm)
    test_end = timeit.default_timer()
    Test_elapsed_time = (test_end - test_start)
    print("Testing time for the iteration: ", Test_elapsed_time, '% >>>>> Iteration done!')

    # import seaborn as sns
    # plt.figure(figsize=(9, 9))
    # sns.heatmap(cm, annot=True, fmt='0.0f', linewidths=0.5, square=True, cbar=False)
    # plt.ylabel('Actual users',  fontsize=22)
    # plt.xlabel('Predicted users',  fontsize=22)
    # plt.title('Belt-based data with LR model (Tr:0.9, Ts:0.1)',  fontsize=22)
    # # plt.title('Seat-based data with LR model (Tr:0.6, Ts:0.4)',  fontsize=22)
    # plt.show()
    print(metrics.classification_report(y_test, y_pred))

def classifier_2 (X_train, X_test, y_train, y_test):
    models = [
        ensemble.RandomForestClassifier(n_estimators=1000, max_depth=100, random_state=0),
    ]
    names = ['RandomForest']  # 'GradientBoosting' consumes large train time
    for name, model in zip(names, models):
        train_start = timeit.default_timer()
        model.fit(X_train, y_train)
        train_end = timeit.default_timer()
        Train_elapsed_time = (train_end - train_start)
        print("Training time for the iteration: ", Train_elapsed_time)
        test_start = timeit.default_timer()
        y_pred = model.predict(X_test)
        print(model.score(X_train, y_train) * 100)
        print(model.score(X_test, y_test) * 100)
        print(y_pred)
        from sklearn import metrics
        cm = metrics.confusion_matrix(y_test, y_pred)
        print(cm)
        test_end = timeit.default_timer()
        Test_elapsed_time = (test_end - test_start)
        print("Testing time for the iteration: ", Test_elapsed_time, '% >>>>> Iteration done!')
        # import seaborn as sns
        # plt.figure(figsize=(9, 9))
        # sns.heatmap(cm, annot=True, fmt='0.0f', linewidths=0.5, square=True, cbar=False, annot_kws={"fontsize":15})
        # plt.ylabel('Actual users', fontsize=28)
        # plt.xlabel('Predicted users', fontsize=28)
        # # plt.title('Belt-based data with RF model (Tr:0.6, Ts:0.4)', fontsize=22)
        # # plt.title('Seat-based data with RF model (Tr:0.6, Ts:0.4)', fontsize=22)
        # plt.xticks(fontsize=16)
        # plt.yticks(fontsize=16)
        # plt.show()
        print(metrics.classification_report(y_test, y_pred))


def start():
    # paths_belt = [r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U1\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U2\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U3\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U4\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U5\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U7\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U8\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U9\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U10\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U11\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U12\Belt"
    #               ]

    # paths_belt = [r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U2\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U3\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U4\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U5\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U7\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U8\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U9\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U10\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U11\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\4_seconds\U12\Belt"
    #               ]

    # paths_belt = [r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U2\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U3\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U4\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U5\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U7\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U8\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U9\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U10\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U11\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\3_seconds\U12\Belt"
    #               ]

    # paths_belt = [r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U2\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U3\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U4\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U5\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U6\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U7\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U8\Belt",
    #               # r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U9\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U10\Belt",
    #               # r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U11\Belt",
    #               r"D:\Sejong_Univ\research\Driver_authentication\datasets\2_seconds\U12\Belt"
    #               ]

    paths_seat = [
                 r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U1\Seat",
                 r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U2\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U3\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U4\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U5\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U6\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U7\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U8\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U9\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U10\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U11\Seat",
                  r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U12\Seat"
                  ]

    ########### BELT DATA #########################
    # data_all_users = []
    # for i in range (len(paths_belt)):
    #     one_user_df = load_Belt_data(paths_belt[i])
    #     one_user_df[len(one_user_df.columns)] = i+1  # Add index as labels to all record_df rows
    #     data_all_users.append(one_user_df)
    ########### SEAT DATA #########################
    data_all_users = []
    for i in range(len(paths_seat)):
        one_user_df = load_Seat_data(paths_seat[i])
        one_user_df[len(one_user_df.columns)] = i + 1  # Add index as labels to all record_df rows
        print(one_user_df.shape)
        data_all_users.append(one_user_df)
    print(len(data_all_users))

    X_tr, X_ts, y_tr, y_ts = Data_process(data_all_users)
    X_tr = X_tr.fillna(0)
    X_ts = X_ts.fillna(0)
    y_tr = y_tr.fillna(0)
    y_ts = y_ts.fillna(0)

    print("X_tr: ", X_tr.shape)
    print("X_ts: ", X_ts.shape)
    print("y_tr: ", y_tr.shape)
    print("y_ts: ", y_ts.shape)


    X_tr1, X_ts1 = data_preprocessing(X_tr, X_ts)
    # classifier(X_tr1, X_ts1, y_tr, y_ts)
    classifier_2(X_tr1, X_ts1, y_tr, y_ts)






if __name__ == '__main__':
    start()







