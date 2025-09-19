from abc import ABC, abstractmethod


class Editor:
    def __init__(self):
        self.content = ""

    def write(self, text:str):
        self.content += text
        print(f"Editor content: {self.content}")
    def delete(self,text:str):
        if self.content.endswith(text):
            self.content = self.content[:-len(text)]
        print(f"Editor content: {self.content}")
    
class Command(ABC):

    @abstractmethod    
    def excute(self):pass

    @abstractmethod    
    def revert(self):pass    


class WriteCommand(Command):
    
    def __init__(self, editor:Editor, text:str):
        self.text = text
        self.editor = editor
        
    def excute(self):
        self.editor.write(self.text)
    
    def revert(self):
        self.editor.delete(self.text)
    
class CommandManager:
    
    def __init__(self):
        self.undo_stack:list[Command] = []
        self.redo_stack:list[Command] = []
        
    def execute(self, command:Command):
        command.excute()
        if(len(self.undo_stack) == 2):
            self.undo_stack.pop(0)
        self.undo_stack.append(command)
        self.redo_stack.clear()
    
    def undo(self):
        if(len(self.undo_stack) == 0): return
        command = self.undo_stack.pop()
        command.revert()
        self.redo_stack.append(command)
        
    def redo(self):
        if(len(self.redo_stack) == 0): return
        command = self.redo_stack.pop()
        command.excute()
        self.undo_stack.append(command)

manager = CommandManager()
editor = Editor()
manager.execute(WriteCommand(editor,"A"))
manager.execute(WriteCommand(editor,"B"))
manager.execute(WriteCommand(editor,"C"))

manager.undo()
manager.undo()
manager.undo()

manager.redo()
manager.redo()
manager.redo()


