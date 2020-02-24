def place():
    if PickitPickId == 1:
        # Dropoff for object picked from the top.
        movej(DropoffTop)
    else:
        # Dropoff for object picked from the bottom.
        movej(DropoffBottom)
    gripper_release()