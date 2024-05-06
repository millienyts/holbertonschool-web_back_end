export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var innertask = true;
    var innertask2 = false;
  }

  return [task, task2];
}
