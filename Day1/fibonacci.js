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
Time Complexity: Exponential
Space Complexity: Exponential
 */
var fiboRec = function(x) {
	if (x == 0)
		return 0;
	else if (x == 1)
		return 1;
	else
		return fiboRec(x-1) + fiboRec(x-2);
}
console.log("Recursive bitches! => " + fiboRec(num))


/*
Recursive with Memoization
Time Complexity: O(n)
Space Complexity: O(n)
 */
var cache = [];
cache.push(0);
cache.push(1);
var fiboMem = function(x) {
	if (x < cache.length) {
		return cache[x];
	} else {
		cache[x] = fiboMem(x-1) + fiboMem(x-2);
		return cache[x];
	}
}
console.log("Memoization => " + fiboMem(num))


/*
Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
 */
var fiboDp = function(x) {
	var mem = [];
	mem.push(0);
	mem.push(1);

	for(i=2; i<=x; i++)
		mem.push(mem[i-1] + mem[i-2]);
	
	return mem[x]; 
}
console.log("Dynamic Programming => " + fiboDp(num))
