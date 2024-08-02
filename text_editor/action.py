class Action:
    def __init__(self, action_name: str, content: str,  line_num: int, undo: bool, redo: bool):
        self.action_name = action_name
        self.content = content
        self.line_num = line_num
        self.undo = undo
        self.redo = redo
    