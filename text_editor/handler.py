"""
Handler file which takes prompt from the user
and create a file in the text editor
"""

from text_editor.text_editor_main import TextEditorSingleton

def run_handler():
    print("----Text Editor opened---")

    text_editor_singelton_obj = TextEditorSingleton()


    print("\n")
    print("---Create a File with a defined file size---")
    file_name = input("Enter file name: ")
    file_size = int(input("Enter file size: "))


    file_1_obj = text_editor_singelton_obj.create_file(name = file_name, capacity = file_size)

    print("\n")
    print(f"---File {file_name} of size {file_size} is created----")

    print("\n")
    print("---Enter text to insert and also on which line number----")
    text_to_insert = input("Enter text to insert: ")
    line_num_to_insert = int(input("Enter line number to insert to: "))

    file_1_obj.insert_text(line_num_to_insert, text_to_insert)

    print("\n")
    print("---Enter texts to insert and also on which line numbers----")

    user_input = input("Enter key-value pairs separated by commas (e.g., lineNum1:text1,lineNum2:text2): ")
    if user_input.startswith("{") and user_input.endswith("}"):
        user_input = user_input[1:-1]  
    data = {}
    for pair in user_input.split(","):
        key, value = pair.split(":")
        print(type(key))
        key = int(key)
        data[key] = value.strip() 

    file_1_obj.insert_text_multiple_lines(data)

    print("\n")
    print("---Delete text from a specific line_num--")
    line_num_to_delete = int(input("Enter line number to delete text from: "))

    file_1_obj.delete_text(line_num_to_delete)

    print("\n")

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