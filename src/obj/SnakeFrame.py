from random import choice


class Frame:
	"""Class containing infos about the Frame to draw"""

	def __init__(self,Arena,Snake):
		self._keys = []
		self._values = []
		for i in range(1,Arena.width * Arena.height + 1):
			if i % Arena.width == 0: # Borders that are on the last column and that require \r\n after it
				self[(Arena.width,i//Arena.width)] = ("border", Arena.border + "\r\n")
			elif i % Arena.width == 1 or i in range(2,Arena.width) or i in range(Arena.width * (Arena.height-1) + 2, Arena.width * Arena.height):
				self[(i%Arena.width,i//Arena.width+1)] = ("border",Arena.border)
			elif (i%Arena.width,i//Arena.width+1) in Snake.pos:
				if (i%Arena.width,i//Arena.width+1) == Snake.pos[0]:
					self[(i%Arena.width,i//Arena.width+1)] = ("head",Snake.head)
				else:
					self[(i%Arena.width,i//Arena.width+1)] = ("body",Snake.body)
			else:
				self[(i%Arena.width,i//Arena.width+1)] = ("empty", " ")
		self.frame = ""
		self.Apple = (-1,-1)
		self.spawnApple(Arena.Apple)

	def __repr__(self):
		string = "{"
		for key, val in self.items():
			string += repr(key) + ": " + repr(val) + ",\n"
		string += "}"
		return string

	def __str__(self):
		return repr(self)

	def __len__(self):
		return len(self._keys)

	def __contains__(self, key):
		return key in self._keys

	def __getitem__(self, key):
		if key not in self._keys:
			raise KeyError("Key {} doesn't exist in this dictionnary".format(key))
		else:
			index = self._keys.index(key)
			return self._values[index]

	def __setitem__(self, key, val):
		if key in self._keys:
			index = self._keys.index(key)
			self._values[index] = val
		else:
			self._keys.append(key)
			self._values.append(val)

	def __delitem__(self, key):
		if key not in self._keys:
			raise KeyError("Key {} doesn't exist in this dictionnary".format(key))
		else:
			index = self._keys.index(key)
			del self._keys[index]
			del self._values[index]

	def __iter__(self):
		return iter(self._keys)

	def __add__(self, obj):
		if type(obj) is not type(self):
			raise TypeError("Cannot concatenate {} et {}".format(type(self), type(obj)))
		else:
			new = Ordered_Dict()

			for key, val in self.items():
				new[key] = val

			for key, val in obj.items():
				new[key] = val

			return new

	def items(self):
		for i, key in enumerate(self._keys):
			val = self._values[i]
			yield(key, val)

	def keys(self):
		return list(self._keys)

	def values(self):
		return list(self._values)

	def reverse(self):
		keys = []
		values = []
		for key, val in self.items():
			keys.insert(0, key)
			values.insert(0, val)
		self._keys = keys
		self._values = values

	def sort(self):
		sortedKeys = sorted(self._keys)

		values = []

		for key in sortedKeys:
			value = self[key]
			values.append(value)

		self._keys = sortedKeys
		self._values = values

	def get(self,*args):
		response = []
		for keys, val in self.items():
			if val[0] in args:
				response.append(keys)
		return response

	def set(self,action=None,target=[]):
		if action == "clear":
			for i in target:
				self[i] = ("empty"," ")

	def spawnApple(self,Apple):
		for keys, val in self.items():
			if val[0] == "Apple":
				self[keys] = ("empty", " ")
				break
		keyChosen = choice(self.get("empty"))
		self[keyChosen] = ("Apple",Apple)
		self.Apple = keyChosen

	def moveSnake(self,Snake):
		self.set("clear",self.get("body","head"))
		isHead = True
		for i in Snake.pos:
			if not isHead:
				self[i] = ("body", Snake.body)
			else:
				self[i] = ("head", Snake.head)
				isHead = False

	def draw(self):
		for val in self.values():
			self.frame += val[1]
		print(self.frame)
		self.frame = ""
