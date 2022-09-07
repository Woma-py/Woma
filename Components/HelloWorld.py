from html.htmlcontent import HtmlShell,HtmlSkeleton
from html.tags import Header

head = Header(type_=1, body="Welcome to Woma.py").create() # equivalent to <h1>Welcome to woma.py</h1>

skl =  HtmlSkeleton()
skl.add(head)
shell = HtmlShell(title='PLayground')
shell.insert(skl)
shell.to_file()

"""
alternatively you could do this
create a shell instance
sh = HtmlShell(title='whatever')
sh.insert('<h1>Hello world</h1>')
sh.to_file()

or you could use the html skeleton directly; battery low later i will fine tune the processes
"""