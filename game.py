class Game():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = [[False for x in range(self.width)] for x in range(self.height)]

	def is_alive(self, x, y):
		return self.board[x][y]
		

	def bring_to_life(self, x, y):
		self.board[x][y] = True

	def kill_cell(self, x, y):
		self.board[x][y] = False

	def count_neighbors(self, x, y):
		sum = 0
		if x - 1 >= 0 and self.board[x - 1][y]:
			sum += 1
		if x + 1 < self.width and self.board[x + 1][y]:
			sum += 1
		if y - 1 >= 0 and self.board[x][y-1]:
			sum += 1
		if y + 1 < self.height and self.board[x][y+1]:
			sum += 1
		return sum

	def iterate(self):
		neighbor_matrix = [[self.count_neighbors(x, y) for y in range(self.height)] for x in range(self.width)]
		for x in range(self.width):
			for y in range(self.height):
				neighbours = neighbor_matrix[x][y]
				if neighbours == 2:
					self.bring_to_life(x, y)
				if neighbours == 4 or neighbours < 2:
					self.kill_cell(x, y)

	
