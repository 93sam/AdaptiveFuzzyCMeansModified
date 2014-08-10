import numpy as np
import csv

class Reader:
	def __init__(self,filename):
		#super(Reader, self).__init__()
		self.filename = filename
		self.text_file = csv.reader(open(self.filename))

		self.data = []

		for row in self.text_file:
			self.data.append(row)

		self.data = np.array(self.data)
		self.X = self.data[0::,0:4].astype(np.float)
		self.Y = self.data[0::,4].astype(np.float)
		print self.X
		print self.Y