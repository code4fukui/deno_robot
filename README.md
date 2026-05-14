# deno_robot

> 日本語のREADMEはこちらです: [README.ja.md](README.ja.md)

A library for automating Windows/Mac mouse and keyboard actions from Deno.

This project uses a client-server architecture. A Deno client sends HTTP requests to a lightweight Python server, which uses `PyAutoGUI` to control the host machine's desktop.

## Features

-   **Mouse Control**: Move cursor, perform left and right clicks, and get the current mouse position.
-   **Keyboard Control**: Press and release individual keys, hold keys down, and type out strings.
-   **Screen Information**: Retrieve the screen's resolution.

## Requirements

-   Deno (for the client)
-   Python 3 (for the server)
-   Python libraries: `Flask`, `PyAutoGUI`

## How to Use

### 1. Server Setup (Python)

The server runs on the machine you want to control.

1.  **Install Python dependencies:**
    ```sh
    pip3 install flask pyautogui
    ```

2.  **(Optional) Configure Network Access:**
    By default, the server only accepts requests from `localhost` (`127.0.0.1` and `::1`). To allow other machines to connect, edit `allow_networks.json` and add the IP addresses or network ranges you want to grant access to.

3.  **Run the server:**
    ```sh
    python3 server.py
    ```
    *Note: The server runs on port 80 by default, which may require administrator or `sudo` privileges on some systems.*

### 2. Client Usage (Deno)

Run Deno scripts on any machine that can access the server.

1.  **Install Deno:**
    Follow the instructions at https://deno.land/

2.  **Run the example scripts:**
    The repository includes examples to demonstrate functionality.

    *   **Automate a sequence of actions (`sample.js`):**
        This script moves the mouse, clicks, and presses keys. On macOS, this sequence opens the "About This Mac" window.
        ```sh
        deno run -A sample.js
        ```

    *   **Watch the mouse position (`poswatch.js`):**
        This script continuously polls and prints the mouse coordinates whenever they change.
        ```sh
        deno run -A poswatch.js
        ```

### Using the `Robot` class in your own project

You can import the `Robot` class to create your own automation scripts.

```javascript
import { Robot } from "https://deno.land/x/deno_robot/Robot.js";
import { sleep } from "https://deno.land/x/sleep/mod.ts";

// Connect to the server. Defaults to "http://localhost/" if no endpoint is provided.
const robot = new Robot();

// Get screen dimensions
const screenSize = await robot.screenSize();
console.log("Screen size:", screenSize); // e.g., "1920,1080"

// Move the mouse to the center of the screen
const [width, height] = screenSize.split(",").map(Number);
await robot.mouseMove(width / 2, height / 2);
await sleep(1);

// Perform a right click
await robot.mouseClickRight();
await sleep(1);

// Type a message
await robot.keyType("Hello from Deno!");
```

## License

MIT License — see [LICENSE](LICENSE).