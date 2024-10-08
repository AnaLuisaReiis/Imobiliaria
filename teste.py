import http.server
import ssl

server_address = ('', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Configuração moderna com SSLContext
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:4443")
httpd.serve_forever()
