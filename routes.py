def mad(environ, start_response):
    
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Pragma', 'no-cache')
        ])
    
    return "hi!"


def init(config):
    config['selector'].add('/mad', GET=mad)
