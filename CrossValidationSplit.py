from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def split():

    app_train = pd.read_csv('./Data/application_train.csv')

    # replace those values have ',' as we are going to export to csv by using ',' to split
    app_train = fix_improper_value_naming(app_train)

    # split to 80% and 20%
    train, test = train_test_split(app_train, test_size=0.2, stratify=app_train['TARGET'].values)

    # get a header
    headers = ''
    for header in app_train:
        headers = headers + header + ','
    headers = headers[:-1]

    # save to csv
    np.savetxt('./Data/train_set.csv', train, delimiter=',', fmt='%s', header=headers)
    np.savetxt('./Data/test_set.csv', test, delimiter=',', fmt='%s', header=headers)

def fix_improper_value_naming(app_train):
    app_train['NAME_TYPE_SUITE'] = app_train['NAME_TYPE_SUITE'].replace(['Spouse, partner'], 'Spouse/partner')
    app_train['WALLSMATERIAL_MODE'] = app_train['WALLSMATERIAL_MODE'].replace(['Stone, brick'], 'Stone/brick')
    return app_train