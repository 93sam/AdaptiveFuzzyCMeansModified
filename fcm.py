import numpy as np
import math
from reader import Reader

class FCM():
	def __init__(self,n_clusters,epsilon=0.05,max_iter=-1):
		self.m = 2
		read = Reader('irisdata2.txt')
		X,y = read.get_data()
		self.data_shape = X.shape
		rows , cols = self.data_shape
		self.U = []
		for i in range(rows):
			index = i % n_clusters
			l = [ 0 for j in range(n_clusters) ]
			l[index] = 1
			self.U.append(l)
		self.U = np.array(self.U).astype(np.float)	

a = FCM(4)

