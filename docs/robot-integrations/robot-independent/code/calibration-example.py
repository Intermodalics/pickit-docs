# Calibration poses (needs replacing with actual values).
Point1 = [x,y,z,rx,ry,rz]
Point2 = [x,y,z,rx,ry,rz]
Point3 = [x,y,z,rx,ry,rz]
Point4 = [x,y,z,rx,ry,rz]
Point5 = [x,y,z,rx,ry,rz]

# Move to each calibration pose and trigger a calibration plate detection.
movej(Point1)
pickit_find_calibration_plate()

movej(Point2)
pickit_find_calibration_plate()

movej(Point3)
pickit_find_calibration_plate()

movej(Point4)
pickit_find_calibration_plate()

movej(Point5)
pickit_find_calibration_plate()
