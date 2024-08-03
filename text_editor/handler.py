"""
Handler file which takes prompt from the user
and create a file in the text editor
"""
import json

# import text_editor

from text_editor_main import TextEditorSingleton



# from text_editor.text_editor_main import TextEditorSingleton

def run_handler():
    print("----Text Editor opened---")

    text_editor_singelton_obj = TextEditorSingleton()


    print("\n")
    print("---Create a File with a defined file size---")
    file_name = input("Enter file name: ")
    file_size = int(input("Enter file size: "))


    # Case 1 -> Initialise a file of a definite capacity & insert text
    file_1_obj = text_editor_singelton_obj.create_file(name = file_name, capacity = file_size)

    print("\n")
    print(f"---File {file_name} of size {file_size} is created----")

    # print("\n")
    # print("---Enter text to insert and also on which line number----")
    # text_to_insert = input("Enter text to insert: ")
    # line_num_to_insert = int(input("Enter line number to insert to: "))

    # file_1_obj.insert_text(line_num_to_insert, text_to_insert)


    # Case 2 -> Insert text into multiple lines
    print("\n")
    print("---Enter texts to insert and also on which line numbers----")

    # user_input is either string or dict
    user_input = input("Enter key-value pairs separated by commas (e.g., lineNum1:text1,lineNum2:text2): ")

    user_input_dict = json.loads(user_input)
    data = {}
    user_input_dict = json.loads(user_input_dict)
    
    for key, val in user_input_dict.items():
        int_key = int(key)
        data[int_key] = val

    file_1_obj.insert_text_multiple_lines(data)


    # Case 3 -> delete text from a specific line
    print("\n")
    print("---Delete text from a specific line_num--")
    line_num_to_delete = int(input("Enter line number to delete text from: "))

    file_1_obj.delete_text(line_num_to_delete)

    print("\n")

    # Case 4 -> Copy text to from a specific line &
    # Paste text to a specific line
    print("---Copy text from a specific line_num----")
    print("\n")
    line_num_to_copy = int(input("Enter line number to copy text from: "))

    file_1_obj.copy_text(line_num_to_copy)

    print("\n")
    print("---Paste text to a specific line_num----")
    print("\n")
    line_num_to_paste = int(input("Enter line number to paste text to: "))
    
    file_1_obj.paste_text(line_num_to_paste)

    
if __name__ == "__main__":
    run_handler()