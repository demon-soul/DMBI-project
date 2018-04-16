from sklearn.cluster import KMeans
import time
	
def import_data_format_iris(file):
	""" 
	This would format the data as required by iris 
	the link for the same is http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
	"""
	data = []
	cluster_location =[]
	f = open(str(file), 'r')
	for line in f:
		current = line.split(",")
		current_dummy = []
		for j in range(0,len(current)-1):
			current_dummy.append(float(current[j]))
		j+=1 
		#print current[j]
		if  current[j] == "Iris-setosa\n":
			cluster_location.append(0)
		elif current[j] == "Iris-versicolor\n":
			cluster_location.append(1)
		else:
			cluster_location.append(2)
		data.append(current_dummy)
	print "finished importing data"
	return data , cluster_location	

start = time.time()

X ,cluster_location = import_data_format_iris('iris.txt')

# Number of clusters
kmeans = KMeans(n_clusters=3)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_

print(centroids)

print(labels)

elapsed_time = time.time()-start

print("elapsed time ",elapsed_time)
