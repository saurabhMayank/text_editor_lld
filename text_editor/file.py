from text_editor.action import Action
from text_editor.errors import SizeOutofBoundsError, TextNotFoundError, NoTextCopiedError

class File:
    undo_stack: Action = []
    redo_stack: Action = []
    

    def __init__(self, capacity):
        self.capacity = capacity
        self.file_list = [""]*self.capacity
        # copy_var is a empty string
        self.copy_var = ""


    def insert_text(self, line_num: int, text: str):
        """
        Insert text into single line
        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
            print("\n")
        else:
            # file_list is 0 indexed that is why
            self.file_list[line_num-1] = text
            print("----display file---")
            print("\n")
            self.display_file()
    
    def insert_text_multiple_lines(self, text_line_dict: dict):
        """
        Insert text into multiple lines
        """
        for line_num, text in text_line_dict.items():
            self.insert_text(line_num, text)

    def delete_text(self, line_num: int):
        """
        Delete text from a single line
        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
            print("\n")
        elif self.file_list[line_num-1] == "":
            raise TextNotFoundError(f" Line number passed {line_num} does not contain any text")
        else:
            self.file_list[line_num-1] = ""
        
        print("----display file---")
        print("\n")
        self.display_file()
    
    def copy_text(self, line_num: int):
        """
        Copy text into single line
        """
        if line_num > self.capacity:
            raise SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
        elif self.file_list[line_num-1] == "":
            raise TextNotFoundError(f" Line number passed {line_num} does not contain any text")
        else:
            if len(self.copy_var) > 0:
                # if there is an element already in copy_var
                # remove that element so we can store the next one
                self.copy_var = ""
            self.copy_var = self.file_list[line_num-1]
    
    def paste_text(self, line_num: int):
        """
        Paste text into single line
        """
        if not self.copy_var:
            raise NoTextCopiedError("Nothing copied, Please copy first")
        elif line_num > self.capacity:
            SizeOutofBoundsError(f"Line Num {line_num} passed is bigger than the file length")
        else:
            self.file_list[line_num-1] = self.copy_var
            print("----display file---")
            print("\n")
            self.display_file()


    def delete_file(self):
        """
        Delete the whole file and display it
        """
        # reassign the list to empty value
        # for all indexes
        self.file_list = [0]*self.capacity

        self.display_file()

    
    def display_file(self):
        for i, item in enumerate(self.file_list, start=1):
            print(f"{i}. {item}")
    
    def undo(self):
        pass
    
    def redo(self):
        pass