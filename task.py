image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

def PythonTask(self, image, sr, sc, newColor):
   
    if(image[sr][sc]==newColor):
        return image
    mas=image[sr][sc]
    stack=[(sr,sc)]
    while(stack):
        x,y=stack.pop()
        if(image[x][y]==mas):
            image[x][y]=newColor    
            if(x+1<len(image)):
                stack.append((x+1,y))
            if(x-1>=0):
                stack.append((x-1,y))
            if(y+1<len(image[0])):
                stack.append((x,y+1))
            if(y-1>=0):
                stack.append((x,y-1))
        else:
            pass
    return image

