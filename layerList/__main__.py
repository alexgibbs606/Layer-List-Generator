#!/bin/env python3

# Standard Libraries
from pathlib import Path
from csv import writer as csvWriter

# Local Modules
from layerData import LayerData

# Iterating through our maps file system
maps = (Path('2.15') / 'game' / 'Maps').absolute()
layerData = []

# For each map
for gameMap in maps.iterdir():

	# There can be two different dir, we're looping through them
	for layerDir in [gameMap / possibleDir for possibleDir in ['Gameplay_LayerData', 'Gameplay_Layer_Data']]:
		# Checking if this possible layer directory exists
		if layerDir.is_dir():
			# For each layer
			for gameLayer in layerDir.iterdir():


				# Storing our layer as a LayerData object
				layerData.append(LayerData(gameLayer))

with open(Path('layers.csv'), 'w', encoding='utf-8', newline='\n') as layerFile:
	writer = csvWriter(layerFile)
	writer.writerow([
		'Layer Name',
		'Level Name',
		'GameMode',
		'Team 1',
		'T1 Tickets',
		'Team 2',
		'T2 Tickets',
	])
	for layer in layerData:
		writer.writerow(layer.asList())