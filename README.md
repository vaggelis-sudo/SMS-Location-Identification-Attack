
# SMS Location Identification Attack

This repository contains the code and data associated with the [USENIX'23 paper](https://www.usenix.org/system/files/usenixsecurity23-bitsikas.pdf) titled "Freaky Leaky SMS: Extracting User Locations by Analyzing SMS Timings". The paper presents a novel technique for extracting user locations based on the analysis of SMS timings.

## Setup

### Ensure your system is up-to-date:
```bash
sudo apt update
```

### Install Python 3
Python 3 is required for running the scripts (if not installed already):
```bash
sudo apt install python3
```

### Install Android Development Tools
Install Android Debug Bridge (ADB) and Fastboot for Android device interactions:
```bash
sudo apt install android-tools-adb android-tools-fastboot
```

### Install Python Package Manager (pip)
If `pip` is not pre-installed, install it as follows:
```bash
sudo easy_install pip
```

### Install Required Python Libraries
Install libraries necessary for data processing and machine learning (at least):
```bash
pip install pandas scikit-learn numpy
```

### Enable USB Debugging for ADB
1. Go to `Settings > About phone`.
2. Tap `Build number` seven times to unlock developer options.
3. Return to `Settings`, find `Developer options`, and enable `USB debugging`.

### Install Java Development Kit (JDK) and Android Studio
Java SDK is essential for Android app development and compilation. Check the [official website](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
Download and install Android Studio, the IDE for Android development, from the [official website](https://developer.android.com/studio). Follow the setup wizard in Android Studio to install necessary SDK tools and components.

## SMS Transmission Control

The transmission control works first by setting up the cronjob in the Linux environment, which automates the process. Use the `crontab -e` to write a cronjob.
For example, `*/30 * * * * /path/to/initial_script.sh` executes the script every 30 minutes. Make sure that you give the executable permissions to the script
`chmod +x /path/to/initial_script.sh`. In the `initial_script.sh` add the ADB code of your sending device, the receiver's number, and the number of iterations. These
will be passed to the `runner.py` script every time it is executed. Modify it as you prefer.

The `runner.py` script is responsible for invoking the application on the phone and for executing the SMS transmissions based on the input. First, it starts the corresponding activity (make modifications based on your application). Then, it controls the interface to pass the phone number to the application and presses the button to send an SMS. This requires to identify the correct/matching coordinates on different devices. Therefore, enable `pointer location` on Android's Developer Options to identify the XY values required for the application. In addition, make sure that the `ADB_PATH = '/path/to/adb'` is correct, and that your computer has identified the device in the `adb devices` output. Overall, the script automates the following process (one iteration):

1. Wakes up the device.
2. Stops the messaging app if running.
3. Starts the messaging app.
4. Sends an SMS message.
5. Returns to the home screen and turns off the screen.

## SMS Application

The application is responsible for sending the actual SMS message in a correct and error-free process, and for collecting the measurements. The measurements are written in a 
file in memory which can be retrieved for processing. The `AndroidManifest.xml` shows the configurations and permissions needed for the application, and the `activity_main.xml` presents the design (bar for the "Phone Number" and button for "Send"). This design was selected in order to facilitate manual transmissions too, but it is optional.  

For security reasons though, the application code (of the `SMSActivity.java`) cannot be public. However...instructions:

1. Start by including necessary Android package imports for handling SMS, telephony, permissions, UI elements, etc.
2. Define the `SMSActivity` class extending `AppCompatActivity` with various class variables like `EditText`, `Button`, `SmsManager`, and others.
3. In the `onCreate` method, initialize UI components and set an onClickListener for the send button to perform checks and execute SMS sending.
6. Create a `sendSMS` method to prepare and send SMS using `SmsManager`, including PendingIntent for sent and delivered statuses.
7. Implement BroadcastReceivers for handling SMS sent and delivered actions, updating timestamps, and displaying Toast messages.
8. Once the SMS transmission is complete, compute the measurements (based on the paper's methodology) and store them.

Nonetheless, the application is not enough to indicate a successful procedure. You must separately and closely monitor the baseband logs (e.g, `adb logcat -b radio > baseband_logs.txt`) to verify the successful transmission of SMSs and reception of Delivery Reports. Ensure that there is synchronization between the application and logs for the measurement collection, and focus on the AT commands. Devices and modems may have different log structures and formats. 

Additionally, it is important to collect information about your network. This could be achieved by amalgamating data from three key sources: your application (they can be used for network checks as well), the baseband logs, and the device's dial codes (e.g., `*3001#12345#*` for iphone, and `*#*#4636#*#*` for Android).

## ML Model & Data

The `model.py` contains the main MLP classifier with cross-validation and a simple function for fine-tuning the hyperparameters of the MLP classifier. To ensure correct ML training and prediction, the dataset intended for input into this model may require thorough preprocessing. This preprocessing stage typically involves:

1. **Data Cleaning:** Identify and remove any erroneous data points or anomalies present within the dataset.

2. **Outlier Detection and Removal:** Detect data points that excessively deviate from the norm, and exclude them from the dataset.

3. **Dataset Formatting:** The data must be structured correctly with the well-defined features. This involves ensuring that each input feature is in a format that the MLP classifier can interpret and utilize.

Please refer to the [paper](https://arxiv.org/pdf/2306.07695.pdf) for more information.

## Future Directions

1. We may provide additional functionalities in the future (in allignment with the patenting guidelines), including automated selection and preprocessing of measurements from extensive datasets. These functionalities aim to streamline the preparation phase of the data before entering the training pipeline. 

2. While the repository may not be fully active, for any questions, clarifications, or suggestions, please do not hesitate to reach out at [vaggelisbtks@gmail.com](mailto:vaggelisbtks@gmail.com).

## Citation

If you use this code or data in your research or work, please cite the following paper:

<blockquote style="background-color: #f7f7f7; padding: 10px; border-left: 6px solid #1f618d;">

<pre>
@inproceedings{bitsikas2023freaky,
  <span style="color: #c0392b;">title = {Freaky Leaky SMS: Extracting User Locations by Analyzing SMS Timings},</span>
  <span style="color: #2980b9;">author = {Bitsikas, Evangelos and Schnitzler, Theodor and Pöpper, Christina and Ranganathan, Aanjhan},</span>
  <span style="color: #27ae60;">booktitle = {32nd USENIX Security Symposium, Anaheim, CA, USA, August 9-11, 2023},</span>
  <span style="color: #8e44ad;">year = {2023},</span>
  <span style="color: #e67e22;">url = {https://www.usenix.org/conference/usenix'23}</span>
}
</pre>
</blockquote>

