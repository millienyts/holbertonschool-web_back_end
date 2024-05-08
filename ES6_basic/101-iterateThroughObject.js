export default function iterateThroughObject(reportWithIterator) {
  let string = '';
  const separator = ' | ';
  console.log(reportWithIterator);
  for (const employeeName of reportWithIterator) {
    string = string + employeeName + separator;
  }
  if (string.endsWith(separator)) {
    string = string.slice(0, -separator.length);
  }
  return string;
}
