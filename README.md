![class_diagram_text_editor](https://github.com/saurabhMayank/text_editor_lld/assets/82028762/ecaf91cc-acba-4f15-9eaa-5b75a3598ca4)# text_editor_lld
LLD of a text Editor

Class Diagram
![class_diagram_text_editor](https://github.com/saurabhMayank/text_editor_lld/assets/82028762/3a931572-cb97-4c00-88ff-fbd851e051f5)


Basic Flow of Text Editor
a. When User opens a text editor ->TextEditorSingleton Class is invocated
b. It is a Singelton class -> Means if a text editor is opened -> The instance of texteditor will be singleton for other objects of system
c. In that User can create a file
d. When User creates a file -> file_obj of File Class will be invocated
e. Lot of files can be created from a TextEditor. TextEditorSingleton Class instance will be same for all the file class instances.
f. Now User can perform lot of actions on the file_obj
*) Insert in a file
*) Copy from a file
*) Paste in a file
*) Delete from a file
*) Undo and Redo in the file
