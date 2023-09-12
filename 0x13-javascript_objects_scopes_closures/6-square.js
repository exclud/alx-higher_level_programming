#!/usr/bin/node
class Square extends Rectangle {
    constructor (size) {
      super(size, size);
    }

    charPrint(c) {
        if (c === undefined) {
            c = 'X'
        }

        for (let i = 0; i < this.size; i++){
            console.log(c.repeat(this.size));

        }
    }
  }

class Square extends Square {
  constructor(size) {
    super(size);
  }
}
