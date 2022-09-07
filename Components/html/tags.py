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
    def __init__(self,type_ , body=None, **kwargs) -> None:
        super().__init__( body, **kwargs)
        self.type_ = type_ 
        if isinstance(self.type_,int):
            self.name = f"h{self.type_}"
        else:
            self.name = 'header'
        self.create()


class H1(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=1,  body, **kwargs)
        self.type_ = 1 
        self.name = 'h1'
        self.create()

class H2(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=2,  body, **kwargs)
        self.type_ = 2 
        self.name = 'h2'
        self.create()

class H3(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=3,  body, **kwargs)
        self.type_ = 3 
        self.name = 'h3'
        self.create()

class H4(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=4,  body, **kwargs)
        self.type_ = 4 
        self.name = 'h4'
        self.create()

class H5(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=5,  body, **kwargs)
        self.type_ = 5 
        self.name = 'h5'
        self.create()

class H6(Header):
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=6,  body, **kwargs)
        self.type_ = 6 
        self.name = 'h6'
        self.create()
