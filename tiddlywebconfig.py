config = {
        'log_level': 'DEBUG',
        'secret': 'the bees are in the what',
        'system_plugins': [
            'tiddlywebplugins.wikidata',
            'tiddlywebplugins.methodhack',
            'tiddlywebplugins.pathinfohack',
            'tiddlywebplugins.static', # a development trick so I can use CherryPy - symlink your static folder here
            'routes'
        ],
        'maps_api_key': 'ABQIAAAAfIA5i-5lcivJMUvTzLDrmxQg7wZe1qASdla1M-DFyiqfOoWRghT6gGJohIOLIoy-3oR7sKWQfPvlxA', # http://wiki-data.com/
	'server_host': {
		'host': 'test.myavoxdata.com',
		'scheme': 'http',
		'port': '80',
	},
}