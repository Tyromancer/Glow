def format_cities(cities):
	cities_dict_by_state = {}
	for c in cities:
		#	format of c: [city name], [state abbr]
		if c[1] in cities_dict_by_state:
			cities_dict_by_state[c[1]].append(c[0])
		else:
			cities_dict_by_state[c[1]] = [c[0]]
	return cities_dict_by_state