from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode("utf-8")

if str(html).count("C++") > str(html).count("Python"):
    print("C++: ", str(html).count("C++"))
else:
    print("Python: ", str(html).count("Python"))