from sklearn.cluster import KMeans
import time



def import_data(file):
	"""
	 This function imports the data into a list form a file name passed as an argument. 
	 The file should only the data seperated by a space.(or change the delimiter as required in split)
	"""
	data = []
	f = open(str(file), 'r')
	for line in f:
		current = line.split()	#enter your own delimiter like ","
		for j in range(0,len(current)):
			current[j] = int(current[j])
		data.append(current)
	print "finished importing data"
	return data
	


start = time.time()

X = import_data('data_set.txt')

# Number of clusters
kmeans = KMeans(n_clusters=2)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_

print(centroids)

print(labels)

elapsed_time = time.time()-start

print "elapsed time ",elapsed_time
