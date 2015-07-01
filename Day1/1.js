var num = process.argv[2],
	first = 0, 
	second = 1,
	curr;

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

console.log(curr);