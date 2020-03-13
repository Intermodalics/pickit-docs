def after_end():
    # Unrecoverable error. Raise alarm and stop program.
    if pickit_no_image_captured():
        alarm("Failed to capture a camera image.")
        halt()

    if not pickit_empty_roi():
        # Save a snapshot to learn why no objects were detected in a non-empty ROI.
        pickit_save_snapshot()

    # Request more parts to start picking all over again.
    feed_more_parts()
