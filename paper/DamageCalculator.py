import ConfigParser
from collections import defaultdict
import random

###############################################################################
### DAMAGE CHART

damage_chart = defaultdict(dict)

damage_chart['Infantry']['Infantry'] = {'Primary':None, 'Secondary':55}
damage_chart['Infantry']['Mech'] = {'Primary':None, 'Secondary':45}
damage_chart['Infantry']['Recon'] = {'Primary':None, 'Secondary':12}
damage_chart['Infantry']['Lt. Tank'] = {'Primary':None, 'Secondary':5}
damage_chart['Infantry']['Md. Tank'] = {'Primary':None, 'Secondary':1}
damage_chart['Infantry']['APC'] = {'Primary':None, 'Secondary':14}
damage_chart['Infantry']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':15}
damage_chart['Infantry']['Missiles'] = {'Primary':None, 'Secondary':25}
damage_chart['Infantry']['Rockets'] = {'Primary':None, 'Secondary':5}
damage_chart['Infantry']['Artillery'] = {'Primary':None, 'Secondary':25}
damage_chart['Infantry']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Infantry']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Infantry']['Battle Copter'] = {'Primary':None, 'Secondary':7}
damage_chart['Infantry']['Transport Copter'] = {'Primary':None, 'Secondary':30}
damage_chart['Infantry']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Infantry']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Infantry']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Infantry']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Mech']['Infantry'] = {'Primary':None, 'Secondary':65}
damage_chart['Mech']['Mech'] = {'Primary':None, 'Secondary':55}
damage_chart['Mech']['Recon'] = {'Primary':85, 'Secondary':18}
damage_chart['Mech']['Lt. Tank'] = {'Primary':55, 'Secondary':6}
damage_chart['Mech']['Md. Tank'] = {'Primary':15, 'Secondary':1}
damage_chart['Mech']['APC'] = {'Primary':75, 'Secondary':20}
damage_chart['Mech']['Anti-Air Vehicle'] = {'Primary':70, 'Secondary':32}
damage_chart['Mech']['Missiles'] = {'Primary':85, 'Secondary':35}
damage_chart['Mech']['Rockets'] = {'Primary':65, 'Secondary':6}
damage_chart['Mech']['Artillery'] = {'Primary':85, 'Secondary':35}
damage_chart['Mech']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Mech']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Mech']['Battle Copter'] = {'Primary':None, 'Secondary':9}
damage_chart['Mech']['Transport Copter'] = {'Primary':None, 'Secondary':35}
damage_chart['Mech']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Mech']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Mech']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Mech']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Recon']['Infantry'] = {'Primary':None, 'Secondary':70}
damage_chart['Recon']['Mech'] = {'Primary':None, 'Secondary':65}
damage_chart['Recon']['Recon'] = {'Primary':None, 'Secondary':35}
damage_chart['Recon']['Lt. Tank'] = {'Primary':None, 'Secondary':6}
damage_chart['Recon']['Md. Tank'] = {'Primary':None, 'Secondary':1}
damage_chart['Recon']['APC'] = {'Primary':None, 'Secondary':45}
damage_chart['Recon']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':45}
damage_chart['Recon']['Missiles'] = {'Primary':None, 'Secondary':55}
damage_chart['Recon']['Rockets'] = {'Primary':None, 'Secondary':4}
damage_chart['Recon']['Artillery'] = {'Primary':None, 'Secondary':28}
damage_chart['Recon']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Recon']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Recon']['Battle Copter'] = {'Primary':None, 'Secondary':10}
damage_chart['Recon']['Transport Copter'] = {'Primary':None, 'Secondary':35}
damage_chart['Recon']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Recon']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Recon']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Recon']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Lt. Tank']['Infantry'] = {'Primary':None, 'Secondary':75}
damage_chart['Lt. Tank']['Mech'] = {'Primary':None, 'Secondary':70}
damage_chart['Lt. Tank']['Recon'] = {'Primary':85, 'Secondary':40}
damage_chart['Lt. Tank']['Lt. Tank'] = {'Primary':55, 'Secondary':6}
damage_chart['Lt. Tank']['Md. Tank'] = {'Primary':15, 'Secondary':1}
damage_chart['Lt. Tank']['APC'] = {'Primary':75, 'Secondary':45}
damage_chart['Lt. Tank']['Anti-Air Vehicle'] = {'Primary':70, 'Secondary':45}
damage_chart['Lt. Tank']['Missiles'] = {'Primary':85, 'Secondary':55}
damage_chart['Lt. Tank']['Rockets'] = {'Primary':65, 'Secondary':5}
damage_chart['Lt. Tank']['Artillery'] = {'Primary':85, 'Secondary':30}
damage_chart['Lt. Tank']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Lt. Tank']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Lt. Tank']['Battle Copter'] = {'Primary':None, 'Secondary':10}
damage_chart['Lt. Tank']['Transport Copter'] = {'Primary':None, 'Secondary':40}
damage_chart['Lt. Tank']['Cruiser'] = {'Primary':5, 'Secondary':None}
damage_chart['Lt. Tank']['Battleship'] = {'Primary':1, 'Secondary':None}
damage_chart['Lt. Tank']['Lander'] = {'Primary':10, 'Secondary':None}
damage_chart['Lt. Tank']['Submarine'] = {'Primary':1, 'Secondary':None}

