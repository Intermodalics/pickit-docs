# Pickit pick and place function.
#
# Parameters:
# - setup: ID of the setup file to load.
# - product: ID of the product file to load.
# - target_picks [optional]: A positive value means exit after n successful picks.
# - retries [optional]: Number of detection retries before bailing out.
#       A non-positive value means exit on no more pickable objects (pick all).
#
# Requires the existence of the following functions:
# - before_start()
# - goto_detection()
# - pick() returns a boolean (True on pick success)
# - on_pick_failure()
# - place()
# - after_end()
#
# Returns the number of successful picks.
def pick_and_place(setup, product, target_picks=-1, retries=5):
    if not pickit_is_running():
        print("Pickit is not in robot mode. Please enable it in the web interface.")
        halt()

    before_start()
    pickit_configure(setup, product)

    goto_detection()
    pickit_find_objects_with_retries(retries)
    pickit_get_result()

    picks = 0
    while True:
        if not pickit_object_found():
            # There are no pickable objects, bail out.
            break

        # Compute pre-pick and post-pick points.
        PrePick = compute_pre_pick(PickitPick)
        PostPick = compute_post_pick(PickitPick)

        if pickit_is_reachable(PickitPick, PrePick, PostPick):
            # Object is pickable! Attempt pick.
            pick_success = pick()
            if pick_success:
                picks += 1
                done_picking = target_picks > 0 and picks == target_picks
                if done_picking:
                    # Target picks reached. Place without further detections.
                    place()
                    break
                else:
                    # Target picks not reached. Place and detect next object.
                    goto_detection()
                    pickit_find_objects_with_retries(retries)
                    place()  # In parallel to detection, saves cycle time.
                    pickit_get_result()
            else:
                # Picking failed, skip place and detect next object.
                on_pick_failure()
                goto_detection()
                pickit_find_objects_with_retries(retries)
                pickit_get_result()
        else:
            # Object is unreachable, get the next detection, if any.
            pickit_next_object()
            pickit_get_result()

    after_end()

    return picks


# Action performed once before starting pick and place.
def before_start():
    gripper_release()

# Move the robot to the point from which object detection is triggered.
def goto_detection():
    movej(Detect)

# PrePick is parallel to the object's z-axis, i.e. it tilts with the object.
# The optional offset parameter is in millimeters.
def compute_pre_pick(PickitPick, pre_pick_offset=100):
    PrePick = PickitPick * Pose(0, 0, -pre_pick_offset, 0, 0, 0)
    return PrePick

# PostPick is along the robot base z-axis, which typically means straight-up.
# The optional offset parameter is in millimeters.
def compute_post_pick(PickitPick, post_pick_offset=100):
    PostPick = PickitPick
    PostPick.z = PostPick.z + post_pick_offset
    return PostPick

# Sequence for performing the picking motion:
# - Starts and ends at AbovePickArea, a point reachable in a collision-free way.
# - PrePick --> PickitPick: Linear approach to the pick point.
# - A grasping action.
# - PickitPick --> PostPick: Linear retreat away from the pick point.
def pick():
    movej(AbovePickArea)
    movel(PrePick)
    movel(PickitPick)
    gripper_grasp()  # For a suction-like gripper, do this one line above.
    movel(PostPick)
    movel(AbovePickArea)

    return gripper_pick_success()

# Action taken when picking an object failed.
def on_pick_failure():
    gripper_release()

# Sequence for placing the object at the specified dropof location.
def place():
    movej(Dropoff)
    gripper_release()

# Action performed once after pick and place has finished.
def after_end():
    if not pickit_object_found():
        if pickit_empty_roi():
            print("The ROI is empty.")
        elif pickit_no_image_captured():
            print("Failed to capture a camera image.")
        else:
            print("The ROI is not empty, but the requested object was not found or is unreachable.")
