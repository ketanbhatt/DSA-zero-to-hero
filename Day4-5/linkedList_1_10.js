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
		var length = this.size();
		if(index >= 0 && index < length ) {
			var current = this._head,
				i = 0;
			while(i++ < index) {
				current = current.next
			}
			return current.data;
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

	sizeRecursive: function(node) {
		if(typeof(node) == "undefined") 
			node = this._head
		if(node == null)
			return 0;
		else
			return 1 + this.sizeRecursive(node.next);
	},

	searchIterative: function(key) {
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

	searchRecursive: function(key, node) {
		if(typeof(node) == "undefined") 
			node = this._head
		if(node == null)
			return false;
		else if(node.data == key)
			return true;
		else 
			return false || this.searchRecursive(key, node.next)
	}

};

var LL = new LinkedList();