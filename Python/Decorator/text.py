from abc import ABC, abstractmethod

class TextComponent(ABC):
    @abstractmethod
    def render(self):pass

class Text(TextComponent):
    def __init__(self, content):
        self.content = content
    def render(self):
        return self.content
       
class Decorator(TextComponent):
    def __init__(self, component:TextComponent):
        self.component = component
    def render(self):
        self.component.render()

class Bold(Decorator):
    
    def __init__(self, component:TextComponent):
        super().__init__(component)
    
    def render(self):
        return f"<b>{self.component.render()}</b>"
    
    
class Underline(Decorator):    
    def __init__(self, component:TextComponent):
        super().__init__(component)
    def render(self):
        return f"<u>{self.component.render()}</u>"
 
text = Text("Ranjit")
boldText = Bold(text)
print(boldText.render())

uboldText = Underline(Bold(text))
print(uboldText.render())



