def setup():
    size(400, 400) 

    

def draw():
    
    for column in range(6):
        for row in range(6):
            if column == row:
                fill(0,0,255)
            else:
                fill(255)
            circle(column * 80, row * 80, 50)
 

run_sketch()
