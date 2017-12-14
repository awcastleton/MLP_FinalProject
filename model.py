import pandas as pd
import sys
import os

# Directory paths
scriptdir = os.path.dirname(os.path.realpath(__file__))
datadir = os.path.join(scriptdir,'scraper')
logdir = os.path.join(scriptdir,'logs')
all_ratings_path = os.path.join(datadir,'all_ratings.csv')

# List of breeds to keep ordering the same for distance logging.  Yes this is 100% technical debt
breeds = ['Pekingese','Bedlington Terrier','Miniature Schnauzer','Lhasa Apso','Shiba Inu','Clumber Spaniel','Kooikerhondje','Akita',
'Giant Schnauzer','Otterhound','Yorkshire Terrier','Gordon Setter','Boykin Spaniel','Old English Sheepdog','Mutt','Bearded Collie',
'Australian Shepherd','Sealyham Terrier','Norwegian Elkhound','Pomsky','Fox Terrier','Alaskan Malamute','West Highland White Terrier',
'Icelandic Sheepdog','Petit Basset Griffon Vendeen','Canaan Dog','Australian Cattle Dog','Jack Russell Terrier','Alaskan Klee Kai',
'Pomeranian','Cardigan Welsh Corgi','Belgian Tervuren','Shih Tzu','Great Pyrenees','Norwegian Buhund','Scottish Deerhound',
'Lancashire Heeler','Pembroke Welsh Corgi','Belgian Sheepdog','Silky Terrier','Skye Terrier','German Pinscher','Maltese Shih Tzu',
'Labradoodle','Small Munsterlander Pointer','Cocker Spaniel','Brussels Griffon','Scottish Terrier','Airedale Terrier','Stabyhoun',
'Curly-Coated Retriever','Samoyed','Chinese Shar-Pei','Anatolian Shepherd Dog','Dandie Dinmont Terrier','German Wirehaired Pointer',
'Dachshund','Border Terrier','Bloodhound','Afghan Hound','Manchester Terrier','Irish Setter','Komondor','American Eskimo Dog',
'English Toy Spaniel','Irish Terrier','English Foxhound','Shetland Sheepdog','Azawakh','Chow Chow','Lakeland Terrier','Dalmatian',
'Kerry Blue Terrier','Doberman Pinscher','Irish Red and White Setter','Bracco Italiano','Chesapeake Bay Retriever','Leonberger',
'Goldador','Collie','Peekapoo','Polish Lowland Sheepdog','Border Collie','Standard Schnauzer','Tibetan Terrier','Golden Retriever',
'Finnish Spitz','Swedish Vallhund','Maltese','Kuvasz','Papillon','Norwich Terrier','Welsh Terrier','Briard','Black and Tan Coonhound',
'Cockapoo','Yorkipoo','Belgian Malinois','Affenpinscher','Cesky Terrier','Borzoi','Japanese Chin','English Springer Spaniel','Newfoundland',
'Catahoula Leopard Dog','Bichon Frise','Finnish Lapphund','Berger Picard','Barbet','Cane Corso','Bernese Mountain Dog','Mastiff',
'Rat Terrier','Treeing Tennessee Brindle','Treeing Walker Coonhound','Miniature Pinscher','Schipperke','Keeshond','Entlebucher Mountain Dog',
'Brittany','Harrier','Norwegian Lundehund','Xoloitzcuintli','Havanese','Siberian Husky','English Cocker Spaniel','Lowchen','Toy Fox Terrier',
'Plott','German Shepherd Dog','American Water Spaniel','Norfolk Terrier','Labrador Retriever','English Setter','Soft Coated Wheaten Terrier',
'Irish Wolfhound','Goldendoodle','Weimaraner','Black Russian Terrier','Portuguese Water Dog','Australian Terrier','Irish Water Spaniel','Puli',
'Welsh Springer Spaniel','Pyrenean Shepherd','Bulldog','Chinook','Boxer','Saluki','Tibetan Spaniel','Sloughi','Schnoodle','Bernedoodle',
'Rottweiler','Bull Terrier','Bolognese','Neapolitan Mastiff','Field Spaniel','Ibizan Hound','Beagle','Nova Scotia Duck Tolling Retriever',
'Basset Hound','Greater Swiss Mountain Dog','American English Coonhound','Black Mouth Cur','Bouvier des Flandres','Pocket Beagle','Puggle',
'Maltipoo','French Bulldog','Pharaoh Hound','Flat-Coated Retriever','Pug','Boston Terrier','Saint Bernard','Cavalier King Charles Spaniel',
'Poodle','American Pit Bull Terrier','Bluetick Coonhound','Redbone Coonhound','Staffordshire Bull Terrier','Whippet','Appenzeller Sennenhunde',
'Cairn Terrier','Greyhound','Dogue de Bordeaux','Basenji','Chinese Crested','Glen of Imaal Terrier','Rhodesian Ridgeback',
'Wirehaired Pointing Griffon','American Foxhound','Great Dane','Pointer','Coton de Tulear','German Shorthaired Pointer','Sussex Spaniel',
'Italian Greyhound','Vizsla','Tibetan Mastiff','Bullmastiff','Chihuahua']

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
		diffs[breed] = [diff,ratings['image']]

	# Put it into a DataFrame
	diffs_df = pd.DataFrame.from_dict(diffs,orient='index')
	diffs_df.columns = ['distance','image']
	diffs_df.sort_values('distance',inplace=True)
	diffs_df['Breed'] = diffs_df.index

	# Logging!
	logDistances(diffs_df[['Breed','distance']])

	return diffs_df

def logDistances(df):
	df.set_index('Breed',inplace=True)
	df = df.reindex_axis(sorted(df.columns), axis=1)
	with open(os.path.join(logdir,'logs.csv'), 'a') as f:
		df.T[breeds].to_csv(f,index=False,header=False)

if __name__ == '__main__':
	ratings = pd.read_csv(all_ratings_path)
	ratings.set_index('Breed',inplace=True)
	sys.exit(createTable(test_answers,ratings))
