# YOLO Framework Object-Detection
This project aims to use object detection methods such as Sliding Window and YOLO algorithm on real-time video files.

## Notebook/Implementation
### NeuralNetwork.ipynb
- Loads a vehicle dataset from the University of Toronto, creates a simple Neural Network to predict class images.

### SlidingWindow.ipynb
- Implementation of the sliding window approach throughout the entire image. The car and truck images were trained from the vehicle dataset (trained using a chosen CNN and VGG16 model). Then, each crop of the image was responsible if it's a car, truck, or background. Achieved a 73.33% accuracy.


  

## How to Run
To use the YOLOV5 model, clone the entire repository first; change the file path in the code to the file path of your video file. You can also change the frames per second, fontScale, or color to your preferences.

To use the YOLOV3 model, run the code cells in order, but change the file path at the very end of the notebook to the path of your video file.

## Final Results

### YOLOV3:



https://github.com/sbal06/Object-Detection/assets/101956177/76cc4494-b440-4d0e-8136-f5013902836c




### YOLOV5 Medium Version: 




https://github.com/sbal06/Object-Detection/assets/101956177/2ec1c781-60ed-465b-9064-c10def4d8a1f


## References:

1. [Real-time Object Detection with YOLO and Webcam: Enhancing Your Computer Vision Skills](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993)
   <br>
   - Special thanks to Dipankar Medhi for an article on YOLOV5 and how to use it on a camera!
