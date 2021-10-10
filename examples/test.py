from auto_ds.predictor import AutoDSPredictor
from auto_ds import AutoDS
import pandas as pd

ads = AutoDS(data='/Users/kaustuv/DataScience/DS_projects/Machine-Hack/BookPrice/'
                  'Participants_Data/Data_Train_cleaned.xlsx', target='Price',text_fields=['Title', 'Synopsis'],
             datetime_fields= ['Edition'], metric='rmse', )
predictor = AutoDSPredictor(ads).fit()
y_pred = predictor.predict('/Users/kaustuv/DataScience/DS_projects/Machine-Hack/BookPrice/'
                       'Participants_Data/Data_Test_cleaned.xlsx')
#
sub = pd.DataFrame()
sub['Price'] = y_pred
sub.to_excel('/Users/kaustuv/DataScience/DS_projects/Machine-Hack/BookPrice/result_submission.xlsx', index=False)


