from text_editor.action import Action

class File:
    undo_stack: Action = []
    redo_stack: Action = []
    

    def __init__(self, capacity):
        self.capacity = capacity
        self.file_list = [""] * capacity


    def insert_text(self, line_num: int, text: str):

        if line_num > self.capacity:
            print("---Line passed is bigger than the file length-----")
        else:
            file_list[line_num] = text
            print("----text inserted---")



    def delete_text(self, line_num: int):
        if line_num > self.capacity:
            print("---Line passed is bigger than the file length-----")
        elif self.file_list[line_num] == "":
            print(f" Line number passed {line_num} does not contain any text")
    
    def copy_text(self, line_num: int):
        pass
    
    def paste_text(self, line_num: int):
        pass
    
    def delete_file(self):
        pass
    
    def display_file(self):
        pass
    
    def undo(self):
        pass
    
    def redo(self):
        pass