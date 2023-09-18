#!/usr/bin/node

exports.callMeMoby = function (a, b) {
  for (let i = 0; i < a; i++) {
    b();
  }
};
