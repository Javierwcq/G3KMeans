from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

'''
Claves y tokens de acceso para descarga stream twitter data
'''
consumer_key = 'PXsmITcYQ3RBMLP4qYbvTbPkY'
consumer_secret = 'wZyBPc5KN7x5KLPvP1VWBIRT8EXq7ahfeUuzx3syHrBfkuehmK'
access_token = '4842123455-NMSCL1TtuzL9UmYibCtyESlCiolLP8ziz22k44B'
access_token_secret = 'Ax48lHhIWNtrKx1VFW7Oa8IIAv9h5dcAYH9GZhZ5xmLmH'

'''
Clase de libreria Tweppy para descarga, almacena en un archivo json
'''
class listener(StreamListener):   
    def on_data(self, cadena_json):      
        archivo = open('datos.json','a')
        archivo.write(json.dumps(json.loads(cadena_json),indent=2))       
        archivo.close()        
        return True

'''
Autenticacion
'''   
autenticacion = OAuthHandler(consumer_key, consumer_secret)
autenticacion.set_access_token(access_token, access_token_secret) 
stream_twitter = Stream(autenticacion, listener())
stream_twitter.filter(track=['WWE','wwe','#wwe','@wwe'])