damage_chart['Md. Tank']['Infantry'] = {'Primary':None, 'Secondary':105}
damage_chart['Md. Tank']['Mech'] = {'Primary':None, 'Secondary':95}
damage_chart['Md. Tank']['Recon'] = {'Primary':105, 'Secondary':45}
damage_chart['Md. Tank']['Lt. Tank'] = {'Primary':85, 'Secondary':8}
damage_chart['Md. Tank']['Md. Tank'] = {'Primary':55, 'Secondary':1}
damage_chart['Md. Tank']['APC'] = {'Primary':105, 'Secondary':45}
damage_chart['Md. Tank']['Anti-Air Vehicle'] = {'Primary':105, 'Secondary':45}
damage_chart['Md. Tank']['Missiles'] = {'Primary':105, 'Secondary':55}
damage_chart['Md. Tank']['Rockets'] = {'Primary':105, 'Secondary':7}
damage_chart['Md. Tank']['Artillery'] = {'Primary':105, 'Secondary':35}
damage_chart['Md. Tank']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Md. Tank']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Md. Tank']['Battle Copter'] = {'Primary':None, 'Secondary':12}
damage_chart['Md. Tank']['Transport Copter'] = {'Primary':None, 'Secondary':45}
damage_chart['Md. Tank']['Cruiser'] = {'Primary':55, 'Secondary':None}
damage_chart['Md. Tank']['Battleship'] = {'Primary':10, 'Secondary':None}
damage_chart['Md. Tank']['Lander'] = {'Primary':35, 'Secondary':None}
damage_chart['Md. Tank']['Submarine'] = {'Primary':10, 'Secondary':None}

damage_chart['APC']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['APC']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Anti-Air Vehicle']['Infantry'] = {'Primary':90, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Mech'] = {'Primary':85, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Recon'] = {'Primary':80, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Lt. Tank'] = {'Primary':70, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Md. Tank'] = {'Primary':45, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['APC'] = {'Primary':70, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Anti-Air Vehicle'] = {'Primary':75, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Missiles'] = {'Primary':80, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Rockets'] = {'Primary':75, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Artillery'] = {'Primary':80, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Cruiser'] = {'Primary':65, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Battleship'] = {'Primary':40, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Lander'] = {'Primary':55, 'Secondary':None}
damage_chart['Anti-Air Vehicle']['Submarine'] = {'Primary':60, 'Secondary':None}

