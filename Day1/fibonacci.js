/*
Program to find the Nth fibonacci number
 */

var num = process.argv[2],
	first = 0, 
	second = 1,
	curr;

/*
Iterative
Time Complexity: O(n)
Space Complexity: O(1)
 */
if (num == 0)	
	curr = first;
else if (num == 1)
	curr = second;
else if (num > 1) {
	for(i=2; i<=num; i++) {
		curr = first + second;
		first = second;
		second = curr;
	}
}
console.log("Iterative => " + curr);

/*
Recursive
Time Complexity: O(2^n)
Space Complexity: O(n)
 */
var fibo = function(x) {
	if (x == 0)
		return 0;
	else if (x == 1)
		return 1;
	else
		return fibo(x-2) + fibo(x-1);
}
console.log("Recursive bitches! => " + fibo(num))