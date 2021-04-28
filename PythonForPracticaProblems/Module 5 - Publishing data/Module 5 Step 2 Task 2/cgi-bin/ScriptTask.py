#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text = form.getfirst("INPUT_TEXT", "не задано")
text = text[:-1]

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>""")

print("""<form action="/cgi-bin/ScriptTask.py">
        <input type="text" name="INPUT_TEXT">
        <input type="submit">
    </form>
""")

print("<h1>" + str(hash(text)) + "</h1>")

print("""</body>
        </html>""")