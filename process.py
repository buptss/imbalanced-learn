#!/usr/bin/env python
# encoding: utf-8

from xgboost import XGBClassifier as xgb
import pandas as pd
from matplotlib import pyplot
from matplotlib.ticker import NullFormatter
from imblearn.metrics import geometric_mean_score
# from imbalancedlearn.imblearn.datasets import fetch_datasets
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN, BorderlineSMOTE, SVMSMOTE, SparseSMOTE

import numpy as np
from sklearn.metrics import roc_curve, auc, recall_score, precision_score, f1_score, roc_auc_score, average_precision_score
from sklearn.model_selection import train_test_split, cross_val_score, KFold
import warnings
import MWMOTE
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import sklearn


warnings.filterwarnings(action='ignore', category=sklearn.exceptions.UndefinedMetricWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
# from analysis import analyze_data_proportion, export_pr_auc

# control block
# sampling strategy means the minority / majority after the oversample operation.
sampling_strategy = 0.5
chunk_size = 1000000
SHOW_FEATURE = False
SHOW_METRICS = True
SHOW_DURATION_TIME = False
SHOW_AUC_ROC_PLOT = False
SHOW_TSNE = False
# init sample method
# sample_methods = ['Sparse SMOTE']
sample_methods = ['SMOTE', 'Sparse SMOTE', 'random', 'No Sample']
# sample_methods = ['SMOTE']
# sample_methods = ['random', 'SMOTE', 'Sparse SMOTE', 'SMOTEBorderline-1', 'SMOTEBorderline-2',
#                   'SVMSMOTE', 'ADASYN', 'No Sample']
# test dataset
# datasets = ['webpage']
# datasets = ['car_eval_4']
# datasets = ["coil_2000"]
# sparsity ratio >= 0.5
datasets = ["coil_2000"]
# datasets = ["arrhythmia", "webpage"]
# datasets = ["car_eval_34", "coil_2000", 'arrhythmia', 'solar_flare_m0','car_eval_4', 'webpage']
# datasets = ["car_eval_34", "coil_2000", 'solar_flare_m0','car_eval_4']

# 0.2 <= sparsity ratio < 0.5
# datasets = ["abalone", "optical_digits", "sick_euthyroid", "thyroid_sick", "abalone_19"]

# sparsity ratio < 0.2
# datasets = ['letter_img']
# datasets = ['ecoli', 'satimage', 'pen_digits',
#             'isolet', 'us_crime', 'yeast_ml8', 'scene', 'libras_move',
#             'oil', 'wine_quality', 'letter_img', 'yeast_me2',
#             'ozone_level', 'mammography', 'protein_homo']


# all
# datasets = ['ecoli', 'optical_digits', 'satimage', 'pen_digits', 'abalone', 'sick_euthyroid', 'spectrometer',
#          'car_eval_34', 'isolet', 'us_crime', 'yeast_ml8', 'scene', 'libras_move', 'thyroid_sick', 'coil_2000',
#          'arrhythmia', 'solar_flare_m0', 'oil', 'car_eval_4', 'wine_quality', 'letter_img', 'yeast_me2',
#          'webpage', 'ozone_level', 'mammography', 'protein_homo', 'abalone_19']


def statistics_sample_num(train_X, train_y, X_resampled, y_resampled, sample_method):
    # print the number of sample before and after oversample operation
    before_major = train_X[train_y == -1]
    before_minor = train_X[train_y == 1]
    after_major = X_resampled[y_resampled == -1]
    after_minor = X_resampled[y_resampled == 1]
    after_minority_nonzero_num = len(after_minor[after_minor != 0])
    after_majority_nonzero_num = len(after_major[after_major != 0])
    # before_ratio = len(before_major[before_major != 0])
    ratio = after_minority_nonzero_num*1.0/after_majority_nonzero_num
    print(sample_method)
    print("before operation major non-zero num:" + str(len(before_major[before_major != 0])))
    print("before operation minor non-zero num:" + str(len(before_minor[before_minor != 0])))
    print("after operation major non-zero num:" + str(after_majority_nonzero_num))
    print("after operation minor non-zero num:" + str(after_minority_nonzero_num))
    print("after operation non-zero ratio(Minority/Majority):" + str(ratio))
    return


# handle each data set
def process(object, sample_methods):
    train_X, train_y, test_X, test_y = object['train_X'], object['train_y'], object['test_X'], object['test_y']
    metrics_dict = {}
    time_info = {}
    n_estimators = 2000
    epochs = n_estimators
    # epochs = len(results['validation_0']['logloss'])
    x_axis = range(0, epochs)
    fig, ax = pyplot.subplots()

    if SHOW_TSNE:
        n_components = 2
        perplexity = 50
        (fig, subplots) = plt.subplots(1, len(sample_methods), figsize=(15, 8))
        num_plot = 0
    for sample_method in sample_methods:
        # before
        before_time = datetime.now()
        if SHOW_TSNE:
            ax = subplots[num_plot]
            num_plot += 1
        # over sample
        X_resampled, y_resampled = oversample(train_X, train_y, method=sample_method)

        if SHOW_TSNE:
            tsne = TSNE(n_components=n_components, init='random',
                                 random_state=0, perplexity=perplexity)
            Y_tsne = tsne.fit_transform(X_resampled)
            ax.set_title("sample_method=%s" % sample_method)
            ax.scatter(Y_tsne[y_resampled == -1, 0], Y_tsne[y_resampled == -1, 1], c="r")
            ax.scatter(Y_tsne[y_resampled == 1, 0], Y_tsne[y_resampled == 1, 1], c="g")
            ax.xaxis.set_major_formatter(NullFormatter())
            ax.yaxis.set_major_formatter(NullFormatter())
            ax.axis('tight')

        # statistics_sample_num(train_X, train_y, X_resampled, y_resampled, sample_method)
        # after
        over_time = datetime.now()
        process_time = (over_time - before_time).microseconds * 1.0 / (10**6)
        # print(process_time)
        time_info[sample_method] = "%.3f" % process_time
        # create model
        gbm = xgb(max_depth=3, n_estimators=n_estimators, learning_rate=0.01)
        # gbm = xgb(max_depth=3, n_estimators=300, learning_rate=0.01, max_delta_step=0.1)
        eval_set = [(X_resampled, y_resampled), (test_X, test_y)]
        # train model
        # gbm.fit(X_resampled, y_resampled, eval_set=eval_set,
        #         eval_metric=["logloss"], verbose=False)
        gbm.fit(X_resampled, y_resampled, eval_set=eval_set,
                eval_metric=["auc"], verbose=False)
        #
        train_precision, train_recall, train_f1, train_gmean, train_auc_roc, train_auc_pr, train_fpr, train_tpr, train_auc_score\
            = evaluate(train_X, train_y, gbm)
        # evaluate on test set
        precision, recall, f1, gmean, auc_roc, auc_pr, fpr, tpr, auc_score = evaluate(test_X, test_y, gbm)
        # print train_auc_roc auc_roc
        print(sample_method, train_auc_roc, auc_roc, train_auc_score, auc_score)
        results = gbm.evals_result()

        ax.plot(x_axis, results['validation_0']['auc'], label=sample_method+'_Train')
        ax.plot(x_axis, results['validation_1']['auc'], label=sample_method+'_Test')
        # ax.plot(x_axis, results['validation_0']['logloss'], label='Train')
        # ax.plot(x_axis, results['validation_1']['logloss'], label='Test')
        ax.legend()
        pyplot.ylabel('Classification AUC')
        pyplot.title('XGBoost Classification AUC')

        if SHOW_AUC_ROC_PLOT:
            plt.plot(fpr, tpr, lw=1, alpha=0.3,
                     label='%s (AUC = %0.2f)' % (sample_method, auc_score))
        metrics_dict[sample_method] = {"precision": precision, "recall": recall, "f1": f1,
                                       "gmean": gmean, "auc_roc": auc_roc, "auc_pr": auc_pr}
    if SHOW_TSNE:
        # plt.show()
        plt.savefig("tsne.pdf")
    pyplot.savefig("result.pdf")
    df = pd.DataFrame(metrics_dict)
    # df.set_index(['precision', 'recall', 'gmean', 'f1'], inplace=True)
    df = df.T
    # print(df)
    if SHOW_METRICS:
        for index, row in df.iterrows():
            print "&"+index+"&",
            # output auc_roc, auc_pr, precision, recall, f1, gmean
            if round(row["auc_roc"], 3) >= round(df["auc_roc"].max(), 3):
                print r"\textbf{%.3f" % row["auc_roc"] + "}&",
            else:
                print "%.3f" % row["auc_roc"] + "&",
            if round(row["auc_pr"], 3) >= round(df["auc_pr"].max(), 3):
                print r"\textbf{%.3f" % row["auc_pr"] + "}&",
            else:
                print "%.3f" % row["auc_pr"] + "&",
            if round(row["precision"], 3) >= round(df["precision"].max(), 3):
                print r"\textbf{%.3f" % row["precision"] + "}&",
            else:
                print "%.3f" % row["precision"] + "&",

            if round(row["recall"], 3) >= round(df["recall"].max(), 3):
                print r"\textbf{%.3f" % row["recall"] + "}&",
            else:
                print "%.3f" % row["recall"] + "&",
            if round(row["f1"], 3) >= round(df["f1"].max(), 3):
                print r"\textbf{%.3f" % row["f1"] + "}&",
            else:
                print "%.3f" % row["f1"] + "&",
            if round(row["gmean"], 3) >= round(df["gmean"].max(), 3):
                print(r"\textbf{%.3f" % row["gmean"] + r"}\\")
            else:
                print("%.3f" % row["gmean"] + r"\\")
    # evaluate(X, y, "No Sample", gbm)
    return time_info


# involved collected over sample methods
def oversample(x, y, method):
    randomstate = 42
    if method == 'No Sample':
        # 不采样
        return x, y
    elif method == 'random':
        # 随机过采样
        ros = RandomOverSampler(sampling_strategy=sampling_strategy, random_state=randomstate)
        X_resampled, y_resampled = ros.fit_resample(x, y)
    elif method == 'SMOTE':
        # SMOTE算法
        X_resampled, y_resampled = SMOTE(sampling_strategy=sampling_strategy, random_state=randomstate).fit_resample(x, y)
    elif method == 'Sparse SMOTE':
        # Sparse SMOTE算法
        X_resampled, y_resampled = SparseSMOTE(sampling_strategy=sampling_strategy, random_state=randomstate).fit_resample(x, y)
    elif method == 'SMOTEBorderline-1':
        # BorderlineSmote算法 borderline-1
        X_resampled, y_resampled = BorderlineSMOTE(sampling_strategy=sampling_strategy, kind='borderline-1', random_state=randomstate).fit_resample(x, y)
    elif method == 'SMOTEBorderline-2':
        # BorderlineSmote算法 borderline-2
        X_resampled, y_resampled = BorderlineSMOTE(sampling_strategy=sampling_strategy, kind='borderline-2', random_state=randomstate).fit_resample(x, y)
    elif method == 'SVMSMOTE':
        # SVMSMOTE算法
        X_resampled, y_resampled = SVMSMOTE(sampling_strategy=sampling_strategy, random_state=randomstate).fit_resample(x, y)
    elif method == 'ADASYN':
        # ADASYN算法
        X_resampled, y_resampled = ADASYN(sampling_strategy=sampling_strategy, random_state=randomstate).fit_resample(x, y)
    elif method == 'mwmote':
        # MWMOTE算法
        X_resampled, y_resampled = MWMOTE.MWMOTE(x, y, N=1000, return_mode='append')
    # 统计过采样数量
    # from collections import Counter
    # print(sorted(Counter(y_resampled).items()))
    return X_resampled, y_resampled


# function: evaluate the oversample effects on the test set
def evaluate(test_X, test_y, model):
    # apply the model to the test and training data
    predicted_test_y = model.predict(test_X)
    # predicted_train_y = gbm.predict(train_X)

    # print("precision rate/recall rate/f1 score/G-means")
    precision = precision_score(test_y, predicted_test_y)
    recall = recall_score(test_y, predicted_test_y)
    f1 = f1_score(test_y, predicted_test_y)
    gmean = geometric_mean_score(test_y, predicted_test_y)
    auc_roc = roc_auc_score(test_y, predicted_test_y)
    auc_pr = average_precision_score(test_y, predicted_test_y)
    fpr, tpr, thresholds = roc_curve(test_y, predicted_test_y)
    auc_score = auc(fpr, tpr)

    return precision, recall, f1, gmean, auc_roc, auc_pr, fpr, tpr, auc_score


def calc_sparsity_ratio(X):
    # calculate sparsity ratio
    print(np.sum(X == 0))
    print(X.size)
    sparsity_ratio = "%.4f" % (np.sum(X == 0)*1.0/X.size)
    return sparsity_ratio

# def deal_with_slash(name):
#     char_list = name.split("_")
#     ret = char_list[0]
#     for i in range(1, len(char_list), 1):
#         ret = ret + "\_" + char_list[i]
#     return ret


# 功能：主程序
if __name__ == '__main__':
    # column_names = ["sex", "length", "diameter", "height", "whole weight", "shucked weight", "viscera weight",
    #                 "shell weight", "rings"]
    # filename = "abalone.data"
    # names = ['optical_digits']
    # names = ['ecoli', 'optical_digits']
    time_dict = {}
    for dataset in datasets:
        if SHOW_AUC_ROC_PLOT:
            plt.cla()
        if SHOW_METRICS:
            print(r"\multirow{6}{*}{\textbf{"+dataset+"}}")
        # object = fetch_datasets(data_home='./data/')[dataset]
        object = np.load('./data/zendo_stable/'+dataset+'.npz')
        time_info = process(object, sample_methods)
        time_dict[dataset] = time_info
        if SHOW_METRICS:
            print("\hline")
        if SHOW_AUC_ROC_PLOT:
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('dataset:' + datasets[0])
            plt.legend(loc="lower right")
            plt.grid()
            plt.savefig(dataset + ".pdf")
    time_df = pd.DataFrame(time_dict)
    time_df = time_df.T
    if SHOW_DURATION_TIME:
        for index, row in time_df.iterrows():
            print index+"&"+row["random"],
            print "&"+row["SMOTE"],
            print "&" + row["SMOTEBorderline-1"],
            print "&" + row["SMOTEBorderline-2"],
            print "&" + row["SVMSMOTE"],
            print "&" + row["ADASYN"] + r"\\"
            print("\hline")


