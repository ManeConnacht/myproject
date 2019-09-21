mystring = "Bla\n\t bla\n\t bla\n Bla"
name = "Vasya pupkin"

print(mystring + name)
print(name.title())
print (name.upper())
print (name.lower())

link = "<loc>http://atv.dilerz.ru/mistake</loc>"
link1 = link.strip('<loc>')
link2 = link1.strip('</')
print (link2)
print(mystring)
print(name.lstrip('V'))
print(name.rstrip('kin'))
