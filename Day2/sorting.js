/*
Program to Sort an array 
 */

var input = [4,4,5,1,2,10,3],
	min, pos;
console.log("Input String => " + input);

/*
Selection Sort
TIme Complexity: O(n^2)
Space Complexity: O(1)
 */
var input_sel = input.slice();
for (i=0; i<input_sel.length; i++) {
	min = input_sel[i];
	for (j=i+1; j<input_sel.length; j++) {
		if (min > input_sel[j]) {
			min = input_sel[j];
			pos = j;
		}
	}
	input_sel[pos] = input_sel[i];
	input_sel[i] = min;
}
console.log("Selection Sort => " + input_sel)