#!/usr/bin/node

exports.esrever = function (list) {
  const listreverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listreverse.push(list[i]);
  }

  return listreverse;
};
