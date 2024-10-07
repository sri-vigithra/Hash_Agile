function rotateLeft(s, k) {
    let n = s.length;
    k = k % n; // In case k is greater than the length of the string
    let rotatedStr = '';
 
    // Append characters starting from the kth index
    for (let i = k; i < n; i++) {
        rotatedStr += s[i];
    }
 
    // Append characters from the start of the string to the kth index
    for (let i = 0; i < k; i++) {
        rotatedStr += s[i];
    }
 
    return rotatedStr;
}
 
// Example usage:
let s = "abcdef";
let k = 2;
console.log(rotateLeft(s, k)); // Output: "cdefab"