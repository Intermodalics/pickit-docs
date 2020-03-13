if not pickit_is_running():
    print("Pickit is not in robot mode. Please enable it in the web interface.")
    halt()

before_start()
pickit_configure(setup, product)

retries = 5  # Number of detection retries before bailing out.
goto_detection()
pickit_find_objects_with_retries(retries)
pickit_get_result()

while True:
    if not pickit_object_found():
        # There are no pickable objects, bail out.
        break

    if pickit_object_reachable():
        # Object is pickable!
        pick()
        goto_detection()
        pickit_find_objects_with_retries(retries)
        place()  # In parallel to detection, saves cycle time.
        pickit_get_result()
    else:
        # Object is unreachable, get the next detection, if any.
        pickit_next_object()
        pickit_get_result()

after_end()

# Action performed once before starting pick and place.
def before_start():
    gripper_release()

# Move the robot to the point from which object detection is triggered.
def goto_detection():
    movej(Detect)

# Sequence for performing the picking motion:
# - Starts and ends at AbovePickArea, a point reachable in a collision-free way.
# - PrePick --> PickitPick: Linear approach to the pick point.
# - A grasping action.
# - PickitPick --> PostPick: Linear retreat away from the pick point.
#
# The optional offset parameters are in millimeters.
def pick(pre_pick_offset=100, post_pick_offset=100):
    # PrePick is parallel to the object's z-axis, i.e. it tilts with the object.
    PrePick = PickitPick * Pose(0, 0, -pre_pick_offset, 0, 0, 0)

    # PostPick is along the robot base z-axis, which typically means straight-up.
    PostPick = PickitPick
    PostPick.z = PostPick.z + post_pick_offset

    # Actual motion sequence.
    movej(AbovePickArea)
    movel(PrePick)
    movel(PickitPick)
    gripper_grasp()  # For a suction-like gripper, do this one line above.
    movel(PostPick)
    movel(AbovePickArea)

# Sequence for placing the object at the specified dropof location.
def place():
    movej(Dropoff)
    gripper_release()

# Action performed once after pick and place has finished.
def after_end():
    if not pickit_object_found():
        if pickit_empty_roi():
            print("The ROI is empty.")
        else:
            print("The ROI is not empty, but the requested object was not found.")
    elif not pickit_object_reachable():
        print("All detections are unreachable.")
    elif pickit_no_image_captured():
        print("Failed to capture a camera image.")