damage_chart['Missiles']['Infantry'] = {'Primary':95, 'Secondary':None}
damage_chart['Missiles']['Mech'] = {'Primary':90, 'Secondary':None}
damage_chart['Missiles']['Recon'] = {'Primary':90, 'Secondary':None}
damage_chart['Missiles']['Lt. Tank'] = {'Primary':80, 'Secondary':None}
damage_chart['Missiles']['Md. Tank'] = {'Primary':55, 'Secondary':None}
damage_chart['Missiles']['APC'] = {'Primary':80, 'Secondary':None}
damage_chart['Missiles']['Anti-Air Vehicle'] = {'Primary':80, 'Secondary':None}
damage_chart['Missiles']['Missiles'] = {'Primary':85, 'Secondary':None}
damage_chart['Missiles']['Rockets'] = {'Primary':85, 'Secondary':None}
damage_chart['Missiles']['Artillery'] = {'Primary':90, 'Secondary':None}
damage_chart['Missiles']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Missiles']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Missiles']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Missiles']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Missiles']['Cruiser'] = {'Primary':85, 'Secondary':None}
damage_chart['Missiles']['Battleship'] = {'Primary':55, 'Secondary':None}
damage_chart['Missiles']['Lander'] = {'Primary':60, 'Secondary':None}
damage_chart['Missiles']['Submarine'] = {'Primary':85, 'Secondary':None}

damage_chart['Rockets']['Infantry'] = {'Primary':105, 'Secondary':None}
damage_chart['Rockets']['Mech'] = {'Primary':105, 'Secondary':None}
damage_chart['Rockets']['Recon'] = {'Primary':60, 'Secondary':None}
damage_chart['Rockets']['Lt. Tank'] = {'Primary':25, 'Secondary':None}
damage_chart['Rockets']['Md. Tank'] = {'Primary':10, 'Secondary':None}
damage_chart['Rockets']['APC'] = {'Primary':50, 'Secondary':None}
damage_chart['Rockets']['Anti-Air Vehicle'] = {'Primary':50, 'Secondary':None}
damage_chart['Rockets']['Missiles'] = {'Primary':55, 'Secondary':None}
damage_chart['Rockets']['Rockets'] = {'Primary':45, 'Secondary':None}
damage_chart['Rockets']['Artillery'] = {'Primary':55, 'Secondary':None}
damage_chart['Rockets']['Bomber'] = {'Primary':75, 'Secondary':None}
damage_chart['Rockets']['Fighter'] = {'Primary':65, 'Secondary':None}
damage_chart['Rockets']['Battle Copter'] = {'Primary':120, 'Secondary':None}
damage_chart['Rockets']['Transport Copter'] = {'Primary':120, 'Secondary':None}
damage_chart['Rockets']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Rockets']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Rockets']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Rockets']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Artillery']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Bomber'] = {'Primary':100, 'Secondary':None}
damage_chart['Artillery']['Fighter'] = {'Primary':100, 'Secondary':None}
damage_chart['Artillery']['Battle Copter'] = {'Primary':120, 'Secondary':None}
damage_chart['Artillery']['Transport Copter'] = {'Primary':120, 'Secondary':None}
damage_chart['Artillery']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Artillery']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Bomber']['Infantry'] = {'Primary':110, 'Secondary':None}
damage_chart['Bomber']['Mech'] = {'Primary':110, 'Secondary':None}
damage_chart['Bomber']['Recon'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Lt. Tank'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Md. Tank'] = {'Primary':95, 'Secondary':None}
damage_chart['Bomber']['APC'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Anti-Air Vehicle'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Missiles'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Rockets'] = {'Primary':95, 'Secondary':None}
damage_chart['Bomber']['Artillery'] = {'Primary':105, 'Secondary':None}
damage_chart['Bomber']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Bomber']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Bomber']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Bomber']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Bomber']['Cruiser'] = {'Primary':85, 'Secondary':None}
damage_chart['Bomber']['Battleship'] = {'Primary':75, 'Secondary':None}
damage_chart['Bomber']['Lander'] = {'Primary':95, 'Secondary':None}
damage_chart['Bomber']['Submarine'] = {'Primary':95, 'Secondary':None}

