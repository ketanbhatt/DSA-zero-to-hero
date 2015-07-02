/*
Program to Sort an array 
 */

var input = [4,4,5,1,2,10,3];
console.log("Input String => " + input);

/*
Selection Sort
TIme Complexity: O(n^2)
Space Complexity: O(1)
 */
var input_sel = input.slice(),
	min, pos;
for (i=0; i<input_sel.length; i++) {
	min = input_sel[i];
	pos = i;
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

/*
Bubble Sort
TIme Complexity: O(n^2)
Space Complexity: O(1)
 */
var input_bub = input.slice(),
	temp, flag;
for (i=0; i<input_bub.length; i++) {
	flag = 0;
	for (j=0; j<input_bub.length - i; j++) {
		if(input_bub[j] > input_bub[j+1]) {
			temp = input_bub[j];
			input_bub[j] = input_bub[j+1];
			input_bub[j+1] = temp;
			flag = 1;
		}
	}
	if (flag == 0)
		break;
}
console.log("Bubble Sort => " + input_bub);