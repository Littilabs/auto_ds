import pandas as pd

from autogluon import tabular

train_data = tabular.TabularDataset('/Users/kaustuv/DataScience/datasets/Titanic/train.csv')

predictor = tabular.TabularPredictor(label='Survived',
                                     path='/Users/kaustuv/DataScience/datasets/Titanic/autogluonout').fit(train_data)

test_data = tabular.TabularDataset( '/Users/kaustuv/DataScience/datasets/Titanic/test.csv')

y_pred = predictor.predict(test_data)

test_ds = pd.read_csv('/Users/kaustuv/DataScience/datasets/Titanic/test.csv')
sub = pd.DataFrame()
sub['PassengerId'] = test_ds['PassengerId']
sub['Survived'] = y_pred
sub.to_csv('/Users/kaustuv/DataScience/datasets/Titanic/submission_autogluon.csv', index=False)
