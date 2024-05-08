export default function createIteratorObject(report) {
  const arrayOfEmployees = [];
  // .allEmployees is an array of employee names
  for (const employees of Object.values(report.allEmployees)) {
    arrayOfEmployees.push(...employees);
  }

  return arrayOfEmployees;
}
