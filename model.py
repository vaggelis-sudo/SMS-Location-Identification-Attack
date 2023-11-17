#"Copyright Notice and Disclaimer. 
#© NORHEASTERN UNIVERSITY 2023 SW-24013 used with permission. All rights reserved."

# Load libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_predict
from sklearn.neural_network import MLPClassifier
from sklearn import metrics, preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np
import math

# Customize tuning based on your preferences.
def tuning(X_train, y_train):
    params = {
        'hidden_layer_sizes': [(10,40,2),(10,40,10),(8,8,8),(10,10,10),(8,10,8)],
        'activation': ['tanh', 'relu', 'logistic', 'identity'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.05],
        'learning_rate': ['constant','adaptive'],
    }
    
    clf = GridSearchCV(
        estimator=MLPClassifier(),
        param_grid=params,
        cv=5,
        n_jobs=3,
        scoring='accuracy'
    )
    
    clf.fit(X_train, y_train)
    
    return clf.best_params_

print("Starting..")

# Each column, except the label, represents a feature. (Refer to the paper for more)
col_names = ['t_sent', 't_del', 't_total', 'p_ratio', 'delta_sent', 'delta_del', 'label']
feature_cols = col_names[:-1]
multiplier = 10**2

# List of file names for international datasets
file_names_international = [
    "Sample Data/International/dataset-overseas_local.csv",
    "Sample Data/International/dataset-all_countries.csv",
    "Sample Data/International/dataset-eu_countries.csv",
    "Sample Data/International/dataset-eu_oper_g.csv",
    "Sample Data/International/dataset-eu_oper_e.csv",
    "Sample Data/International/dataset-eu_oper_f.csv"
]

# List of file names for AE datasets
file_names_ae = [
    "Sample Data/AE/dataset-ae_3locations.csv",
    "Sample Data/AE/dataset-ae_4locations.csv"
]

# List of file names for GR datasets
file_names_gr = [
    "Sample Data/GR/dataset-gr_1-3.csv",
    "Sample Data/GR/dataset-gr_4-6.csv"
]

all_file_names = file_names_international + file_names_ae + file_names_gr

# Load and classify datasets
for i, file_name in enumerate(all_file_names):
    # Load dataset
    data = pd.read_csv(file_name, header=None, names=col_names)

    # Split dataset into features and target variable
    X = data[feature_cols]
    y = data.label

    label_enc = preprocessing.LabelEncoder()
    y = label_enc.fit_transform(y)

    # Feature Scaling
    sc = StandardScaler()
    X = sc.fit_transform(X)

    # Model Structure
    clf = MLPClassifier(hidden_layer_sizes=(10,40,10), solver='sgd', alpha=0.0001, learning_rate='constant', max_iter=5000, batch_size=32)
    clf.out_activation_ = 'softmax'

    y_pred = cross_val_predict(clf, X, y, cv=10)

    accuracy = metrics.accuracy_score(y, y_pred)
    print(math.ceil(accuracy * multiplier)/multiplier)
