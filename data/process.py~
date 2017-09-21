import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = os.getcwd()

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for root, dirs, files in os.walk(path_data): 
	for file in files:
		if file.endswith('_crop.png'): 	
			file = os.path.abspath(os.path.join(root,file))
			print file

			if counter == index_test:
				counter = 1
				file_test.write(file + "\n")
			else:
				file_train.write(file+ "\n")
				counter = counter + 1
