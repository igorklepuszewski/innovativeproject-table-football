import http.client
import ssl
from requests import Request, Session
from base64 import b64encode

serverUrl = "192.168.100.18"
keyStorePassword = "tablefootballclient"
trustStorePassword = "changeit"
basicAuthLogin = "sensor"
basicAuthPassword = "sensor"

d = "x: 1 y:1 z:1"

userAndPass = b64encode(b"sensor:sensor").decode("ISO-8859-1")
header= { 'Authorization' : 'Basic %s' %  userAndPass }

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile="certificate.pem", keyfile="keyfile.pem", password=keyStorePassword)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

conn = http.client.HTTPSConnection(serverUrl, port=8443, context=context)
conn.request("POST","/sensor/", body=d, headers=header)

response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(d)
conn.close()


