import numpy
import matplotlib.pyplot as plt
from heapq import heappush,heappop

def heuristic_cost_estimate(neighbor, goal):#启发函数h
    x = neighbor[0] - goal[0]
    y = neighbor[1] - goal[1]
    return abs(x) + abs(y)

def dist_between(a, b):#距离g
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def reconstruct_path(came_from, current):#沿着父节点生成最短路
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


def astar(array, start, goal):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8个方向
    close_set = set()#采用set（红黑树）实现，便于快速查找
    openSet = []     #插入最小堆中，便于排序
    came_from = {}
    gscore = {start: 0} #实际代价
    fscore = {start: heuristic_cost_estimate(start, goal)}  #f=h+g,初始g=0

    heappush(openSet, (fscore[start], start))  # 往堆中插入一条新的值

    while openSet:# 当 openSet 非空
        current = heappop(openSet)[1]  # 从堆中弹出fscore最小的节点

        if current == goal:
            return reconstruct_path(came_from, current)

        close_set.add(current)#加入close表

        for i, j in directions:  # 对当前节点的 8 个相邻节点一一进行检查
            neighbor = current[0] + i, current[1] + j

            #判断节点是否在地图范围内，并判断是否为障碍物
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue #在范围内但为障碍物，忽略
                else:
                    continue    #y不符合要求，忽略
            else:
                continue        #x不符合要求，忽略

            if neighbor in close_set:
                continue        #已在close表，忽略

            #  经过current到neighbor的距离
            temp_gScore = gscore[current] + dist_between(current, neighbor)

            if neighbor not in [i[1] for i in openSet]:  # 如果neighbor不在openlist中
                heappush(openSet, (fscore.get(neighbor, numpy.inf), neighbor))
            elif temp_gScore >= gscore.get(neighbor, numpy.inf):  # 原路径更短，不加入
                continue

            came_from[neighbor] = current #把neighbor的父亲设为当前结点
            gscore[neighbor] = temp_gScore
            fscore[neighbor] = temp_gScore + heuristic_cost_estimate(neighbor, goal)

    return False

if __name__ == "__main__":
    nmap = numpy.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    path = astar(nmap, (0, 0), (19, 19))
    nmap=nmap*10#便于hot图显示
    print(len(path))
    for i in range(len(path)):
        nmap[path[i]] = 5
        print(path[i])
    plt.imshow(nmap,cmap=plt.get_cmap('hot'))
    plt.axis('off')
    plt.show()
