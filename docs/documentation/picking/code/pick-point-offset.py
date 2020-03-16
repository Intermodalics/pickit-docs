def place():
    # The '*' operator represents the pose composition operator.
    CorrectedDropoff = Dropoff * PickitPickOff
    movej(CorrectedDropoff)
    gripper_release()
