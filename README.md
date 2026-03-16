# deno_robot

> 日本語のREADMEはこちらです: [README.ja.md](README.ja.md)

A library for manipulating a Windows/Mac robot using Deno.

## Features
- Control mouse movement and clicks
- Send keyboard input
- Retrieve screen size and mouse position

## Requirements
- Python 3
- Flask, PyAutoGUI

## Usage

### Server Setup
1. Install required libraries:
   ```sh
   pip3 install flask
   pip3 install pyautogui
   ```
2. Run the server:
   ```sh
   python3 server.py
   ```

### Client Usage
1. Install Deno: https://deno.land/
2. Run the sample script:
   ```sh
   deno run -A sample.js
   ```

The sample script demonstrates the following actions:
- Move the mouse to coordinates (10, 10)
- Click the mouse
- Press the "down" key
- Press the "enter" key

## License
MIT License — see [LICENSE](LICENSE).