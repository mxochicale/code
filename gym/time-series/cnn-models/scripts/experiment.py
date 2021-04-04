import os
from pandas import read_csv
from numpy import dstack
from keras.utils import to_categorical


# load a single file as a numpy array
def load_file(filepath):
	dataframe = read_csv(filepath, header=None, delim_whitespace=True)
	return dataframe.values

# load a list of files into a 3D array of [samples, timesteps, features]
def load_group(filenames, prefix=''):
	loaded = list()
	for name in filenames:
		data = load_file(prefix + name)
		loaded.append(data)
	# stack group so that features are the 3rd dimension
	loaded = dstack(loaded)
	return loaded

# load a dataset group, such as train or test
def load_dataset_group(group, prefix=''):
	filepath = prefix + group + '/Inertial Signals/'
	print (prefix, group,filepath)
	# load all 9 files as a single array
	filenames = list()
	# total acceleration
	filenames += ['total_acc_x_'+group+'.txt', 'total_acc_y_'+group+'.txt', 'total_acc_z_'+group+'.txt']
	# body acceleration
	filenames += ['body_acc_x_'+group+'.txt', 'body_acc_y_'+group+'.txt', 'body_acc_z_'+group+'.txt']
	# body gyroscope
	filenames += ['body_gyro_x_'+group+'.txt', 'body_gyro_y_'+group+'.txt', 'body_gyro_z_'+group+'.txt']
	# load input data
	X = load_group(filenames, filepath)
	# load class output
	y = load_file(prefix + group + '/y_'+group+'.txt')
	return X, y

# load the dataset, returns train and test X and y elements
def load_dataset(prefix=''):
	# load all train
	trainX, trainy = load_dataset_group('train', prefix + 'UCIHARDataset/')
	print('TrainX.shape:',trainX.shape, 'Trainy.shape:',trainy.shape)
	# load all test
	testX, testy = load_dataset_group('test', prefix + 'UCIHARDataset/')
	print('TestX.shape:',testX.shape, 'Testy.shape:',testy.shape)
	#print(testX)
	# zero-offset class values
	print(f'\n \n Printing trainy[:30]: \n {trainy[:30]}')
	trainy = trainy - 1
	testy = testy - 1
	print(f'\n \n Printing trainy[:30]: \n {trainy[:30]}')
	# one hot encode y
	trainy = to_categorical(trainy)
	testy = to_categorical(testy)

	print(f'\n \n One hot encode trainy: \n {trainy[:30]}')
	return trainX, trainy, testX, testy

# run an experiment
def run_experiment(repeats=10):
	print('Running experiment')
	datapath='/home/mxochicale/Downloads/'
    # load data
	trainX, trainy, testX, testy = load_dataset(datapath)
	#print(trainX.shape, trainy.shape, testX.shape, testy.shape)

	#for r in range(repeats):
	#	print (r)



def main():
	number_of_iterations=2
	run_experiment(number_of_iterations)

if __name__=='__main__':
	main()
