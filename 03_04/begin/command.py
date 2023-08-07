class Command:
	def execute(self):
		raise NotImplementedError("Not implemented in sub-class")

class Copy(Command):
	def execute(self):
		print("Copying ...")

class Paste(Command):
	def execute(self):
		print("Pasting ...")

class Save(Command):
	def execute(self):
		print("Saving ...")

class Macro:
	def __init__(self):
		self._commands = []

	def add(self, command):
		self._commands.append(command)

	def run(self):
		for command in self._commands:
			command.execute()

def main():
	m = Macro()
	m.add(Copy())
	m.add(Paste())
	m.add(Save())
	m.run()

if __name__ == "__main__":
	main()
