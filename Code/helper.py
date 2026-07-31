import os
import re
import sklearn as sk
from sklearn.model_selection import train_test_split

import numpy as np
# import sklearn as sk
# import sklearn.preprocessing as prep
# import sklearn.model_selection as model_selection
# import sklearn.metrics as metrics
# import sklearn.ensemble as ensemble
import pandas as pd


def load_Belt_data(Belt_path):
    iterations= ["1", "10", "2", "3", "4", "5", "6", "7", "8", "9"]
    index = 0

    data_one_user = []
    for root, dirs, files in os.walk(Belt_path):
        for name in files:
            df = pd.read_csv(os.path.join(Belt_path, name))
            # print(os.path.join(Belt_path, name))
            df.columns = [1, 2, 3, 4, 5,
                          6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15,
                          16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25,
                          26, 27, 28, 29, 30
                          ]
            # print(df)
            # df.to_csv(name + ".csv")
            data_one_user.append(df)
    one_user_df = pd.concat(data_one_user, ignore_index=True)
    # print(one_user_df)
    # print(one_user_df.shape)
    return one_user_df




def load_Seat_data(Seat_path):
    df_list= []
    for root, dirs, files in os.walk(Seat_path):
        for name in files:
            df = pd.read_csv(os.path.join(Seat_path, name), index_col=None)
            # print(df.shape)
            del df[df.columns[0]]#delet time column (first column)
            df.drop(columns=df.columns[-1], axis=1, inplace=True)#delete the 31th col, to be same as Belt (i.e. 30 cols)
            # print(os.path.join(Seat_path, name))
            # print(df.shape)
            # print(df)
            df = pd.DataFrame(df.values)
            df_list.append(df)
    one_user_df = pd.concat(df_list, ignore_index=True)
    # print(one_user_df.shape)
    return one_user_df


def Data_process(data):# split each website dataframe into train/test and then contact them
    X_train =[]
    X_test = []
    y_train = []
    y_test = []
    for i in range(len(data)):#
        data_df_ith = data[i]
        # print(data_df_ith.shape)
        X = data_df_ith.iloc[:,:-1]
        y = data_df_ith.iloc[:, -1:]

        X_train_ith, X_test_ith, y_train_ith, y_test_ith = train_test_split(X, y, test_size=0.4, random_state=0)
        # print(X_train_ith.shape)
        # print(X_test_ith.shape)
        X_train.append(X_train_ith)
        X_test.append(X_test_ith)
        y_train.append(y_train_ith)
        y_test.append(y_test_ith)
    final_X_train = pd.concat(X_train, ignore_index=True,sort=False)
    final_X_test = pd.concat(X_test, ignore_index=True)
    # print(final_X_train.shape)
    # final_X_train.to_csv("final_X_train.csv")
    # print(final_X_test.shape)
    final_y_train = pd.concat(y_train, ignore_index=True)
    final_y_test = pd.concat(y_test, ignore_index=True)
    return final_X_train, final_X_test, final_y_train, final_y_test



def generate_n_grams(data_df, n ):
	from nltk.util import ngrams
	import itertools
	train_data_grams = []
	for a in data_df.values:
		l = list(ngrams(a, n=n))
		l2 = list(itertools.chain(*l))
		train_data_grams.append(l2)
	train_data_grams_df = pd.DataFrame(train_data_grams)
	return train_data_grams_df


# data normalization and preprossing
def data_preprocessing(train_data, test_data, pca=False, bigrams=False, trigrams=False):
	"""
	:param train_data:
	:param test_data:
	:return: normalized train data and test data
	"""


	# ##################### MinMaxScaler ##############################
	from sklearn.preprocessing import StandardScaler, MinMaxScaler
	scaler = MinMaxScaler(feature_range=(0, 1))
	scaler = scaler.fit(train_data)
	train_data = pd.DataFrame(scaler.transform(train_data))
	scaler = scaler.fit(test_data)
	test_data = pd.DataFrame(scaler.transform(test_data))
	###################################################


	# bigram
	if bigrams:
		# for bigrams
		train_data = generate_n_grams(train_data, 2)
		test_data = generate_n_grams(test_data, 2)

	# trigram
	if trigrams and not bigrams:
		train_data = generate_n_grams(train_data, 3)
		test_data = generate_n_grams(test_data, 3)

	# PCA
	if pca:
		pca = sk.decomposition.PCA(n_components=0.95)
		train_data = pca.fit_transform(train_data)
		test_data = pca.transform(test_data)

	return train_data, test_data

