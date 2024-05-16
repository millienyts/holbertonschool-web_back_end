export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const data = 1;
    if (data) {
      resolve();
    } else {
      reject();
    }
  });
}
