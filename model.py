import pandas as pd
import numpy as np


# Must return a dataframe
# answer_dict contains question id as key, followed by user response.
# If user did not select an answer for a particular question, response is None.
# TODO: implement actual model
def createTable(answer_dict):
	dates = pd.date_range('20130101',periods=6)
	df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
	return df