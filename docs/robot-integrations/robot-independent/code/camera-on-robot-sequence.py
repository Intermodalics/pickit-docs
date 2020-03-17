# Try first a single detection in parallel to place...
goto_detection()
capture_ok = pickit_capture_image()
if capture_ok:
    pickit_process_image()
    place()
    pickit_get_result()
# If not successful, detect with retries. No longer in parallel with motions.
if not capture_ok or not pickit_object_found():
    goto_detection()
    pickit_find_objects_with_retries(retries)
    pickit_get_result()