# deno_robot

a manipulate Windows/Mac robot on Deno

## Set up

### library

```sh
pip3 install flask
pip3 install pyautogui
```

### server

```sh
python3 server.py
```

## Sample

```sh
deno run -A sample.js
```

```JavaScript
import { Robot } from "./Robot.js";
import { endpoint } from "./endpoint.js";

const r = new Robot(endpoint);

// about this mac
await r.mouseMove(10, 10);
await r.mouseClick();
await r.keyPress("down");
await r.keyPress("enter");
```
