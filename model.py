import pandas as pd
import numpy as np
import sys
import os

scriptdir = os.path.dirname(os.path.realpath(__file__))
datadir = os.path.join(scriptdir,'scraper')
all_ratings_path = os.path.join(datadir,'all_ratings.csv')

# Must return a dataframe
# answer_dict contains question id as key, followed by user response.
# If user did not select an answer for a particular question, response is None.
# TODO: implement actual model

# reference
# id_list_questions = ['apartment','alone','warm','cold','family','kids','otherdogs','strangers','train','groom','shed','drool','energy','exercise','playful','novice','size','bark']
# id_list_breedratings = ['Breed', ' Adaptability', ' All Around Friendliness', ' Exercise Needs', ' Health Grooming',
# ' Trainability','Adapts Well to Apartment Living','Affectionate with Family','Amount Of Shedding','Dog Friendly',
# 'Drooling Potential','Easy To Groom','Easy To Train','Energy Level','Exercise Needs','Friendly Toward Strangers',
# 'General Health','Good For Novice Owners','Incredibly Kid Friendly Dogs','Intelligence','Intensity',
# 'Potential For Mouthiness','Potential For Playfulness','Potential For Weight Gain','Prey Drive','Sensitivity Level',
# 'Size','Tendency To Bark Or Howl','Tolerates Being Alone','Tolerates Cold Weather','Tolerates Hot Weather','Wanderlust Potential']

# How the questionnaire data is translated, provides flexibility
idmap = {
	'apartment':{
		'Adapts Well to Apartment Living'	: {'weight':1,'options':{0:1, 1:5}}},
	'alone':{
		'Tolerates Being Alone'				: {'weight':1,'options':{0:1, 1:5}}},
	'warm':{
		'Tolerates Hot Weather'				: {'weight':1,'options':{0:1, 1:5}}},
	'cold':{
		'Tolerates Cold Weather'			: {'weight':1,'options':{0:1, 1:5}}},
	'family':{
		'Affectionate with Family'			: {'weight':1,'options':{0:1, 1:5}}},
	'kids':{
		'Incredibly Kid Friendly Dogs'		: {'weight':1,'options':{0:1, 1:5}},
		' All Around Friendliness'			: {'weight':0.5,'options':{0:1, 1:5}}},
	'otherdogs':{
		'Dog Friendly'						: {'weight':1,'options':{0:1, 1:5}}},
	'strangers':{
		'Friendly Toward Strangers'			: {'weight':1,'options':{0:1, 1:5}},
		' All Around Friendliness'			: {'weight':0.5,'options':{0:1, 1:5}}},
	'train':{
		' Trainability'						: {'weight':1,'options':{0:1, 1:5}}},
	'groom':{
		'Easy To Groom'						: {'weight':1,'options':{0:1, 1:5}}},
	'shed':{
		'Amount Of Shedding'				: {'weight':1,'options':{0:5, 1:1}}},
	'drool':{
		'Drooling Potential'				: {'weight':1,'options':{0:5, 1:1}}},
	'energy':{
		'Energy Level'						: {'weight':2,'options':{'low':1, 'medium':3, 'high':5}}},
	'exercise':{
		' Exercise Needs'					: {'weight':1,'options':{0:1, 1:5}}},
	'playful':{
		'Potential For Playfulness'			: {'weight':1,'options':{0:1, 1:5}}},
	'novice':{
		'Good For Novice Owners'			: {'weight':0.5,'options':{0:1, 1:5}}},
	'size':{
		'Size'								: {'weight':3,'options':{'small':1, 'medium':3, 'large':5}}},
	'bark':{
		'Tendency To Bark Or Howl'			: {'weight':1,'options':{0:5, 1:1}}}
}

# for testing purposes only
test_answers = {
	'apartment':1,
	'alone':1,
	'warm':1,
	'cold':1,
	'family':1,
	'kids':1,
	'otherdogs':1,
	'strangers':1,
	'train':1,
	'groom':1,
	'shed':1,
	'drool':1,
	'energy':'high',
	'exercise':1,
	'playful':1,
	'novice':1,
	'size':'large',
	'bark':1
}

def createTable(answer_dict,ratings_df):

	# transform according to the above mapping
	answers = {}
	for q_key, selection in answer_dict.items():
		if selection is not None:
			for rating_key, spec in idmap[q_key].items():
				answers[(q_key,rating_key)] = spec['options'][selection]

	# compute euclidean distance to each breed
	diffs = {}
	for breed, ratings in ratings_df.iterrows():
		diff = 0
		for q_tuple, answer in answers.items():
			weight = idmap[q_tuple[0]][q_tuple[1]]['weight']
			diff += (weight * abs(answer - ratings[q_tuple[1]]))**2
		diffs[breed] = diff

	# Put it into a DataFrame
	diffs_df = pd.DataFrame.from_dict(diffs,orient='index')
	diffs_df.columns = ['distance']
	diffs_df.sort_values('distance',inplace=True)

	# TESTING handy-dandy printout of results
	print(diffs_df)

	return diffs_df

if __name__ == '__main__':
	ratings = pd.read_csv(all_ratings_path)
	ratings.set_index('Breed',inplace=True)
	sys.exit(createTable(test_answers,ratings))
