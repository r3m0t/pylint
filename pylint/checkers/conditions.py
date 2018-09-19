import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class RedundantIfelseChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'redundant-ifelse'
    priority = -1
    msgs = {
        'W0002': (  # XXX needs number assigned
            'Simple if-else',
            'redundant-ifelse',
            'if-else expression can be simplified.'
        )
    }
    
    def visit_ifexp(self, node):
        left_is_true = isinstance(node.body, astroid.node_classes.Const) and node.body.value == True
        right_is_false = isinstance(node.orelse, astroid.node_classes.Const) and node.orelse.value == False
        middle_is_cond = isinstance(node.test, astroid.node_classes.Compare)
        if left_is_true and right_is_false and middle_is_cond:
            self.add_message(
                'redundant-ifelse', node=node,
            )
    
def register(linter):
    linter.register_checker(RedundantIfelseChecker(linter))