damage_chart['Fighter']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Bomber'] = {'Primary':100, 'Secondary':None}
damage_chart['Fighter']['Fighter'] = {'Primary':55, 'Secondary':None}
damage_chart['Fighter']['Battle Copter'] = {'Primary':100, 'Secondary':None}
damage_chart['Fighter']['Transport Copter'] = {'Primary':100, 'Secondary':None}
damage_chart['Fighter']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Fighter']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Battle Copter']['Infantry'] = {'Primary':None, 'Secondary':75}
damage_chart['Battle Copter']['Mech'] = {'Primary':None, 'Secondary':75}
damage_chart['Battle Copter']['Recon'] = {'Primary':55, 'Secondary':30}
damage_chart['Battle Copter']['Lt. Tank'] = {'Primary':55, 'Secondary':6}
damage_chart['Battle Copter']['Md. Tank'] = {'Primary':25, 'Secondary':1}
damage_chart['Battle Copter']['APC'] = {'Primary':60, 'Secondary':20}
damage_chart['Battle Copter']['Anti-Air Vehicle'] = {'Primary':65, 'Secondary':25}
damage_chart['Battle Copter']['Missiles'] = {'Primary':65, 'Secondary':35}
damage_chart['Battle Copter']['Rockets'] = {'Primary':25, 'Secondary':6}
damage_chart['Battle Copter']['Artillery'] = {'Primary':65, 'Secondary':35}
damage_chart['Battle Copter']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Battle Copter']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Battle Copter']['Battle Copter'] = {'Primary':None, 'Secondary':65}
damage_chart['Battle Copter']['Transport Copter'] = {'Primary':None, 'Secondary':95}
damage_chart['Battle Copter']['Cruiser'] = {'Primary':55, 'Secondary':None}
damage_chart['Battle Copter']['Battleship'] = {'Primary':25, 'Secondary':None}
damage_chart['Battle Copter']['Lander'] = {'Primary':25, 'Secondary':None}
damage_chart['Battle Copter']['Submarine'] = {'Primary':25, 'Secondary':None}

damage_chart['Transport Copter']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Transport Copter']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Cruiser']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Bomber'] = {'Primary':None, 'Secondary':65}
damage_chart['Cruiser']['Fighter'] = {'Primary':None, 'Secondary':55}
damage_chart['Cruiser']['Battle Copter'] = {'Primary':None, 'Secondary':115}
damage_chart['Cruiser']['Transport Copter'] = {'Primary':None, 'Secondary':115}
damage_chart['Cruiser']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Cruiser']['Submarine'] = {'Primary':90, 'Secondary':None}

damage_chart['Battleship']['Infantry'] = {'Primary':95, 'Secondary':None}
damage_chart['Battleship']['Mech'] = {'Primary':90, 'Secondary':None}
damage_chart['Battleship']['Recon'] = {'Primary':90, 'Secondary':None}
damage_chart['Battleship']['Lt. Tank'] = {'Primary':80, 'Secondary':None}
damage_chart['Battleship']['Md. Tank'] = {'Primary':55, 'Secondary':None}
damage_chart['Battleship']['APC'] = {'Primary':80, 'Secondary':None}
damage_chart['Battleship']['Anti-Air Vehicle'] = {'Primary':80, 'Secondary':None}
damage_chart['Battleship']['Missiles'] = {'Primary':85, 'Secondary':None}
damage_chart['Battleship']['Rockets'] = {'Primary':85, 'Secondary':None}
damage_chart['Battleship']['Artillery'] = {'Primary':90, 'Secondary':None}
damage_chart['Battleship']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Battleship']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Battleship']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Battleship']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Battleship']['Cruiser'] = {'Primary':95, 'Secondary':None}
damage_chart['Battleship']['Battleship'] = {'Primary':50, 'Secondary':None}
damage_chart['Battleship']['Lander'] = {'Primary':95, 'Secondary':None}
damage_chart['Battleship']['Submarine'] = {'Primary':95, 'Secondary':None}

damage_chart['Lander']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Cruiser'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Battleship'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Lander'] = {'Primary':None, 'Secondary':None}
damage_chart['Lander']['Submarine'] = {'Primary':None, 'Secondary':None}

