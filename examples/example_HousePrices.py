from auto_ds.predictor import AutoDSPredictor
from auto_ds import AutoDS
import pandas as pd
ads = AutoDS(data='/Users/kaustuv/DataScience/datasets/HousePrice/train.csv', target='SalePrice', metric='rmse')
predictor = AutoDSPredictor(ads).fit()

y_pred = predictor.predict('/Users/kaustuv/DataScience/datasets/HousePrice/test.csv')

test_ds = pd.read_csv('/Users/kaustuv/DataScience/datasets/HousePrice/sample_submission.csv')
sub = pd.DataFrame()
sub['Id'] = test_ds['Id']
sub['SalePrice'] = y_pred
sub.to_csv('/Users/kaustuv/DataScience/datasets/HousePrice/autods_submission.csv', index=False)



