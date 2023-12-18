planet = { #Create a dictionary
    'name': 'Earth',
    'moons': 1
}
planet.update({'name': 'Makemake'}) #Update the value of the key 'name'
print(planet.get('name')) #Returns none if nothing available
print(planet['moons']) #Returns error if nothing available
print(f'{planet["name"]} has {planet["moons"]} moon(s)')