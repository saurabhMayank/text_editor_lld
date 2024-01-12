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

    user_input = input("Enter key-value pairs separated by commas (e.g., key1:value1,key2:value2): ")
    data = {}
    for pair in user_input.split(","):
        key, value = pair.split(":")
        data[key.strip()] = value.strip() 

     file_1_obj.insert_text_multiple_lines(data)


if __name__ == "__main__":
    run_handler()