import pandas as pd
import sys
import os

def createTable():
	ratings = pd.read_csv('scraper/all_ratings.csv')
	df = pd.read_csv('logs/logs.csv')
	df = df.div(df.sum(axis=1), axis=0).sum() #normalize the rows then sum
	df = df.T
	df = df.sort_values()
	df = pd.DataFrame(df, columns=['distance'])
	df['Breed'] = df.index
	df['distance'] = df['distance'].round(2)

	final = df.merge(ratings)[['distance', 'Breed', 'image']]

	return final

if __name__ == '__main__':
	#ratings = pd.read_csv(all_ratings_path)
	#ratings.set_index('Breed',inplace=True)
	sys.exit(createTable())