config = {
    'log_level': 'DEBUG',
    'secret': 'the bees are in the what',
    'system_plugins': [
        'tiddlywebplugins.wikidata',
        'tiddlywebplugins.methodhack',
        'tiddlywebplugins.pathinfohack',
        'tiddlywebplugins.static', # a development trick so I can use CherryPy - symlink your static folder here
    ],
    'server_store': ['tiddlywebplugins.diststore', {
            'main': ['text', {'store_root': 'store'}],
            'extras': [
                (r'^avox$', ['tiddlywebplugins.wikidata.madsql',
                    {'db_config': 'mysql://avox@localhost/avox?charset=utf8'}]),
                    #{'db_config': 'sqlite:///test.db'}]),
                ],
            }],
    'twanager_plugins': ['tiddlywebplugins.wikidata'],
    'maps_api_key': 'ABQIAAAAfIA5i-5lcivJMUvTzLDrmxRO20Db7Xdd4lc_seIy4R9wZKUPyhSJfJnlwAdfjEPLHleUU5PcZhxZxA', # http://myavoxdata.com/
	'server_host': {
		'host': 'test.myavoxdata.com',
		'scheme': 'http',
		'port': '80',
	},
	'mappingsql.tasters': True,
	'mappingsql.open_fields': [
		'avid',
		'legal_name',
		'previous_name_s_',
		'trades_as_name_s_',
		'trading_status',
		'swift_bic',
		'company_website',
		'registration_number__jurisdiction_',
		'primary_listing_exchange',
		'ticker_code',
		'operational_po_box',
		'operational_floor',
		'operational_building',
		'operational_street_1',
		'operational_street_2',
		'operational_street_3',
		'operational_city',
		'operational_state',
		'operational_country', # "ISO country code" previously, changed to reflect display of country name
		'operational_postcode',
		'registered_agent_name',
		'registered_po_box',
		'registered_floor',
		'registered_building',
		'registered_street_1',
		'registered_street_2',
		'registered_street_3',
		'registered_city', # "Registered City" previously, changed for consistency
		'registered_state',
		'registered_country',
		'registered_postcode',
		'naics_code',
		'naics_description',
		'us_sic_code',
		'us_sic_description',
		'entity_type',
		'immediate_parent_avid',
		'immediate_parent_name',
		'ultimate_parent_avid',
		'ultimate_parent_name',
	],
}
