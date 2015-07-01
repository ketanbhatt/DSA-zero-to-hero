var num = process.argv[2];

var fibo = function(x) {
	if (x == 0)
		return 0;
	else if (x == 1)
		return 1;
	else
		return fibo(x-2) + fibo(x-1);
}

console.log(fibo(num))