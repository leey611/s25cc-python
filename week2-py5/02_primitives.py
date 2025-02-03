# run the following py5 code using Thonny IDE and Thonny py5 plugin

def setup():
    size(400, 400) # sizing your canvas

    
def draw():
    
    fill('#00ff00')
    circle(width/2, height/2, 50)
    
    fill('#0000ff')
    rect(50,100, 100, 200)
    
    line(300, 100, 350, 200)
    
    fill("#ffff00")
    ellipse(300, 250, 100, 50)

run_sketch()