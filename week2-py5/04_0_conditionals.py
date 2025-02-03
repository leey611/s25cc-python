def setup():
    size(400, 400) 

    

def draw():
    
    for column in range(6):
        if column % 2 == 0:
            fill(0,0,255)
        else:
            fill(255)
        for row in range(6):
            circle(column * 80, row * 80, 50)
 


run_sketch()