damage_chart['Submarine']['Infantry'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Mech'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Recon'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Lt. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Md. Tank'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['APC'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Anti-Air Vehicle'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Missiles'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Rockets'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Artillery'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Bomber'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Fighter'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Battle Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Transport Copter'] = {'Primary':None, 'Secondary':None}
damage_chart['Submarine']['Cruiser'] = {'Primary':25, 'Secondary':None}
damage_chart['Submarine']['Battleship'] = {'Primary':55, 'Secondary':None}
damage_chart['Submarine']['Lander'] = {'Primary':95, 'Secondary':None}
damage_chart['Submarine']['Submarine'] = {'Primary':55, 'Secondary':None}


###############################################################################
### TERRAIN CHART

terrain_chart= defaultdict(dict)

terrain_chart['Mountain']['-4'] = {'damage':None, 'roll': None}
terrain_chart['Mountain']['-3'] = {'damage':None, 'roll': None}
terrain_chart['Mountain']['-2'] = {'damage':None, 'roll': None}
terrain_chart['Mountain']['-1'] = {'damage':0, 'roll': 1}
terrain_chart['Mountain']['0'] = {'damage':0, 'roll': 1}
terrain_chart['Mountain']['1'] = {'damage':0, 'roll': 5}
terrain_chart['Mountain']['2'] = {'damage':1, 'roll': 3}
terrain_chart['Mountain']['3'] = {'damage':2, 'roll': 1}
terrain_chart['Mountain']['4'] = {'damage':2, 'roll': 4}
terrain_chart['Mountain']['5'] = {'damage':3, 'roll': 2}
terrain_chart['Mountain']['6'] = {'damage':3, 'roll': 5}
terrain_chart['Mountain']['7'] = {'damage':4, 'roll': 3}
terrain_chart['Mountain']['8'] = {'damage':5, 'roll': 1}
terrain_chart['Mountain']['9'] = {'damage':5, 'roll': 4}
terrain_chart['Mountain']['10'] = {'damage':6, 'roll': 2}
terrain_chart['Mountain']['11'] = {'damage':6, 'roll': 5}
terrain_chart['Mountain']['12'] = {'damage':7, 'roll': 3}
terrain_chart['Mountain']['13'] = {'damage':8, 'roll': None}

terrain_chart['Rubble']['-4'] = {'damage':None, 'roll': None}
terrain_chart['Rubble']['-3'] = {'damage':None, 'roll': None}
terrain_chart['Rubble']['-2'] = {'damage':None, 'roll': None}
terrain_chart['Rubble']['-1'] = {'damage':0, 'roll': 1}
terrain_chart['Rubble']['0'] = {'damage':0, 'roll': 2}
terrain_chart['Rubble']['1'] = {'damage':1, 'roll': 1}
terrain_chart['Rubble']['2'] = {'damage':1, 'roll': 5}
terrain_chart['Rubble']['3'] = {'damage':2, 'roll': 3}
terrain_chart['Rubble']['4'] = {'damage':3, 'roll': 1}
terrain_chart['Rubble']['5'] = {'damage':3, 'roll': 5}
terrain_chart['Rubble']['6'] = {'damage':4, 'roll': 3}
terrain_chart['Rubble']['7'] = {'damage':5, 'roll': 1}
terrain_chart['Rubble']['8'] = {'damage':5, 'roll': 5}
terrain_chart['Rubble']['9'] = {'damage':6, 'roll': 4}
terrain_chart['Rubble']['10'] = {'damage':7, 'roll': 2}
terrain_chart['Rubble']['11'] = {'damage':8, 'roll': 3}
terrain_chart['Rubble']['12'] = {'damage':None, 'roll': 3}
terrain_chart['Rubble']['13'] = {'damage':None, 'roll': 3}

