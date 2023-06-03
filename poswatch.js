import { Robot } from "./Robot.js";
import { sleep } from "https://js.sabae.cc/sleep.js";
import { endpoint } from "./endpoint.js";

const r = new Robot(endpoint);

let bks = null;
for (;;) {
  const s = await r.mousePosition();
  if (s != bks) {
    console.log(s);
  }
  await sleep(100);
  bks = s;
}
