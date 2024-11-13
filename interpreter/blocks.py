from typing import Self
from . import NodeType, Statement, Expression


class Block:
    def __init__(self) -> None:
        self.node_type = NodeType('Block')
        self.body = []
    
    def body_append(self, statement: Statement | Self):
        self.body.append(statement)
    
    def fields(self) -> dict:
        return {'type': self.node_type.node_type, 'body': self.body}
    
    def get_type(self) -> str:
        return self.node_type.node_type



class IfStatement(Block):
    def __init__(self, condition) -> None:
        self.condition = condition
        super().__init__()
        self.node_type = NodeType("IfStatement")
    
    def fields(self) -> dict:
        return {'type': self.node_type.node_type, 'condition': self.condition, 'body': self.body}

    def get_type(self) -> str:
        return self.node_type.node_type


class IfBlock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.node_type = NodeType("IfBlock")
        self.conditions: list[IfStatement] = []
        self.pointer = 0 
    
    def add_condition(self, condition: IfStatement):
        self.conditions.append(condition)

    def next_condition(self) -> IfStatement | None:
        if len(self.conditions) != 0:
            condition = self.conditions[self.pointer]
            self.pointer += 1
            return condition
        return None
    
    def reset_conditions(self) -> None:
        self.pointer = 0
    
    def fields(self) -> dict:
        return {'type': self.node_type.node_type, 'conditions': self.conditions}

    def get_type(self) -> str:
        return self.node_type.node_type


class ForBlock(Block):
    def __init__(self, initialiser, limit, step=None) -> None:
        super().__init__()
        self.node_type = NodeType("ForBlock")
        self.initialiser = initialiser
        self.limit = limit
        self.step = step or 1

    def next(self):
        self.initialiser += self.step
        return self.initialiser if self.initialiser < self.limit else None

    def fields(self) -> dict:
        return {
            'type': self.node_type.node_type,
            'initialiser': self.initialiser,
            'limit': self.limit,
            'step': self.step
        }
    
    def get_type(self) -> str:
        return self.node_type.node_type


class WhileBlock(Block):
    pass


class SwitchBlock(Block):
    pass


class CaseBlock(Block):
    pass


class FuncBlock(Block):
    pass
