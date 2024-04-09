#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  let i = number;
  i++;
  theFunction(i);
}
module.exports = { addMeMaybe };
