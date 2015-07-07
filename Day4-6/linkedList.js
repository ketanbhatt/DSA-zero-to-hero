function LinkedList() {
	this._head = null;
}

LinkedList.prototype = {

	constructor: LinkedList,

	push: function(data) {
		var node = {
			data: data,
			next: null
		}, current;

		if(this._head === null) {
			this._head = node;
		} else {
			current = this._head;
			while(current.next) {
				current = current.next;
			}
			current.next = node
		}
	},

	pop: function() {
		var current = this._head,
			previous;
		var length = this.size();

		if(length == 1) {
			this._head = null;
			console.log(current.data);
		} else if(length > 1) {
			for(i=0; i<(length - 1); i++) {
				previous = current;
				current = current.next
			}
			previous.next = null;
			console.log(current.data);
		}
	},

	print: function() {
		var current = this._head,
			result = [];
		while(current) {
			result.push(current.data);
			current = current.next;
		}
		console.log(result);
	},

	item: function(index) {
		index = Math.floor(index);
		var length = this.size();
		if(index >= 0 && index < length ) {
			var current = this._head,
				i = 0;
			while(i++ < index) {
				current = current.next
			}
			return current;
		} else 
			return "Invalid index missus!";
	},

	insert: function(data, index) {
		var length = this.size();
		if(index >= 0 && index < length ) {
			var node = {
				data: data,
				next: null
			}, current = this._head,
				previous;

			if(index == 0) {
				this._head = node;
				node.next = current;
			} else {
				for(i=0; i<index; i++) {
					previous = current;
					current = current.next
				}
				previous.next = node;
				node.next = current;
			}
		} else 
			return "Invalid index missus!";
	},

	remove: function(index) {
		var length = this.size();
		if(index >= 0 && index < length ) {
			var current = this._head,
				previous;

			if(index == 0) {
				this._head = current.next;
			} else {
				for(i=0; i<index; i++) {
					previous = current;
					current = current.next
				}
				previous.next = current.next;
			}
			console.log(current.data);
		} else 
			return "Invalid index missus!";
	},

	size: function() {
		var current = this._head,
			count = 0;
		while(current) {
			current = current.next;
			count++;
		}
		return count;
	},

	search: function(key) {
		var current = this._head,
			flag = 0;
		while(current) {
			if(current.data == key) {
				flag = 1;
				return true;
			} else {
				current = current.next
			}
		}
		if(flag == 0)
			return false;
	},

	// Dont do this
	makeCycle: function() {
		current = this._head;
		while(current.next) {
			current = current.next;
		}
		current.next = this._head;
	}

};


// Get size of LL recusrively
LinkedList.prototype.sizeRecursive = function(node) {
	if(typeof(node) == "undefined") 
		node = this._head
	if(node == null)
		return 0;
	else
		return 1 + this.sizeRecursive(node.next);
};

// Search for key in LL recusrively
LinkedList.prototype.searchRecursive = function(key, node) {
	if(typeof(node) == "undefined") 
		node = this._head
	if(node == null)
		return false;
	else if(node.data == key)
		return true;
	else 
		return false || this.searchRecursive(key, node.next)
};

var LL = new LinkedList();
LL.push(1);
LL.push(4);
LL.push(6);
LL.push(8);
LL.push(9);

var LL2 = new LinkedList();
LL2.push(0);
LL2.push(2);
LL2.push(3);
LL2.push(8);
LL2.push(10);
LL2.push(11);
LL2.push(15);

// Printing middle node in the LL
console.log(LL.item(LL.size()/2).data);

LinkedList.prototype.printReverse = function() {
	var current = this._head,
		array = [],
		reverse = [];
	while(current) {
		array.push(current.data);
		current = current.next;
	}
	var size = array.length;
	for(i=0; i<size; i++)
		reverse.push(array.pop());

	return reverse;
}

LinkedList.prototype.reverseLinkedList = function() {
	var current = this._head,
		length = this.size(),
		previous, next;
	if(length > 1) {
		next = current.next;
		current.next = null;
		previous = current;
		current = next;
		while(current) {
			next = current.next;
			current.next = previous;
			previous = current;
			current = next;
		}
		this._head = previous;
	}	
}

// LL.reverseLinkedList();
// LL.print();

LinkedList.prototype.concatLL = function(L, index) {
	for(i=0; i<index; i++) {
		try {
			L = L.next;
		} catch (e) {
			return;
		}
	}
	while(L) {
		this.push(L.data);
		L = L.next;
	}
}

var mergeLL = function(L1, L2) {
	var L1current = L1.item(0),
		L2current = L2.item(0),
		mergedLL = new LinkedList(),
		countL1 = 0, countL2 = 0;

	while(L1current && L2current) {
		if(L1current.data < L2current.data) {
			mergedLL.push(L1current.data);
			L1current = L1current.next;
			countL1++;
		} else {
			mergedLL.push(L2current.data);
			L2current = L2current.next;
			countL2++;
		}
	}

	mergedLL.concatLL(L1.item(0), countL1)
	mergedLL.concatLL(L2.item(0), countL2)
	return	mergedLL;
}

var MLL = mergeLL(LL, LL2);
MLL.print();

// MLL.makeCycle();

var detectCycle = function(LL) {
	var turtle = LL._head,
		hare = LL._head;
	while(true) {
		if(!hare.next)
			return false;

		hare = hare.next;

		if(!hare.next)
			return false;

		hare = hare.next;
		turtle = turtle.next

		if(hare == turtle)
			return true;
	}
}

console.log(detectCycle(MLL));

