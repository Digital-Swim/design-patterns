from abc import ABC, abstractmethod

# Base component interface
class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete component - plain text
class PlainText(TextComponent):
    def __init__(self, text: str):
        self._text = text
    
    def render(self) -> str:
        return self._text

# Base decorator class
class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component
    
    def render(self) -> str:
        return self._component.render()

# Concrete decorators
class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{self._component.render()}</b>"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{self._component.render()}</u>"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{self._component.render()}</i>"

# Example usage
if __name__ == "__main__":
    # Create base text
    text = PlainText("Hello, World!")
    print(f"Plain text: {text.render()}")
    
    # Apply single decoration
    bold_text = BoldDecorator(text)
    print(f"Bold text: {bold_text.render()}")
    
    # Chain multiple decorators
    bold_underline_text = UnderlineDecorator(BoldDecorator(text))
    print(f"Bold + Underline: {bold_underline_text.render()}")
    
    # More complex chaining
    fancy_text = ItalicDecorator(UnderlineDecorator(BoldDecorator(text)))
    print(f"Bold + Underline + Italic: {fancy_text.render()}")
    
    # You can also wrap different text
    another_text = PlainText("Python is awesome!")
    styled_text = BoldDecorator(UnderlineDecorator(another_text))
    print(f"Another example: {styled_text.render()}")
    
    # Demonstrate that decorators can be applied in any order
    different_order = BoldDecorator(ItalicDecorator(UnderlineDecorator(PlainText("Order matters!"))))
    print(f"Different order: {different_order.render()}")