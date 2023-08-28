#Get user input for length of the video in seconds.
length_of_video = float(input("Length of video(s): "))
# Get the user input for the frame rate (fps)
fps = float(input("Fps: "))
# Calculate the total frames using the formula: length of video *fps
print(round(fps * length_of_video))
# Display the result to the nearest whole number.
