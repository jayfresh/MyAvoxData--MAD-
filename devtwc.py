config = {
    'log_level': 'DEBUG',
    'secret': 'the bees are in the what',
    'system_plugins': [
        'tiddlywebplugins.wikidata',
        'tiddlywebplugins.methodhack',
        'tiddlywebplugins.pathinfohack',
        'tiddlywebplugins.static', # a development trick so I can use CherryPy - symlink your static folder here
    ],
    'maps_api_key': 'ABQIAAAAfIA5i-5lcivJMUvTzLDrmxRO20Db7Xdd4lc_seIy4R9wZKUPyhSJfJnlwAdfjEPLHleUU5PcZhxZxA', # http://myavoxdata.com/
	'server_host': {
		'host': 'test.myavoxdata.com',
		'scheme': 'http',
		'port': '80',
	},
	'mappingsql.tasters': True,
	'mappingsql.open_fields': [
		'avid',
		'avox_match_status',
		'avox_entity_class',
		'avox_entity_type',
		'record_source',
		'legal_name',
		'previous_name_s_',
		'trades_as_name_s_',
		'name_notes',
		'legal_form',
		'trading_status',
		'swift_bic',
		'vat_number',
		'tax_payer_id',
		'company_website',
		'regulated_by',
		'regulator_id',
		'regulatory_status',
		'registration_authority',
		'registration_number__operational_',
		'registration_number__jurisdiction_',
		'date_of_registration',
		'date_of_dissolution',
		'issuer_flag',
		'primary_listing_exchange',
		'ticker_code',
		'cabre', # this is not being used
		'fiscal_year_end',
		'mifid_source',
		'balance_sheet_date',
		'balance_sheet_currency',
		'balance_sheet_total',
		'annual_net_turnover',
		'own_funds',
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
		'operational_address_notes',
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
		'registered_address_notes',
		'naics_code',
		'naics_description',
		'us_sic_code',
		'us_sic_description',
		'nace_code',
		'nace_description',
		'entity_type',
		'immediate_parent_avid',
		'immediate_parent_name',
		'immediate_parent_percentage',
		'immediate_parent_notes',
		'ultimate_parent_avid',
		'ultimate_parent_name',
		'ultimate_parent_notes',
		'general_notes',
	],
}
