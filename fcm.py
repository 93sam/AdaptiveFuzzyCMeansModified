import numpy as np
from reader import Reader

class FCM():
	def __init__(self,filename,n_clusters,epsilon=0.05,max_iter=-1):
		self.m = 2
		self.n_clusters = n_clusters
		self.max_iter = max_iter
		self.epsilon = epsilon

		read = Reader(filename)
		self.X,self.y = read.get_data()
		self.data_shape = self.X.shape
		rows , cols = self.data_shape
		
		self.U = []
		for i in range(rows):
			index = i % n_clusters
			l = [ 0 for j in range(n_clusters) ]
			l[index] = 1
			self.U.append(l)
		self.U = np.array(self.U).astype(np.float)
		
		self.C = []
		l = [ 0 for j in range(cols) ]
		for i in range(n_clusters):
			self.C.append(l)
		self.C = np.array(self.C).astype(np.float)


	def cost_function(self):
		J = 0
		for i in range(self.data_shape[0]):
			for j in range(self.n_clusters):
				J += (self.U[i][j] ** self.m) * (self.eucledian_dist(self.X[i],self.C[j]) ** 2)
		return J

	def update_U(self):
		for i in range(self.X.shape[0]):
			for j in range(self.n_clusters):
				sumation = 0
				for k in range(self.n_clusters):
					sumation += ( self.eucledian_dist(self.X[i],self.C[j]) / self.eucledian_dist(self.X[i],self.C[k]) ) ** (2 / (self.m-1) )
				self.U[i][j] = 1 / sumation

	def update_C(self):
		for j in range(self.n_clusters):
			num_sum = 0
			den_sum = 0
			for i in range(self.data_shape[0]):
				num_sum += np.dot((self.U[i][j] ** self.m),self.X[i])
				den_sum += self.U[i][j] ** self.m
			self.C[j] = np.divide(num_sum,den_sum)

	def eucledian_dist(self,a,b):
		return np.linalg.norm(a-b)

	def form_clusters(self):
		d = 100
		if self.max_iter != -1:
			for i in range(self.max_iter):
				print "loop : " , int(i)
				self.update_C()
				temp = np.copy(self.U)
				self.update_U()
				d = sum(abs(sum(self.U - temp)))
				print d
				if d < self.epsilon:
					break
		else:
			i = 0
			while d > self.epsilon:
				self.update_C()
				temp = np.copy(self.U)
				self.update_U()
				d = sum(abs(sum(self.U - temp)))
				print "loop : " , int(i)
				print d
				i += 1

	def calculate_score(self):
		print self.y
		print self.result
		correct = float(0)
		incorrect = 0
		for i in range(self.y.shape[0]):
			if(self.result[i] == self.y[i]):
				correct += 1
			else:
				incorrect += 1
		accuracy = (correct/float(self.y.shape[0])) * 100
		print accuracy
		

	def show_result(self):
		print self.U
		self.result = np.zeros(shape=(self.data_shape[0],1))
		self.result = np.argmax(self.U, axis = 1)
		print self.result.shape
		self.calculate_score()

def main():
	cluster = FCM('irisdata2.txt',3,0.00000000000001,300)
	cluster.form_clusters()
	cluster.show_result()

if __name__ == '__main__':
	main()