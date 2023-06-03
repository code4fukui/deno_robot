const base = "http://localhost/";

export class Robot {
  constructor(endpoint = "http://localhost/") {
    this.endpoint = endpoint;
  }
  async get(path) {
    return await (await fetch(this.endpoint + path)).text();
  }
  async mouseMove(x, y) {
    return await this.get(`mouseMove/${x},${y}`);
  }
  async mouseClick() {
    return await this.get(`mouseClick`);
  }
  async mouseClickRight() {
    return await this.get(`mouseClickRight`);
  }
  async mousePosition() {
    return await this.get(`mousePosition`);
  }
  async keyPress(key) {
    return await this.get(`keyPress/${key}`);
  }
  async keyDown(key) {
    return await this.get(`keyDown/${key}`);
  }
  async keyUp(key) {
    return await this.get(`keyUp/${key}`);
  }
  async keyType(s) {
    return await this.get(`keyType/${s}`);
  }
}
