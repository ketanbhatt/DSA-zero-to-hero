function DoublyLinkedList() {
	this._head = null;
}

DoublyLinkedList.prototype = {

	constructor: DoublyLinkedList,

	push: function(data){
		var node = {
			data: data,
			next: null,
			prev: null
		}, current;

		if(this._head === null) {
			this._head = node;
		} else {
			current = this._head;
			while(current.next) {
				current = current.next;
			}
			current.next = node;
			node.prev = current;
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
	}
}

DoublyLinkedList.prototype.insertSorted = function (data) {
	var node = {
		data: data,
		next: null,
		prev: null
	}, current = this._head,
		previous, i = 0;

	while(current){
		i++;
		if(current.data > data && i == 1 ) {
			node.next = current;
			current.prev = node;
			this._head = node;
			return;
		}
		if(current.data > data) {
			current.prev.next = node;
			current.prev = node;
			node.next = current;
			return;
		}
		previous = current;
		current = current.next
	}

	previous.next = node;
	node.prev = previous;
}

var DLL = new DoublyLinkedList();
DLL.push(1);
DLL.push(2);
DLL.push(3);
DLL.push(4);
DLL.push(5);
DLL.push(7);
DLL.push(8);
DLL.print();

DLL.insertSorted(10);
DLL.print();

DoublyLinkedList.prototype.reverseDLL = function() {
	var current = this._head,
		previous, next;

	while(current) {
		previous = current.prev;
		next = current.next;
		current.next = previous;
		current.prev = next;
		previous = current;
		current = next;
	}
	this._head = previous;
}

DLL.reverseDLL();
DLL.print();

