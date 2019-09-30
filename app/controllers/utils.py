from app import db
from app.models import User

def format_cities(cities):
	cities_dict_by_state = {}
	for c in cities:
		#	format of c: [city name], [state name], [state code]
		if c[1] in cities_dict_by_state:
			cities_dict_by_state[c[1]].append(c[0])
		else:
			cities_dict_by_state[c[1]] = [c[0]]
	return cities_dict_by_state
	
def format_demands(demands):
	formatted_demands = []
	for d in demands:
		one_demand = {}
		one_demand['username'] = db.session.query(User.username).filter(User.id==d[0]).one()[0]
		if d[1] == 0:
			one_demand['role'] = 'Photographer'
		elif d[1] == 1:
			one_demand['role'] = 'Model'
		else:
			one_demand['role'] = 'Other'
		
		if d[2] == 0:
			one_demand['goal'] = 'Photographer'
		elif d[2] == 1:
			one_demand['goal'] = 'Model'
		else:
			one_demand['goal'] = 'Other'
		
		one_demand['price'] = 'Free' if d[3] == None else d[3]
		
		formatted_demands.append(one_demand)
	return formatted_demands