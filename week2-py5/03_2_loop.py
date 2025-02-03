def setup():
    size(400, 400) 

    

def draw():
    
    for i in range(6):
        fill(random(0,255), random(0,255), random(0,255))
        circle(random(0, width), random(0, height), 50)

    no_loop() # stop the draw() after running once


run_sketch()