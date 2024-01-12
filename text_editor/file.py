from text_editor.action import Action

class File:
    undo_stack: Action = []
    redo_stack: Action = []
    

    def __init__(self, capacity):
        self.capacity = capacity
        self.file_list = [""]*self.capacity
        # copy_var is a list
        # list will always contain 1 element
        # that is the current copied text
        self.copy_var = []


    def insert_text(self, line_num: int, text: str):
        if line_num > self.capacity:
            print(f"---Line Num {line_num} passed is bigger than the file length-----")
            print("")
        else:
            # file_list is 0 indexed that is why
            print("---line_num")
            self.file_list[line_num-1] = text
            print("----text inserted---")
            print("\n")
            print("----display file---")
            print("\n")
            self.display_file()
    
    def insert_text_multiple_lines(self, text_line_dict: dict):
        for line_num, text in text_line_dict:
            insert_text(line_num, text)

    def delete_text(self, line_num: int):
        if line_num > self.capacity:
            print("---Line passed is bigger than the file length-----")
        elif self.file_list[line_num] == "":
            print(f" Line number passed {line_num} does not contain any text")
        else:
            self.file_list[line_num-1] = ""
        
        print("----display file---")
        print("\n")
        self.display_file()
    
    def copy_text(self, line_num: int):
        if line_num > self.capacity:
            print("---Line passed is bigger than the file length-----")
        elif self.file_list[line_num-1] == "":
            print(f" Line number passed {line_num} does not contain any text")
        else:
            if self.copy_var.size() > 0:
                # pop the element and store next one
                self.copy_var.pop()
            self.copy_var.append(self.file_list[line_num-1])
    
    def paste_text(self, line_num: int):
        if self.copy_var_pair.size() == 0:
            print("Nothing copied, Please copy first")
        elif line_num > self.capacity:
            print("---Line passed is bigger than the file length-----")
        else:
            self.file_list[line_num-1] = self.copy_var[0]
            print("----display file---")
            print("\n")
            self.display_file()


    def delete_file(self):
        # reassign the list to empty value
        # for all indexes
        self.file_list = [0]*self.capacity

        self.display_file()

    
    def display_file(self):
        # print(self.file_list)
        # for index, item in self.file_list:
        #     print(f"{index}. {item}")

        for i, item in enumerate(self.file_list, start=1):
            print(f"{i}. {item}")
    
    def undo(self):
        pass
    
    def redo(self):
        pass