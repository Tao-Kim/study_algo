import sys
sys.setrecursionlimit(10000000)
import copy

class Node:
    value = None
    left_child = None
    right_child = None

    def __init__(self, value):
        self.value = value


def make_binary_tree(nodeinfos):
    root_node = Node(nodeinfos[0][2])
    node_map = {nodeinfos[0][0] : root_node}
    top_depth = nodeinfos[0][1]
    previous_depth_nodeinfos = [nodeinfos[0]]
    del nodeinfos[0]

    for current_depth in range(top_depth-1,-1,-1):
        current_depth_nodeinfos = [node for node in nodeinfos if node[1] == current_depth]

        if not current_depth_nodeinfos:
            continue

        for current_nodeinfo in current_depth_nodeinfos:
            shortest_parent_node_distance = 987654321
            shortest_parent_nodeinfo = None

            for previous_nodeinfo in previous_depth_nodeinfos:
                distance_with_parent = previous_nodeinfo[0] - current_nodeinfo[0]
                if abs(distance_with_parent) < abs(shortest_parent_node_distance):
                    shortest_parent_node_distance = distance_with_parent
                    shortest_parent_nodeinfo = copy.deepcopy(previous_nodeinfo)

            current_node = Node(current_nodeinfo[2])
            node_map[current_nodeinfo[0]] = current_node
            parent_node = node_map[shortest_parent_nodeinfo[0]]
            if shortest_parent_node_distance < 0:
                parent_node.right_child = current_node
            else:
                parent_node.left_child = current_node
            nodeinfos.remove(current_nodeinfo)

        previous_depth_nodeinfos = copy.deepcopy(current_depth_nodeinfos)

    return root_node

def make_pre_order_list(root):
    pre_order_list = []
    def _pre_order(_root):
        if _root is None:
            return
        pre_order_list.append(_root.value)
        _pre_order(_root.left_child)
        _pre_order(_root.right_child)

    _pre_order(root)
    return pre_order_list

def make_post_order_list(root):
    post_order_list = []
    def _post_order(_root):
        if _root is None:
            return
        _post_order(_root.left_child)
        _post_order(_root.right_child)
        post_order_list.append(_root.value)

    _post_order(root)
    return post_order_list

def solution(nodeinfo):
    if not nodeinfo:
        return [[],[]]

    nodeinfo = [node + [i] for i, node in enumerate(nodeinfo, start=1)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    binary_tree_root = make_binary_tree(nodeinfo)
    pre_order_list = make_pre_order_list(binary_tree_root)
    post_order_list = make_post_order_list(binary_tree_root)
    answer = [pre_order_list, post_order_list]
    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42890
시간 : 1:10:25
테스트 : 11/29 37.9점 

- 
다른 사람 풀이 :
========================================================================================
import sys
sys.setrecursionlimit(10 ** 6)

class Tree:
    def __init__(self, dataList):
        self.data = max(dataList, key=lambda x: x[1])
        leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
        rightList = list(filter(lambda x: x[0] > self.data[0], dataList))
        if leftList != []:
            self.left = Tree(leftList)
        else:
            self.left = None
        if rightList != []:
            self.right = Tree(rightList)
        else:
            self.right = None


def fix(node, postList, preList):
    postList.append(node.data)
    if node.left is not None:
        fix(node.left, postList, preList)
        
    if node.right is not None:
        fix(node.right, postList, preList)
    preList.append(node.data)


def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []
    fix(root, postList, preList)
    
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    return answer

========================================================================================

노트 :
- 다른 사람 풀이 다시보기
"""