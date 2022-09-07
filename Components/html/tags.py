class Tag:
    def __init__(self,body=None,**kwargs) -> None:
        self.name = kwargs.get('name')
        self._class = kwargs.get('classname', '')
        self.id = kwargs.get('id','')
        self.style = kwargs.get('style', '')
        self.body = body #if you want to create an empty tag, then assign empty to body
        self.misc = kwargs.get('misc','') # this is a list containing all other tag variable such as required etc in string format
        self.href = kwargs.get('href', '')
        if self.misc is not None:
            self.misclist = "".join(i+" " for i in self.misc)
        
    def create(self):
        if self.body is None:
            return f'<{self.name}  href="{self.href}" class="{self._class}" id = "{self.id}" {self.misclist}/>'
        elif self.body == 'empty':
            return f'<{self.name} href="{self.href}" class="{self._class}" id = "{self.id}" {self.misclist}></{self.name}>'
        else:
            return f'<{self.name} href="{self.href}" class="{self._class}" id = "{self.id}" {self.misclist}>{self.body}</{self.name}>'
    
    def __str__(self) -> str:
        return self.create()
    
    def __repr__(self) -> str:
        return self.create()
    
class Header(Tag):
    def __init__(self,type_=None , body=None, **kwargs) -> None:
        super().__init__( body, **kwargs)
        self.type_ = type_ 
        if isinstance(self.type_, int):
            self.name = f"h{self.type_}"
        else:
            self.name = 'header'
        self.create()

def h_tag(type_=None, body=None, **kwargs):
    param_dict = kwargs
    tag_obj = Header(type_, body, **param_dict).create()
    return tag_obj

class Paragraph(Tag):
    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'p'
        self.create()

def p_tag(body=None, **kwargs):
    param_dict = kwargs 
    tag_obj = Paragraph(body,**param_dict).create()
    return tag_obj

class Division(Tag):
    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'div'
        self.create()
    
def div(body=None, **kwargs):
    param_dict = kwargs
    tag_obj = Division(body, **param_dict).create()
    return tag_obj

def make_tag(name:str,**kwargs):
    if not isinstance(name, str):
        raise ValueError(f'expected string object got {type(name)}')
    param_dict = kwargs
    new_tag = Tag(name=name, **param_dict).create()
    return new_tag

