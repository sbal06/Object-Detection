
# YOLO Framework Object-Detection
This project aims to use object detection methods such as Sliding Window and YOLO algorithm on real-time video files. The YOLOV3 notebook and model was built in the Inspirit AI scholars program.

## Notebooks
### NeuralNetwork.ipynb
- Loads a vehicle dataset from the University of Toronto, and creates a simple Neural Network to predict class images.

### SlidingWindow.ipynb
- Implementation of the sliding window approach throughout the entire image. The car and truck images were trained from the vehicle dataset (trained using a chosen CNN and VGG16 model). Then, each crop of the image was responsible if it's a car, truck, or background. The CNN model achieved a 73.33% accuracy.

## YOLOV5 Implementation Challenges
1. Initially, the frames per second setting was manually adjusted to different values like 10.0, 15.0, and 20.0. However, the resulting videos didn't synchronize well with the YOLOV3 model—some videos played too quickly, while others were too slow; thus the fps = vid.get(cv2.CAP_PROP_FPS) method provided a frames per second that was orginally created when the video was recorded.

2. Obtaining the percentage-based confidence score presented difficulties due to its Torch tensor format. To round the confidence score to the nearest percent, the code is employed: confidence_score_percent = torch.round(torch.tensor([confidence_score * 100.0]), decimals = 0).item(). The item() function is used to extract the value of the single-element PyTorch tensor. 


## How to Run
To use the YOLOV5 model, clone the entire repository first; change the file path in the YOLOV5 code to the file path of your video file. You can also change the frames per second, fontScale, or color to your preferences.

To use the YOLOV3 model, run the code cells in YOLOV3 notebook in order, but change the file path at the very end of the notebook to the path of your video file. The output mp4 file should be under the contents section of the Colab notebook.

## Final Results

### YOLOV3:





https://github.com/sbal06/Object-Detection/assets/101956177/9cb92734-cd6d-4fb3-9fab-014171358527





### YOLOV5 Medium Version: 



https://github.com/sbal06/Object-Detection/assets/101956177/96c9e014-d262-4194-9a47-d53df1639fa1


- An interesting observation to make is that YOLOV5m model detects more objects than the YOLOV3 model, but with a lower confidence score on the video file. For example, in the initial frame, the YOLOV3 model predicted the nearest car with a confidence score of 94% compared to the confidence score of 78% from the YOLOV5 model. In the future, experimenting with the different sizes of the YOLOV5 modles could offer a valuable for comparing against other object detection architectures.
## References:

1. [Real-time Object Detection with YOLO and Webcam: Enhancing Your Computer Vision Skills](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993)
   <br>
   - Special thanks to Dipankar Medhi for an article on YOLOV5 and how to use it on a camera!
