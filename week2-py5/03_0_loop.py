def setup():
    size(400, 400) 

    

def draw():
    
    # for x in [0, 80, 160, 240, 320, 400]:
    #     circle(x, height/2, 50)
        
    for i in range(6):
        circle(i * 80, height/2, 50)

    # for x in range(0, 401, 80):
    #     circle(x, height/2, 50)
 

run_sketch()