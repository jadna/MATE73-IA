
class Op():
    def __init__(self,symbol, fun):
        self.symbol = symbol
        self.fun = fun
        

    def true_value(self, op1, op2):
        return self.fun(op1, op2)
    

class Atom():
    def __init__(self, symbol):
        self.symbol = symbol
        self.value = False


    def set_value(self, value):
        self.value = value
        
    def true_value(self):
        return self.value

class NodeSentence():
    def __init__(self,content, left, right):
        self.content = content
        self.left = left
        self.right = right



def mount_tree(nodes):
    if len(nodes) == 1:
        return nodes[0]
    else:
        node = None
        for op in ['^' , '|', '=>']:
            ops = [n for n in nodes if n.content.symbol == op and n.left == None]
            if ops:
                node = ops[0]
                break

        pos = nodes.index(node)
        node.left = nodes[pos-1]
        node.right = nodes[pos+1]
        nodes.remove(node.left)
        nodes.remove(node.right)
        return mount_tree(nodes)


def infer(rules, facts, query):
    if query in facts:
        return True
    elif isinstance(query, str):
        results_rules = [rule for rule in rules if rule.right.content.symbol == query]
        if not results_rules:
            return False
        rule = results_rules[0]
        op1 = infer(rules, facts, rule.left)
        return rule.content.true_value(op1, True)
    else:
        if isinstance(query.content, Atom):
            return infer(rules, facts, query.content.symbol)
        else:
            op1 = infer(rules, facts, query.left)
            op2 = infer(rules, facts, query.right)
            return query.content.true_value(op1, op2)


if __name__ == '__main__':

    rules = []
    while True:
        entry = input().rstrip()
        if entry == 'END':
            break;
        tokens = []
        entry = ''.join(entry.split())
        for c in entry:
            if c == '^':
                tokens.append(NodeSentence(Op(c, lambda x,y : x and y), None, None))
            elif c == '|':
                tokens.append(NodeSentence(Op(c, lambda x,y : x or y), None, None))
            elif c == '=':
                pass
            elif c == '>':
                tokens.append(NodeSentence(Op('=>', lambda x,y : y if x else False), None, None))
            else:
                tokens.append(NodeSentence(Atom(c), None, None))

    
        rules.append(mount_tree(tokens))

    
    entry = input().rstrip()
    facts = entry.split(',')
    query = input().rstrip()
    
    
    if infer(rules, facts, query):
        print('TRUE')
    else:
        print('FALSE')
