function LinkedList() {
	this._length = 0;
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

		this._length++;
	},

	pop: function() {
		var current = this._head,
			previous;

		if(this._length == 1) {
			this._head = null;
			this._length--;
			console.log(current.data);
		} else if(this._length > 1) {
			for(i=0; i<(this._length - 1); i++) {
				previous = current;
				current = current.next
			}
			previous.next = null;
			this._length--;
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

	insert: function(data, index) {
		if(index >= 0 && index < this._length ) {
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
			this._length++;
		} else 
			console.log("Invalid index missus!");
	},

	remove: function(index) {
		if(index >= 0 && index < this._length ) {
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
			this._length--;
			console.log(current.data);
		} else 
			console.log("Invalid index missus!");
	}

}

var LL = new LinkedList();
LL.push(1)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(5)
LL.pop()
LL.remove(2)
LL.push(6)
LL.push(7)
LL.insert(8,2)
LL.print();