// Initialize a WeakMap to store endpoint usage counts
const weakMap = new WeakMap();

// Export the WeakMap instance
export { weakMap };

// Function to query the API and track usage
export function queryAPI(endpoint) {
  // Get the current count for this endpoint from the WeakMap
  let count = weakMap.get(endpoint) || 0;
  
  // Increment the count
  count++;
  
  // Update the count in the WeakMap
  weakMap.set(endpoint, count);
  
  // Check if the count is >= 5
  if (count >= 5) {
    // If so, throw an error
    throw new Error('Endpoint load is high');
  }
}
