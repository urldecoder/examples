import urllib 
url = u'http://example.com/?param=url%20decode'
urllib.unquote( url ).decode( 'utf8' ) 
print urllib.unquote( url ).decode( 'utf8' )
