bear_positions = []

def setup():
    size(400, 400) 


def draw():
    for pos in bear_positions:
        drawBear(pos["x"], pos["y"])
    
            
def drawBear(x_pos, y_pos):
    face_size = 50
    ear_size = 30
    spacing = 20
    circle(x_pos - spacing, y_pos - spacing, ear_size)
    circle(x_pos + spacing, y_pos - spacing, ear_size)
    circle(x_pos, y_pos, face_size)

def mouse_clicked(e):
    pos = {
        "x": mouse_x,
        "y": mouse_y
    }
    bear_positions.append(pos)

def key_pressed(e):
    pressed_key = e.get_key()
    
    if pressed_key == 's':
        save('sketch.jpg')

run_sketch()
