import scholarly
def cobaaja(Rutgers, 3349):
		search_query = scholarly.search_author('Rutgers, 3349')
		return next(search_query)


