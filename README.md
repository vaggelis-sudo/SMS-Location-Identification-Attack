# SMS Location Identification Attack

This repository contains the code and data associated with the accepted USENIX'23 paper titled "Freaky Leaky SMS: Extracting User Locations by Analyzing SMS Timings". The paper presents a novel technique for extracting user locations based on the analysis of SMS message timings.

## Abstract

Short Message Service (SMS) remains one of the most popular communication channels since its introduction in 2G cellular networks. In this paper, we demonstrate that merely receiving silent SMS messages regularly opens a stealthy side-channel that allows other regular network users to infer the whereabouts of the SMS recipient. The core idea is that receiving an SMS inevitably generates Delivery Reports whose reception bestows a timing attack vector at the sender. We conducted experiments across various countries, operators, and devices to show that an attacker can deduce the location of an SMS recipient by analyzing timing measurements from typical receiver locations. Our results show that, after training
an ML model, the SMS sender can accurately determine multiple locations of the recipient. For example, our model achieves up to 96% accuracy for locations across different countries, and 86% for two locations within Belgium. Due to the way cellular networks are designed,
it is difficult to prevent Delivery Reports from being returned to the originator making it challenging to thwart this covert attack without making fundamental changes to the network architecture.

## Code and Data Availability

A POC code and data associated with this paper will be made publicly available in this repository once the licensing is determined. We are also working on organizing and documenting the codebase to ensure its usability and reproducibility. We aim to provide clear instructions on how to run the code and utilize the provided data for further research and experimentation.

Please stay tuned for updates!

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

