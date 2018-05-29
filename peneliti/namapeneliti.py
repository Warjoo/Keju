import scholarly
def cobaaja(Rutgers):
		search_query = scholarly.search_author('Rutgers')
		return next(search_query)


