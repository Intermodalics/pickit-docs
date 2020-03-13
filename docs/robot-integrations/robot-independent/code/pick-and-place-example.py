# Application inputs (needs replacing with actual values).
Detect = [x,y,z,rx,ry,rz]
AbovePickArea = [x,y,z,rx,ry,rz]
Dropoff = [x,y,z,rx,ry,rz]

setup = 1
product = 1

def gripper_release():
    # Add custom gripper release logic.

def gripper_grasp():
    # Add custom gripper grasp logic.

def gripper_pick_success():
    # Add custom gripper pick success check. Returns a boolean.
    # If you don't have the means to measure pick success, return always True.

# Pick all objects and write number of successful picks to 'picks'.
picks = pick_and_place(setup, product)
