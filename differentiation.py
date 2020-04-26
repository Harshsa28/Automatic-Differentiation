class Node:
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.val = data    
def print_node (fire):
    #print_tree(fire, 0)
    
    if fire is None :
        return
    print_node(fire.left)
    print(fire.val, end="") 
    print_node(fire.right) 
    


def print_tree(fire, ws):
    if fire is None:
        return
    for i in range(0, ws):
        print(" ", end="")
    print(fire.val)                    
    new_ws = ws+10 
    if fire.val == 'log' or fire.val == 'sin' or fire.val == 'cos':
        print_tree(fire.left , new_ws)
    else:
        print_tree(fire.left , new_ws)
        print_tree(fire.right , new_ws) 

#after differentiate, we also need a function which would remove the useless redundacies like '- 0' or '+ 0' or '* 2 * 3 * 6' 

def differentiate (tree):
    if tree.left is None and tree.right is None:
        if tree.val == 'x':
            return Node('1')
        else:
            return Node('0')
    
    if tree.val == '+' or tree.val == '-':
        hades = summinus(tree)
        #hades  = Node(tree.val)
        #hades.left = differentiate(tree.left)
        #hades.right = differentiate(tree.right)
    if tree.val == '*':
        hades = multiplication(tree)
        #hades = Node('+')
        #hades.left = Node('*')
        #hades.left.left = differentiate(tree.left)  
        #hades.left.right = tree.right 
        #hades.right = Node('*')
        #hades.right.left = tree.left
        #hades.right.right = differentiate(tree.right)
    if tree.val == '/':
        hades = division(tree)
        #hades = Node('/')
        #hades.left = Node('-')
        #hades.left.left = Node('*')
        #hades.left.left.left = differentiate(tree.left)
        #hades.left.left.right = tree.right
        #hades.left.right = Node('*')
        #hades.left.right.left = tree.left
        #hades.left.right.right = differentiate(tree.right)
        #hades.right = Node('^')
        #hades.right.left = tree.right
        #hades.right.right = 2  
    if tree.val == '^':
        hades = power (tree)
    if tree.val == 'log':
        hades = logarithm (tree)
    if tree.val == 'sin':
        hades = sine(tree) 
    if tree.val == 'cos':
        hades = cosine(tree) 
    return hades 


def summinus(tree):
    if tree.val == '+' or tree.val == '-':
        hades = Node (tree.val)
        hades.left = differentiate(tree.left)
        hades.right = differentiate(tree.right) 
    return hades

def multiplication(tree):
    if tree.val == '*':
        hades = Node('+')
        hades.left = Node('*')
        hades.left.left = differentiate(tree.left)  
        hades.left.right = tree.right 
        hades.right = Node('*')
        hades.right.left = tree.left
        hades.right.right = differentiate(tree.right)
    return hades 

def division(tree):
    if tree.val == '/':
        hades = Node('/')
        hades.left = Node('-')
        hades.left.left = Node('*')
        hades.left.left.left = differentiate(tree.left)
        hades.left.left.right = tree.right
        hades.left.right = Node('*')
        hades.left.right.left = tree.left
        hades.left.right.right = differentiate(tree.right)
        hades.right = Node('^')
        hades.right.left = tree.right
        hades.right.right = Node('2')
    return hades 

def power(tree):
    if tree.val == '^':
        hades = Node('*')
        hades.left = tree
        hades.right = Node('*')
        hades.right.left = Node('log')
        hades.right.left.left = tree.left
        hades.right.right = tree.right 
        hades.right = differentiate(hades.right) 
    return hades

def logarithm (tree):
    if tree.val == 'log':
        hades = Node('*')
        hades.left = Node('/')
        hades.left.left = Node('1')
        hades.left.right = tree.left  
        hades.right = differentiate(tree.left) 
    return hades 

def sine(tree):
    if tree.val == 'sin':
        hades = Node('*')
        hades.left = Node('cos')
        hades.left.left = tree.left 
        hades.right = differentiate(tree.left)
    return hades 

def cosine(tree):
    if tree.val == 'cos':
        hades = Node('*')
        hades.left = Node('*')
        hades.left.left = Node('-1')
        hades.left.right = Node('sin')
        hades.left.right.left = tree.left 
        hades.right = differentiate(tree.left) 
    return hades 



from parse_function import athena 

def differentiate_func (tree):
    print_node(tree)
    print('\n')
    print_tree(tree, 0) 
    temp = differentiate(tree)
    print_node(temp)
    print('\n')
    print_tree(temp, 0)

differentiate_func(athena) 




