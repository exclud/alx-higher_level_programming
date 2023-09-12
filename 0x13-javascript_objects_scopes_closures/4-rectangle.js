#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    if (this.width !== undefined && this.height !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
