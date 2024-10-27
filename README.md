# VoIP to Audio Decoder Using Raspberry Pi
Intership project (4th year)

**Author**: Benoît Vidotto

**Polytech Mons (FPMs), UMONS, Belgium**

   <p align="center">
      <img src="./images/image24.webp" alt="bar" width="50%">
      </p><p align="center"><em>A schema of the testing protocol.</em>
   </p>

---


This project focuses on transforming Raspberry Pi devices into 4-channel SIP phones. This endeavor aims not only to innovate but also to perform a comparative study against existing SIP phones in terms of cost and performance.


   <p align="center">
      <img src="./images/image16.webp" alt="bar" width="50%">
      </p><p align="center"><em>The architecture.</em>
   </p>

### Key Components:
Utilizing the Asterisk software on the company's servers, this project enables effective VoIP communication, promising to enhance connectivity solutions.

## Equipment: Raspberry Pi

- **Model:** Raspberry Pi 3B+
- **Description:** A compact mini-computer approximately the size of a credit card, ideal for various applications.
- **Operating System:** Built on a Linux foundation, offering flexibility and performance.
- **Power Supply:** Operates on a 5-volt input, ensuring energy efficiency.
- **Storage:** Supports micro-SD cards, providing ample space for applications.
- **Audio Codecs:** Equipped with high-definition codecs for superior audio quality.
- **Cost:** Each unit was acquired for €34.72, representing a cost-effective solution for this project.

   <p align="center">
      <img src="./images/image17.webp" alt="bar" width="50%">
      </p><p align="center"><em>The Raspberry Pi 3B+</em>
   </p>


## Additional Equipment: Terracom TERRA-IEX & Zycoo X10

To effectively compare the Raspberry Pi solution, two existing SIP phones were evaluated:

- **Terracom TERRA-IEX:** A premium device priced between €500 and €700, offering high-end features.
- **Zycoo X10:** More affordable, priced between €120 and €200, providing basic functionalities.

   <p align="center">
      <img src="./images/image18.webp" alt="bar" width="33%">
      <img src="./images/image19.webp" alt="bar" width="33%">
      </p><p align="center"><em>TERRA_IEX (left) and Zycoo X1 (right)</em>
   </p>

## Cost Analysis

For a complete 4-channel SIP phone setup, the following components are necessary:
- **Network Switch:** To efficiently share the Ethernet connection across devices.
- **Power Supply:** A 5-volt power supply and a converter (12 or 24 volts) for the TERRA and Zycoo devices.

### Cost Efficiency
The Raspberry Pi prototype is exceptionally cost-effective, being **13 times cheaper** than the TERRA-IEX and **4 times cheaper** than the Zycoo, making it an attractive alternative for companies seeking to optimize costs without compromising quality.

   <p align="center">
      <img src="./images/image22.webp" alt="bar" width="60%">
      </p><p align="center"><em>Cost analysis of the different options (Food has been wrongly translated from "Power Supply")</em>
   </p>


## Testing Protocol

To ensure the system operates effectively, a structured testing protocol was implemented:

1. Alice initiates a call to Bob through the server, playing an audio signal.
2. The Asterisk server efficiently redirects the call to Bob.
3. Bob accepts the call and sends the audio signal back to Alice via an audio cable.
4. Alice records the audio signal received for analysis.

   <p align="center">
      <img src="./images/image24.webp" alt="bar" width="33%">
      </p><p align="center"><em>A schema of the testing protocol.</em>
   </p>

### Normalized Volume
To maintain consistent sound levels and avoid distortion, all SIP phones were calibrated using an oscilloscope prior to testing.

   <p align="center">
      <img src="./images/image25.webp" alt="bar" width="33%">
      <img src="./images/image26.webp" alt="bar" width="33%">
      <img src="./images/image27.webp" alt="bar" width="30%">
      </p><p align="center"><em>Raspberry Pi (left), Zycoo X1 (middle) and TERRA-IEX (right)</em>
   </p>

## Testing Results: Frequency at 1 kHz

The tests aimed to determine the presence of harmonics and their amplitudes compared to the source signal. The results revealed that:

- The Raspberry Pi outperformed its competitors, showcasing its superior audio processing capabilities.
- The TERRA-IEX, conversely, displayed significantly poorer performance.

   <p align="center">
      <img src="./images/image28.webp" alt="bar" width="33%">
      </p><p align="center"><em>Source at 1 kHz.</em>
   </p>
   <p align="center">
      <img src="./images/image29.webp" alt="bar" width="33%">
      <img src="./images/image30.webp" alt="bar" width="32%">
      <img src="./images/image31.webp" alt="bar" width="33%">
      </p><p align="center"><em>Resulting tests for the devices? Raspberry Pi (left), Zycoo X1 (middle) and TERRA-IEX (right)</em>
   </p>

## Testing Results: Frequency Sweep from 300 to 3400 Hz

This phase involved comparing the audio fidelity of the three devices over a range of frequencies (frequencies heard by humans). Key observations included:

- The device curves were expected to closely match the source curve.
- Any harmonics outside the designated frequency band were considered noise interference.
- Again, the Raspberry Pi demonstrated superior performance, while the TERRA-IEX exhibited serious deficiencies.

   <p align="center">
      <img src="./images/image32.webp" alt="bar" width="33%">
      </p><p align="center"><em>Source from 300 to 3400 kHz.</em>
   </p>
   <p align="center">
      <img src="./images/image33.webp" alt="bar" width="33%">
      <img src="./images/image34.webp" alt="bar" width="32%">
      <img src="./images/image35.webp" alt="bar" width="33%">
      </p><p align="center"><em>Resulting tests for the devices. Raspberry Pi (left), Zycoo X1 (middle) and TERRA-IEX (right)</em>
   </p>

## Conclusion - VoIP

The Raspberry Pi prototype reveals a compelling case for its adoption:
- It offers substantial cost savings compared to both competitors.
- The audio quality is notably superior, making it suitable for various communication needs.
- Its compact size enhances practicality, allowing for easy integration into existing systems.


   <p align="center">
      <img src="./images/image36.webp" alt="bar" width="50%">
      </p><p align="center"><em>Work setup</em>
   </p>

### Improvement Prospects
Looking ahead, several enhancements can be made:
- **Custom Enclosure:** Developing an appropriate enclosure to house the prototype, ideally measuring a minimum of 15x15x15 cm, to ensure durability and aesthetic appeal.

   <p align="center">
      <img src="./images/image38.webp" alt="bar" width="50%">
      </p><p align="center"><em>A concept of a box containing the 4 Raspberrys stacked.</em>
   </p>
      <p align="center">
      <img src="./images/image37.webp" alt="bar" width="20%">
      </p><p align="center"><em>The Raspberrys stacked.</em>
   </p>

- **Web Interface:** Creating a user-friendly web interface to streamline communication between the Raspberry Pi and PC, enhancing user interaction.

   <p align="center">
      <img src="./images/image39.webp" alt="bar" width="33%">
      <img src="./images/image40.webp" alt="bar" width="33%">
      </p><p align="center"><em>Existing command line interface.</em>
   </p>

### Installation
Instructions for the installation on Raspberry are available in raspberry.md

## Authors & contributors

The original setup of this repository is by [Benoît Vidotto](https://github.com/bvidotto).

## License

MIT License

Copyright (c) 2024 Benoît Vidotto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.