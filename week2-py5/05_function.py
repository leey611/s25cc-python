def setup():
    size(400, 400) 

    

def draw():
    
    for column in range(6):
        for row in range(6):
            x_pos = column * 80
            y_pos = row * 80
            drawBear(x_pos, y_pos)
            
def drawBear(x_pos, y_pos):
    face_size = 50
    ear_size = 30
    spacing = 20
    circle(x_pos - spacing, y_pos - spacing, ear_size)
    circle(x_pos + spacing, y_pos - spacing, ear_size)
    circle(x_pos, y_pos, face_size)


run_sketch()
