import http.server as hs, socketserver as so
with so.TCPServer(("0.0.0.0", 8080), hs.SimpleHTTPRequestHandler) as hd: hd.serve_forever()