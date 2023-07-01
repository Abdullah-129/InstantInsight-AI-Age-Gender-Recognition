<h1 align="center">Real-Time Age and Gender Detection with Video Ads</h1>

<p align="center">
  <a href="https://ibb.co/PT0hzLK"><img src="https://i.ibb.co/Rhd04Ff/Whats-App-Image-2023-06-23-at-23-52-51.jpg" alt="Whats-App-Image-2023-06-23-at-23-52-51" border="0"></a>
</p>

<p align="center">This project demonstrates real-time age and gender detection using OpenCV and deep learning models. The application captures video from the default camera and detects faces in the frames using an OpenCV face detection model. Once a face is detected, the application determines the age and gender of the person and plays a targeted video ad based on these attributes.</p>

<h2>Features</h2>

<ul>
  <li>Real-time age and gender detection using deep learning models</li>
  <li>Dynamic selection of video ads based on age and gender</li>
  <li>Display of video ads while faces are detected</li>
  <li>Supports detection of multiple faces simultaneously</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.6 or above</li>
  <li>OpenCV 4.5 or above</li>
  <li>Deep learning models (included in the project):
    <ul>
      <li>OpenCV face detection model:
        <ul>
          <li><code>opencv_face_detector.pbtxt</code></li>
          <li><code>opencv_face_detector_uint8.pb</code></li>
        </ul>
      </li>
      <li>Age prediction model:
        <ul>
          <li><code>age_deploy.prototxt</code></li>
          <li><code>age_net.caffemodel</code></li>
        </ul>
      </li>
      <li>Gender prediction model:
        <ul>
          <li><code>gender_deploy.prototxt</code></li>
          <li><code>gender_net.caffemodel</code></li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/your-username/realtime-age-gender-detection.git</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Download the required model files:
    <ul>
      <li>OpenCV face detection model:
        <ul>
          <li><code>opencv_face_detector.pbtxt</code></li>
          <li><code>opencv_face_detector_uint8.pb</code></li>
        </ul>
      </li>
      <li>Age prediction model:
        <ul>
          <li><code>age_deploy.prototxt</code></li>
          <li><code>age_net.caffemodel</code></li>
        </ul>
      </li>
      <li>Gender prediction model:
        <ul>
          <li><code>gender_deploy.prototxt</code></li>
          <li><code>gender_net.caffemodel</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Place the downloaded model files in the project directory.</li>
</ol>

<h2>Usage</h2>

<ol>
  <li>Run the following command to start the application:
    <pre><code>python main.py</code></pre>
  </li>
  <li>The application will open a window displaying the camera feed.</li>
  <li>When a face is detected, the application will determine the age and gender of the person and play a targeted video ad based on these attributes.</li>
  <li>The video ads are stored in separate folders based on gender and age. Make sure to organize your video ads accordingly in the <code>Male</code> and <code>Female</code> folders, each containing subfolders for different age groups (e.g., <code>(0-2)</code>, <code>(4-6)</code>, etc.).</li>
  <li>If a video file is not found or if no face is detected, appropriate messages will be displayed in the application window.</li>
</ol>

<h2>Contributing</h2>

<p>Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<h2>Acknowledgments</h2>

<ul>
  <li>The age and gender prediction models are based on the work of <a href="https://talhassner.github.io/home/publication/2015_CVPR">Gil Levi and Tal Hassner</a>.</li>
  <li>The face detection model is based on the work of <a href="https://github.com/opencv/opencv">OpenCV</a>.</li>
</ul>

<h2>References</h2>

<ul>
  <li><a href="https://opencv.org">OpenCV</a></li>
  <li><a href="https://talhassner.github.io/home/publication/2015_CVPR">Age and Gender Classification Using Convolutional Neural Networks</a></li>
</ul>
