from auto_ds.autods import AutoDS
from auto_ds.predictor import AutoDSPredictor
import pandas as pd


ads = AutoDS(data='/Users/kaustuv/DataScience/datasets/Titanic/train.csv', target='Survived', metric='accuracy')
predictor = AutoDSPredictor(ads).fit()


y_pred = predictor.predict('/Users/kaustuv/DataScience/datasets/Titanic/test.csv')

test_ds = pd.read_csv('/Users/kaustuv/DataScience/datasets/Titanic/test.csv')
sub = pd.DataFrame()
sub['PassengerId'] = test_ds['PassengerId']
sub['Survived'] = y_pred
sub.to_csv('/Users/kaustuv/DataScience/datasets/Titanic/submission.csv', index=False)
# 78% accuracy