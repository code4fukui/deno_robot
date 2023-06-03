import { Robot } from "./Robot.js";
import { endpoint } from "./endpoint.js";

const r = new Robot(endpoint);

// about this mac
await r.mouseMove(10, 10);
await r.mouseClick();
await r.keyPress("down");
await r.keyPress("enter");
