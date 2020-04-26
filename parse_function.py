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
    
     

zeus = Node('+')
zeus.left = Node('3')
zeus.left.left = Node ('5')
zeus.left.right = Node('6')
zeus.right = Node('4')
zeus.right.left = Node('10')
zeus.right.right = Node('12')

def parse_func(arr):
    fire = parse(arr).split(",")
    #print(fire)
    return  fire 

def parse (arr):
    order = {'+': 4, '-': 4, '*': 3, '/': 3, '^': 2, 'log': 1, 'sin': 1, 'cos': 1}
    operators = ['+', '-', '*', '/', '^', 'log', 'sin', 'cos']
    if len(arr) == 1:
        if isinstance(arr[0], list):
            return parse(arr[0])
        else:
            return arr[0] 
    nums = []
    ops = []
    i = 0
    while i < len(arr):           
        if arr[i] in operators :
            ops.append(arr[i])
        elif isinstance(arr[i], list):
            nums.append(parse(arr[i]))
        else:
            nums.append(arr[i])
        i += 1
        if len(ops)>0 and (ops[len(ops)-1] == 'log' or ops[len(ops)-1] == 'sin' or ops[len(ops)-1] == 'cos'):
            nums.append(ops[len(ops)-1]+','+parse(arr[i]))   
            del ops[len(ops)-1]
            i+=1 
        while len(ops) > 1 and order[ops[len(ops)-1]] >= order[ops[len(ops)-2]]:
            first = nums.pop(len(nums) - 2) 
            second = nums.pop(len(nums) - 1)
            func = ops.pop(len(ops) - 2)  
            nums.append(func + "," + first + "," + second) 
    first = nums.pop(len(nums) - 2)
    second = nums.pop(len(nums) - 1)
    func = ops.pop(0)
    nums.append(func + "," + first + "," + second) 
    return nums[0]

def make_tree(arr , i):
    if i == len(arr):
        return [None, i] 
    operators = ['+', '-', '*', '/', '^', 'log', 'e', 'sin', 'cos']
    fire = Node(arr[i])
    if arr[i] not in operators:
        return [fire, i+1] 
    i += 1
    if arr[i-1] == 'log' or arr[i-1] == 'sin' or arr[i-1] == 'cos':
        [fire.left , i] = make_tree(arr, i)
        fire.right = None
    else:
        [fire.left , i] = make_tree(arr, i)
        [fire.right, i] = make_tree(arr, i) 
    return [fire, i] 
def parser (arr):
    print(make_tree(parse_func(arr),0)[0]) 
    print_node(make_tree(parse_func(arr),0)[0])
    print_tree(make_tree(parse_func(arr),0)[0] , 0)

arr = [['sin', ['x', '^', '2'], '+' , '6'], '/', [['3', '*', 'x', '^', '2', '-', 'pi'], '^', '4', '+', '4']]
athena = make_tree(parse_func(arr),0)[0]
print(athena)

