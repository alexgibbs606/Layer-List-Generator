from pathlib import Path
from re import split as resplit

class LayerData():
	def __init__(self, layerFile:Path):

		self.layerName = ''
		self.factions = []
		self.gameMode = ''
		self.levelName = ''

		# Opening our layer file to read it's data
		with open(layerFile, 'r', encoding='utf-8') as layerFile:

			# Getting our layer name
			self.layerName = layerFile.readline().split('"')[1]

			for line in layerFile:
				line = line.strip()

				# If this is a faction setup line
				if line.startswith('SpecificFactionSetup='):
					lineList = resplit(r'/|\.|_', line)
					for posFac in lineList:
						if posFac.strip() in ['USA', 'RUS', 'RU', 'GB', 'CAF', 'MEA', 'INS', 'MIL', 'AUS', 'ADF']:
							posFac = 'RUS' if posFac == 'RU' else posFac
							faction = posFac
							break

					# Getting next line with faction tickets
					line = layerFile.readline().strip()
					tickets = 0
					if line.startswith('Tickets='):
						tickets = line.split('=')[-1].strip()

					# Appending to our faction list
					self.factions.append([faction, tickets])

				# If this is a gamemode line
				if line.startswith('GameMode='):
					self.gameMode = line.split('"')[1].strip()

				# If this is a levelID line
				if line.startswith('LevelId='):
					self.levelName = line.split('"')[1].strip()

	def __str__(self):
		string = ''

		# Printing our layer and gamemode
		string += f'{self.layerName}\n'
		string += f'  Level: {self.levelName}\n'
		string += f'  Gamemode: {self.gameMode}\n'

		# Printing our factions
		string += '  Factions:\n'
		for num, faction in enumerate(self.factions):
			string += f'    [{num}]: {faction[0]} - {faction[1]}\n'

		# Returning constructed string
		return string

	def asList(self):
		return [
			self.layerName,
			self.levelName,
			self.gameMode,
		] + [_ for __ in self.factions for _ in __]


if __name__ == '__main__':
	layer = LayerData(Path(r'C:\Users\AleX\x\layerList\Maps\Anvil\Gameplay_LayerData\Anvil_AAS_v1.PCOPY'))
	print(layer)