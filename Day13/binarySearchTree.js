function BST() {
	this._root = null;
} 

BST.prototype = {
	
	constructor: BST,

	contains: function(value) {
		var found = false,
			current = this._root;

		while(!found && current) {
			if(current.value == value)
				found = true;

			else if(value > current.value)
				current = current.right;

			else
				current = current.left;
		}
		return found
	},

	add: function(value) {
		var node = {
			value: value,
			left: null,
			right: null
		},
			current = this._root;

		if(!current) {
			this._root = node;
		} else {
			while(true) {
				if(value > current.value){
					if(!current.right) {
						current.right = node;
						break;
					}						
					else 
						current = current.right
				}

				else if(value < current.value) {
					 if(!current.left){
						current.left = node;
						break;
					}
					else
						current = current.left
					
				}

				else
					break;
			}
		}
	},

	traverse: function(process) {

		var inOrder = function(t) {
			if(!t)
				return

			inOrder(t.left);
			process.call(this, t);
			inOrder(t.right);
		}

		inOrder(this._root);
	},

	size: function() {
		var len = 0;
		this.traverse(function(node) {
			len++
		})
		return len;
	},

	toArray: function() {
		var arr = [];
		this.traverse(function(node) {
			arr.push(node.value)
		})
		return arr;
	},

	toString: function() {
		return this.toArray().toString();
	}

}

var myBST = new BST();
myBST.add(3)
myBST.add(1)
myBST.add(2)
myBST.add(5)

console.log(myBST.toString())