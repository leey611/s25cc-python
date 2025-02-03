# run the following py5 code using Thonny IDE and Thonny py5 plugin

def setup():
    size(400, 400) 

    

def draw():
    
    background(255)
    no_stroke()
    
    # Ears
    fill(220, 220, 220)
    circle(120, 60, 80)
    circle(280, 60, 80)
    fill(0, 0, 0)
    ellipse(120, 60, 60, 60)
    ellipse(280, 60, 60, 60)
    
    # Face
    fill(220, 220, 220)
    rect_mode(CENTER)
    rect(200, 200, 280, 280, 80)  # Rounded square
    
    
    # Eye patches
    fill(80, 80, 80)
    ellipse(140, 180, 100, 100)
    ellipse(260, 180, 100, 100)
    
    # Pupils
    fill(0, 0, 0)
    ellipse(140, 180, 12, 12)
    ellipse(260, 180, 12, 12)
    
    # Nose
    fill(0, 0, 0)
    triangle(190, 230, 210, 230, 200, 250)
    
    # Mouth
    stroke(0, 0, 0)
    stroke_weight(6)
    line(200, 250, 200, 310) 
    no_fill()
    arc(200, 300, 40, 30, 0, PI) 

run_sketch()