terrain_chart['Forest']['-4'] = {'damage':None, 'roll': None}
terrain_chart['Forest']['-3'] = {'damage':None, 'roll': None}
terrain_chart['Forest']['-2'] = {'damage':0, 'roll': 1}
terrain_chart['Forest']['-1'] = {'damage':0, 'roll': 2}
terrain_chart['Forest']['0'] = {'damage':0, 'roll': 3}
terrain_chart['Forest']['1'] = {'damage':1, 'roll': 1}
terrain_chart['Forest']['2'] = {'damage':2, 'roll': 1}
terrain_chart['Forest']['3'] = {'damage':2, 'roll': 5}
terrain_chart['Forest']['4'] = {'damage':3, 'roll': 4}
terrain_chart['Forest']['5'] = {'damage':4, 'roll': 2}
terrain_chart['Forest']['6'] = {'damage':5, 'roll': 1}
terrain_chart['Forest']['7'] = {'damage':6, 'roll': 1}
terrain_chart['Forest']['8'] = {'damage':6, 'roll': 5}
terrain_chart['Forest']['9'] = {'damage':7, 'roll': 4}
terrain_chart['Forest']['10'] = {'damage':8, 'roll': None}
terrain_chart['Forest']['11'] = {'damage':None, 'roll': None}
terrain_chart['Forest']['12'] = {'damage':None, 'roll': None}
terrain_chart['Forest']['13'] = {'damage':None, 'roll': None}

terrain_chart['Plains']['-4'] = {'damage':None, 'roll': 3}
terrain_chart['Plains']['-3'] = {'damage':None, 'roll': 3}
terrain_chart['Plains']['-2'] = {'damage':0, 'roll':  1}
terrain_chart['Plains']['-1'] = {'damage':0, 'roll': 2}
terrain_chart['Plains']['0'] = {'damage':0, 'roll': 4}
terrain_chart['Plains']['1'] = {'damage':1, 'roll': 2}
terrain_chart['Plains']['2'] = {'damage':2, 'roll': 2}
terrain_chart['Plains']['3'] = {'damage':3, 'roll': 1}
terrain_chart['Plains']['4'] = {'damage':4, 'roll': 1}
terrain_chart['Plains']['5'] = {'damage':4, 'roll': 5}
terrain_chart['Plains']['6'] = {'damage':5, 'roll': 5}
terrain_chart['Plains']['7'] = {'damage':6, 'roll': 5}
terrain_chart['Plains']['8'] = {'damage':7, 'roll': 4}
terrain_chart['Plains']['9'] = {'damage':8, 'roll': None}
terrain_chart['Plains']['10'] = {'damage':None, 'roll': None}
terrain_chart['Plains']['11'] = {'damage':None, 'roll': None}
terrain_chart['Plains']['12'] = {'damage':None, 'roll': None}
terrain_chart['Plains']['13'] = {'damage':None, 'roll': None}

terrain_chart['Road']['-4'] = {'damage':None, 'roll': None}
terrain_chart['Road']['-3'] = {'damage':0, 'roll': 1}
terrain_chart['Road']['-2'] = {'damage':0, 'roll': 2}
terrain_chart['Road']['-1'] = {'damage':0, 'roll': 3}
terrain_chart['Road']['0'] = {'damage':0, 'roll': 5}
terrain_chart['Road']['1'] = {'damage':1, 'roll': 3}
terrain_chart['Road']['2'] = {'damage':2, 'roll': 3}
terrain_chart['Road']['3'] = {'damage':3, 'roll': 3}
terrain_chart['Road']['4'] = {'damage':4, 'roll': 3}
terrain_chart['Road']['5'] = {'damage':5, 'roll': 3}
terrain_chart['Road']['6'] = {'damage':6, 'roll': 3}
terrain_chart['Road']['7'] = {'damage':7, 'roll': 3}
terrain_chart['Road']['8'] = {'damage':8, 'roll': None}
terrain_chart['Road']['9'] = {'damage':None, 'roll': None}
terrain_chart['Road']['10'] = {'damage':None, 'roll': None}
terrain_chart['Road']['11'] = {'damage':None, 'roll': None}
terrain_chart['Road']['12'] = {'damage':None, 'roll': None}
terrain_chart['Road']['13'] = {'damage':None, 'roll': None}

