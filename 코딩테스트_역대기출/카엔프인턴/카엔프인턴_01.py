# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
si = sys.stdin.readline
N, K = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(N)]
d = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS(y,x,start):
	visited = [[False for _ in range(N)] for _ in range(N)]
	target = start + 1 # 다음 목표지점은 그다음번호임
	q = deque([(y,x,0)])
	visited[y][x] = True
	while q:
		cy,cx,cd = q.popleft()
		if board[cy][cx] == target:
			return cd
		for i in range(4):
			ny = cy + d[i][0]
			nx = cx + d[i][1]
			if ny < 0 or nx < 0 or ny >= N or nx >= N:
				continue
			if visited[ny][nx] == True:
				continue
			visited[ny][nx] = True
			q.append((ny,nx,cd + 1))
	return 0
# 각 점에서 그다음 목표로 독착하기 위해 탐색함
answer = 0
for k in range(1,K+1):
	flag = False
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == k:
				answer += BFS(i,j,board[i][j])
				flag = True
				break
		if flag == True:
			break

print(answer)