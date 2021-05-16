# example of vertical line detection with a convolutional layer
from numpy import asarray
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import AveragePooling2D
from keras.layers import MaxPooling2D
from keras.layers import GlobalMaxPooling2D

def run_experiment(repeats=10):
	print('# ')
	print('# Running your experiment')
	print('# ')
	# define input data
	data = [[0, 0, 0, 1, 1, 0, 0, 0],
		    [0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 0, 1, 1, 0, 0, 0]]
	data = asarray(data)
	data = data.reshape(1, 8, 8, 1)
	print('#################')
	# create model
	model = Sequential()
	model.add(Conv2D(1, (3,3), activation='relu', input_shape=(8, 8, 1)))
	#model.add(AveragePooling2D())
	model.add(MaxPooling2D())
	#model.add(GlobalMaxPooling2D())
	# summarize model
	model.summary()
	# define a vertical line detector
	detector = [[[[0]],[[1]],[[0]]],
    		[[[0]],[[1]],[[0]]],
            [[[0]],[[1]],[[0]]]]
	weights = [asarray(detector), asarray([0.0])]
	# store the weights in the model
	model.set_weights(weights)
	# apply filter to input data
	yhat = model.predict(data)
	print(yhat)
	for r in range(yhat.shape[1]):
		# print each column in the row
		print([yhat[0,r,c,0] for c in range(yhat.shape[2])])

	for r in range(repeats):
		print(f"Repetition No: {r}")

def main():
	number_of_repetitions=1
	run_experiment(number_of_repetitions)

if __name__=='__main__':
	main()