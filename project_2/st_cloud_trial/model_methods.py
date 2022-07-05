import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.impute import KNNImputer
import pickle

class Model_Methods:
    
    def predict(new_data):
        # impute missing `Overall Cond` values
        url = 'https://raw.githubusercontent.com/yxmauw/Personal/main/General%20Assembly/Projects/project_2/multi_app_trial/streamlit_imp_data.csv?token=GHSAT0AAAAAABWJK5JLU7B22VHUQCDUZVHOYWEFFDA'
        imp_data = pd.read_csv(url, header=0)
        imp = KNNImputer()
        imp.fit(imp_data)
        shaped_data = np.reshape(new_data, (1, -1))
        input_data = imp.transform(shaped_data)
        # load model
        with open('final_model.sav','rb') as f:
            model = pickle.load(f)
        pred = model.predict([input_data][0])
        return pred 