from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):pass
    
class Checkbox(ABC):
    @abstractmethod
    def render(self):pass


class WindowsButton(Button):
    def render(self):
        print("Windows button")
        pass

class WindowsCheckbox(Checkbox):
    def render(self):
        return WindowsCheckbox()
    
    
class GuiFactory(ABC):
    @abstractmethod
    def createButton(self)->Button:pass
    
    @abstractmethod
    def createCheckbox(self):pass

class WindowsFactory(GuiFactory):
    def createButton(self) -> Button:
        print("Creating windows button")
        return WindowsButton()
    
    def createCheckbox(self):
        return WindowsCheckbox()
    
    
    
def createGui(factory:GuiFactory):
    return (factory.createButton(), factory.createCheckbox() )


btn, chb = createGui(WindowsFactory())
btn.render()