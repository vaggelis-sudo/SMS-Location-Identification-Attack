# SMS Location Identification Attack

This repository contains the code and data associated with the accepted USENIX'23 paper titled "Freaky Leaky SMS: Extracting User Locations by Analyzing SMS Timings". The paper presents a novel technique for extracting user locations based on the analysis of SMS message timings.

## Abstract

Short Message Service (SMS) remains one of the most popular communication channels since its introduction in 2G cellular networks. In this paper, we demonstrate that merely receiving silent SMS messages regularly opens a stealthy side-channel that allows other regular network users to infer the whereabouts of the SMS recipient. The core idea is that receiving an SMS inevitably generates Delivery Reports whose reception bestows a timing attack vector at the sender. We conducted experiments across various countries, operators, and devices to show that an attacker can deduce the location of an SMS recipient by analyzing timing measurements from typical receiver locations. Our results show that, after training
an ML model, the SMS sender can accurately determine multiple locations of the recipient. For example, our model achieves up to 96% accuracy for locations across different countries, and 86% for two locations within Belgium. Due to the way cellular networks are designed,
it is difficult to prevent Delivery Reports from being returned to the originator making it challenging to thwart this covert attack without making fundamental changes to the network architecture.

## Code and Data Availability

The code and data associated with this paper will be made publicly available in this repository before the conference takes place. We are currently working on organizing and documenting the codebase to ensure its usability and reproducibility. We aim to provide clear instructions on how to run the code and utilize the provided data for further research and experimentation.

Please stay tuned for updates!

## How to Cite

If you use this code or data in your research or work, please cite the following paper:

## Citation

If you use this code or data in your research or work, please cite the following paper:

> Freaky Leaky SMS: Extracting User Locations by Analyzing SMS Timings

The citation details can be found in the [CITATION.cff](./CITATION.cff) file.

