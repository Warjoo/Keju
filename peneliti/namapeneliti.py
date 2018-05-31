import scholarly
def coba(nama):
		search_query = scholarly.search_author('nama')
		return next(search_query)