terrain_chart['Water']['-4'] = {'damage':None, 'roll': None}
terrain_chart['Water']['-3'] = {'damage':0, 'roll': 1}
terrain_chart['Water']['-2'] = {'damage':0, 'roll': 2}
terrain_chart['Water']['-1'] = {'damage':0, 'roll': 3}
terrain_chart['Water']['0'] = {'damage':0, 'roll': 5}
terrain_chart['Water']['1'] = {'damage':1, 'roll': 3}
terrain_chart['Water']['2'] = {'damage':2, 'roll': 3}
terrain_chart['Water']['3'] = {'damage':3, 'roll': 3}
terrain_chart['Water']['4'] = {'damage':4, 'roll': 3}
terrain_chart['Water']['5'] = {'damage':5, 'roll': 3}
terrain_chart['Water']['6'] = {'damage':6, 'roll': 3}
terrain_chart['Water']['7'] = {'damage':7, 'roll': 3}
terrain_chart['Water']['8'] = {'damage':8, 'roll': None}
terrain_chart['Water']['9'] = {'damage':None, 'roll': None}
terrain_chart['Water']['10'] = {'damage':None, 'roll': None}
terrain_chart['Water']['11'] = {'damage':None, 'roll': None}
terrain_chart['Water']['12'] = {'damage':None, 'roll': None}
terrain_chart['Water']['13'] = {'damage':None, 'roll': None}



###############################################################################

config = ConfigParser.ConfigParser()
config.read('config.ini')

attacker_race = config.get('attacker', 'race')
attacker_type = config.get('attacker', 'type')
attacker_hp = config.getint('attacker', 'hp')
attacker_terrain = config.get('attacker', 'terrain')
attacker_weapon = config.get('attacker', 'weapon')
attacker_level = config.get('attacker', 'level')

defender_race = config.get('defender', 'race')
defender_type = config.get('defender', 'type')
defender_hp = config.getint('defender', 'hp')
defender_terrain = config.get('defender', 'terrain')
defender_weapon = config.get('defender', 'weapon')
defender_level = config.get('defender', 'level')

# print 'attacker_type: ' + attacker_type
# print 'attacker_hp: ' + str(attacker_hp)
# print 'attacker_terrain: ' + attacker_terrain
# print 'defender_type: ' + defender_type
# print 'defender_hp: ' + str(defender_hp)
# print 'defender_terrain: ' + defender_terrain

base_damage = damage_chart[attacker_type][defender_type][attacker_weapon]
if base_damage is not None:
    base_damage = base_damage * (attacker_hp / 10)

    # print '\n\n'
    # print 'base_damage: ' + str(base_damage)
    
    terrain = terrain_chart[defender_terrain][str(int(base_damage / 10))]
    damage = terrain['damage']

    if damage is not None:
        # print 'damage: ' + str(damage)
        r = random.randint(1,6)
        if r < terrain_chart[defender_terrain][str(int(base_damage / 10))]['roll']:
            damage = damage + 1
    else:
            damage = 0
else:
    damage = 0

if attacker_race == 'Monster' and defender_race == 'Building':
    damage = damage * 1.5
elif attacker_race == 'Robot' and defender_race == 'Monster':
    damage = damage * 1.5

if attacker_level == 2:
    damage = damage * 1.5
elif attacker_level == 3:
    damage = damage * 2.25

# print 'final damage: ' + str(damage)
defender_hp = defender_hp - damage
print 'defender_hp: ' + str(defender_hp)

base_damage = damage_chart[defender_type][attacker_type][defender_weapon]
if base_damage is not None:
    base_damage = base_damage * (defender_hp / 10)
    # print '\n\n'
    # print 'base_damage: ' + str(base_damage)
    damage = terrain_chart[attacker_terrain][str(int(base_damage / 10))]['damage']

    if damage is not None:
        # print 'damage: ' + str(damage)
        r = random.randint(1,6)
        if r < terrain_chart[attacker_terrain][str(int(base_damage / 10))]['roll']:
            damage = damage + 1
    else:
        damage = 0
else:
    damage = 0

if defender_level == 2:
    damage = damage * 1.5
elif defender_level == 3:
    damage = damage * 2.25

# print 'final damage: ' + str(damage)
attacker_hp = attacker_hp - damage
print 'attacker_hp: ' + str(attacker_hp)