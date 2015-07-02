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
var input_sel = input.slice();
for (i=0; i<input_sel.length; i++) {
	var min = input_sel[i];
	var pos = i;
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
var input_bub = input.slice();
for (i=0; i<input_bub.length; i++) {
	var flag = 0;
	for (j=0; j<input_bub.length - i; j++) {
		if(input_bub[j] > input_bub[j+1]) {
			var temp = input_bub[j];
			input_bub[j] = input_bub[j+1];
			input_bub[j+1] = temp;
			flag = 1;
		}
	}
	if (flag == 0)
		break;
}
console.log("Bubble Sort => " + input_bub);


/*
Insertion Sort
TIme Complexity: O(n^2)
Space Complexity: O(1)
 */
var input_ins = input.slice();
for(i=1; i<input_ins.length; i++) {
	var curr = input_ins[i];
	for (j=i-1; j>=0; j--) {
		if (input_ins[j] > curr) {
			input_ins[j+1] = input_ins[j];
		} else
			break;
	}
	input_ins[j+1] = curr;
}
console.log("Insertion Sort => " + input_ins);


/*
Merge Sort
TIme Complexity: O(nlogn)
Space Complexity: O(n)
 */
var input_mer = input.slice();
var mergeSort = function(array) {
	if (array.length < 2)
		return array;
	var mid = array.length/2;
	var left = array.slice(0, mid);
	var right = array.slice(mid);
	return merge(mergeSort(left), mergeSort(right));
}
var merge = function (left, right) {
	var A = [];
	var i = 0, j = 0;
	while (i < left.length && j < right.length) {
		if(left[i] <= right[j]) {
			A.push(left[i++]);
	 	} else {
	 		A.push(right[j++]);
	 	}
	}
      return A.concat(left.slice(i)).concat(right.slice(j));
}
console.log("Merge Sort => " + mergeSort(input_mer))