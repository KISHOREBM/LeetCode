from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        q=deque([(sr,sc)])
        ori=image[sr][sc]
        visited = [[True for _ in range(len(image[0]))] for _ in range(len(image))]

        while q:
            sr,sc=q.popleft()
            ir,dr=sr+1,sr-1
            ic,dc=sc+1,sc-1
            while ir<len(image) and image[ir][sc]==ori and visited[ir][sc]:
                image[ir][sc]=color
                q.extend([(ir,sc)])
                visited[ir][sc]=False
                ir+=1
            while dr>=0 and image[dr][sc]==ori and visited[dr][sc]:
                image[dr][sc]=color
                q.extend([(dr,sc)])
                visited[dr][sc]=False
                dr-=1
            while ic<len(image[0]) and image[sr][ic]==ori and visited[sr][ic]:
                image[sr][ic]=color
                q.extend([(sr,ic)])
                visited[sr][ic]=False
                ic+=1
            while dc>=0 and image[sr][dc]==ori and visited[sr][dc]:
                image[sr][dc]=color
                q.extend([(sr,dc)])
                visited[sr][dc]=False
                ir-=1
            image[sr][sc]=color
        return image
        