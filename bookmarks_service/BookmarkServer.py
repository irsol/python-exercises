import http.server
import requests
import os
from urllib.parse import unquote, parse_qs
import threading
from socketserver import ThreadingMixIn


class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."

memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
'''


def CheckURI(uri, timeout=5):
    #Check whether this URI is reachable.
    try:
        req = requests.get(uri, timeout=5)
        if req.status_code == 200:
            return True
        else:
            return False
    except:
        return False


class Shortener(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # A GET request will either be for / (the root path) or for /some-name.
        # Strip off the / and we have either empty string or a name.
        name = unquote(self.path[1:])

        if name:
            if name in memory:
                # Send a 303 redirect to the long URI in memory[name].
                self.send_response(303)
                self.send_header('Location', memory[name])
                self.end_headers()
            else:
                # If we don't know that name! Send a 404 error.
                self.send_response(404)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write("I don't know '{}'.".format(name).encode())       

        else:
            # Root path. Send the form.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # List the known associations in the form.
            known = "\n".join("{} : {}".format(key, memory[key])
                              for key in sorted(memory.keys()))
            self.wfile.write(form.format(known).encode())

    def do_POST(self):
        # Decode the form data.
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)

        # Check that the user submitted the form fields.
        if "longuri" not in params or "shortname" not in params:
            # 3. Serve a 400 error with a useful message.
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Something is missing!!".encode())
            return
        longuri = params["longuri"][0]
        shortname = params["shortname"][0]

        if CheckURI(longuri):
            # This URI is good!  Remember it under the specified name.
            memory[shortname] = longuri

            # Serve a redirect to the root page (the form).
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

        else:
            # Didn't successfully fetch the long URI.
            # Send a 404 error with a useful message.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Wrong url!! '{}' ".format(longuri).encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
