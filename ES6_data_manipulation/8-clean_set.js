export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const values = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        values.push(item.slice(startString.length));
      }
    }
    return values.join('-');
  }
  // Return an empty string if the set is not a `Set` obj or `startString` is not a str
  return '';
}
