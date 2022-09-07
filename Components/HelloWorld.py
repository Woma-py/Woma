from html.htmlcontent import HtmlShell,HtmlSkeleton
from html.tags import Header,div,h_tag,make_tag

"""
So here i will demonstrate the usage of these stuffs 
i will create a webpage with script, style and three sections, header, body,footer
"""

#creating the head section
mainObj = HtmlShell(title='Woma.py Tutorial', sfl=['./index.js',], link_css=['./index.css'])

#creating the body contents, one div, one header and one footer, I will use the HtmlSkeleton
body = HtmlSkeleton()

#now i will use the h_tag function to make a header tag, h_tag function is equivalent to Header class
header = h_tag(body="This is how to make an html file in woma.py", classname='headman',) #note h_tag defaults to header, if you want h1 or the likes specify the type_
center = div(body="woma is the best python frontend framework yet, and the most famous", classname='middle') #creating a div element

footer = make_tag('footer',body="powered by team woma", classname="foot") #creating a custom tag that doesn't exist yet in the tags module

#Now i will add the elements sequentially to the skeleton, the skeleton remembers insertion order

body.add(header, name='header') # the name arguments allows you to remove any tag, obj.remove(<name>)
body.add(center, name='center')
body.add(footer, name='footer')

# now to add the style i will use a style string
style_string = """
<style>
body{
    margin: 0;
    padding: 0;
}
.headman, .middle, .foot{
    display: block;
    padding: 10px;
    background-color: aqua;
    color: chocolate;
    margin: 6px solid black;
    width: 200px;
}

.headman, .foot, .middle:hover{
    background-color: chocolate;
    color: aquamarine;
}
*{
    box-sizing: border-box;
}
</style>
"""
body.load_string(style_string) #added styling

#now to wrap it all as a body element

body.wrap('body')

#c'est fini, now put this into the shell
mainObj.insert(body)
mainObj.to_file()