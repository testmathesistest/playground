class BFSdist:
	def __init__(self, s):
		#self.m = m
		self.s = s
	def get_distance(e):

		path = []
		distance = 0
	#	prededecessor = -1
		while queue != []:
			current = queue.pop(queue[0])
			m[current[0]][current[1]] = "V"
			if current == e:
				return distance
			disance += 1
			if m[current[0]+1][current[1]] == "U": # betrachte Feld über current
				queue.append((current[0]+1, current[1]))
			elif m[current[0]+1][current[1]] == "V":
				dist -= 1

			if m[current[0]-1][current[1]]== "U": # betrachte Feld unter current
				queue.append((current[0]-1 , current[1]))
			elif m[current[0]-1][current[1]]== "V":
				dist -= 1

			if m[current[0]][current[1]-1] == "U": # betrachte Feld links neben current
				queue.append((current[0], current[1]-1))
			elif m[current[0]][current[1]-1] == "V":
				dist -= 1

			if m[current[0]][current[1]+1] == "U": # betrachte Feld rechts neben current
				queue.append((current[0], current[1]+1))
			elif m[current[0]][current[1]+1] == "V":
				dist -= 1
		if queue == []:
			return -1
