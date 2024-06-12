import cv2

# Create a VideoCapture object
cam = cv2.VideoCapture(0)
# Create a window to display the video
cv2.namedWindow("test 1 python webcam")

# Initialize a counter for the number of images
image_counter = 0

# Infinite loop to capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()

    # If the frame is not captured correctly, break the loop
    if not ret:
        print("failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow("test 1 python webcam", frame)

    # Wait for a key press and check if it is the escape key
    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape  hit, closing...")
        break
    # Check if the space bar is pressed
    elif k % 256 == 32:
        # Save the frame as an image file
        image_name = "opencv_frame_{}.png".format(image_counter)
        cv2.imwrite(image_name, frame)
        print("{} written!".format(image_name))
        # Increment the counter
        image_counter += 1
        print("take ss")

# When everything is done, release the VideoCapture object
cam.release()

# Destroy all the windows
cv2.destroyAllWindows()

# Close the VideoCapture object
cam.close()