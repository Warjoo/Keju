import scholarly

def A(Manish Singh):
        search_query = scholarly.search_author('Manish Singh')
	print(next(search_query))
        {'_filled': False,
         'affiliation': 'Rutgers University, New Brunswick, NJ',
         'citedby': 3349,
         'email': '@ruccs.rutgers.edu',
         'id': '9XRvM88AAAAJ',
         'interests': ['Human perception', 'Computational Vision', 'Cognitive Science'],
         'name': 'Manish Singh',
         'url_picture': '/citations/images/avatar_scholar_56.jpg'}
def B(Oussama Khatib):
        search_query = scholarly.search_author('Oussama Khatib')      
	print(next(search_query))
        {'_filled': False,
         'affiliation': 'Stanford University',
         'citedby': 27493,
         'email': '@cs.stanford.edu',
         'id': '4arkOLcAAAAJ',
         'interests': ['Robotics', 'Haptics', 'Human Motion'],
         'name': 'Oussama Khatib',
         'url_picture': '/citations/images/avatar_scholar_56.jpg'}
def C(Chris):
        search_query = scholarly.search_author('Chris')
	return next(search_query)
def D(Juliffer):
	search_query = scholarly.search_author('Juliffer')
	return next(search_query)
def E(Roza):
	search_query = scholarly.search_author('Roza')
	return next(search_query)
