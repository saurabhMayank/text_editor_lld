
LLD of a text Editor

Class Diagram
![class_diagram_text_editor_2](https://github.com/saurabhMayank/text_editor_lld/assets/82028762/236840c3-6339-470d-808e-1789b5fb03aa)


**Basic Flow of Text Editor**
- When User opens a text editor ->TextEditorSingleton Class is invocated
- It is a Singelton class -> Means if a text editor is opened -> The instance of texteditor will be singleton for other objects of system
- In that User can create a file
- When User creates a file -> file_obj of File Class will be invocated
- Lot of files can be created from a TextEditor. TextEditorSingleton Class instance will be same for all the file class instances.
- Now User can perform lot of actions on the file_obj
    1. Insert in a file
    2. Copy from a file
    3. Paste in a file
    4. Delete from a file
    5. Undo and Redo in the file
    6. Delete the whole file
    7. Display the whole file
