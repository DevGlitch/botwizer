# botwizer

Final Project for CSCI E-29, Fall 2020, Harvard University

<br>

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/DevGlitch/botwizer)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/DevGlitch/botwizer)
[![Build Status](https://travis-ci.com/DevGlitch/botwizer.svg?branch=develop)](https://travis-ci.com/DevGlitch/botwizer)
[![Maintainability](https://api.codeclimate.com/v1/badges/6f2f0051db57f72a0e58/maintainability)](https://codeclimate.com/github/DevGlitch/botwizer/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6f2f0051db57f72a0e58/test_coverage)](https://codeclimate.com/github/DevGlitch/botwizer/test_coverage)
[![GitHub license](https://img.shields.io/github/license/DevGlitch/botwizer)](https://github.com/DevGltich/botwizer/master/LICENSE)


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/DevGlitch/botwizer">
    <img src="images/botwizer_logo.jpg" alt="Logo" width="300" height="300">
  </a>
</p>

<br>

<!-- DESCRIPTION OF THE PROJECT -->
## Description

A wiser bot using object detections and best marketing practices to act like a human.


<!-- DEMO OF THE PROJECT -->
## Demo

<p align="center">
  <a href="https://youtu.be/v_kwtLhuve8">
    <img src="images/youtube.jpeg" alt="Logo" width="200" height="200">
  </a>
</p>

<!-- GETTING STARTED -->
## Getting Started

Follow the below instructions in order to be able to use botwizer on your machine.

### Prerequisites

* Firefox
   ```python
  $ brew install --cask firefox

  # or directly via their website:
  https://www.mozilla.org/en-US/firefox/new/
  ```

* Geckodriver
   ```python
  $ brew install geckodriver

  # or manually:
  https://github.com/mozilla/geckodriver
  ```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DevGlitch/botwizer.git
   ```

2. Download weights file
   ```python
   # Place this file in yolo.weights
   https://pjreddie.com/media/files/yolov3.weights
   ```

2. Create .env file with your credentials
   ```python
   # in .env
   username=________  # Your Insta username
   password=________  # Your Insta password
   ```

3. Add your targets and comments in dashboard.xlsx (Don't forget to save!)
    <p align="center">
      <a href="https://github.com/DevGlitch/botwizer">
        <img src="images/dashboard.png" alt="Logo" width="600">
      </a>
    </p>


### Options

1. Firefox headless mode
   ```python
   # actions.login
   opts.headless = True  # Browser running in background
   #or
   opts.headless = False # Browser visible when botwizer is running
   ```


### Running

To run botwizer
   ```
   python3 -m final_project
   ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Nicolas Morant - [LinkedIn](https://www.linkedin.com/in/nicolasmorant/)

Project Link: [https://github.com/DevGlitch/botwizer](https://github.com/DevGlitch/botwizer)
