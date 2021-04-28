#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
INPUT_TEXT = form.getvalue('INPUT_TEXT')


def ohash(s):
    ans = 0
    for c in s:
        ans = ans * 123417 + ord(c)
    return ans


form = cgi.FieldStorage()
text = form.getfirst("INPUT_TEXT", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Введите Python</title>
        </head>
        <body>""")

print("""<form action="/cgi-bin/ScriptTask.py">
        <input type="text" name="INPUT_TEXT">
        <input type="submit">
    </form>
""")

print("<h1>" + str(ohash(INPUT_TEXT)) + "</h1>")

print("""</body>
        </html>""")
