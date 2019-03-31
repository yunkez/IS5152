import pandas as pd 
import matplotlib.pyplot as plt

is_training_data = False

if is_training_data:

    app_train = pd.read_csv('./Data/train_set.csv')
    print('Training data shape: ', app_train.shape)

else:

    app_train = pd.read_csv('./Data/test_set.csv')
    print('Testing data shape: ', app_train.shape)

# count number of postive/negative samples
print(app_train['TARGET'].value_counts())

plt.figure()
app_train['TARGET'].astype(int).plot.hist()
plt.show()
