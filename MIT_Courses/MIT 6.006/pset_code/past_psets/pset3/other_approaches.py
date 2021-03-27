indices = dict()

def preorder(inorder:list, postorder:list, shift=0) -> list:
    if inorder == [] or postorder == []: return []

    # get last element (our root) from postorder
    root = postorder.pop()
    # find its index in inorder 
    idx = indices[root] - shift

    # elements before and after
    before_root = inorder[:idx]
    after_root = inorder[idx+1:]
    # print(before_root, after_root, idx)

    # add root to our result, then the left subtree result, then right
    result = [root]
    result += get_preorder(before_root, postorder[:idx], shift)
    result += get_preorder(after_root, postorder[idx:], shift+idx+1)
    
    return result

def get_preorder(inorder:list, postorder:list, start:int, end:int) -> list:
    if start > end: return []

    # get last element (our root) from postorder
    root = postorder[end]
    # find its index in inorder 
    idx = indices[root]

    result = [root]
    result += get_preorder(inorder, postorder, start, idx - 1)
    result += get_preorder(inorder, postorder, idx + 1, end)

    return result
