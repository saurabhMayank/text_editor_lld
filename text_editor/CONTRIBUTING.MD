* Assumptions in the application
* Undo & Redo operations theoretically implemented. Actual implementation not done
* The emptying of undo & redo stack -> is out of scope
* Single instance of text editor in the entire application
* Text editor can have multiple files
* Every file is an array of limited size
* File is initialized as empty string of definite size
* Each line is an empty string at the start
* Copy content from single line, past to a single line
* One copy paste operation will be completed, then only other can start
* Cannot copy multiple things at once
* Delete text from a single line
* Modes of opening the file is out of scope