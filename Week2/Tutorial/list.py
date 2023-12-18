planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto") # Add Pluto to öist
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets) # Number of items in list
jupiter_index = planets.index("Jupiter") # Find Jupiter in list, get index
print("The third planet is", planets[2]) # Print third planet
print("There are", number_of_planets, "planets in the solar system.")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
#Join two lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)