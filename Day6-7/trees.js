function BinaryTree(data) {
	this.data = data;
	this.left = null;
	this.right = null;
}

var insertBT = function(t, data) {
	var node = new BinaryTree(data);
	var queue = [];
	queue.push(t);
	while(true) {
		temp = queue.shift();
		if(!temp.left) {
			temp.left = node;
			return;
		} else 
			queue.push(temp.left);
		if(!temp.right) {
			temp.right = node;
			return;
		} else
			queue.push(temp.right)
	}
}

var preOrder = function(t) {
	if(!t)
		return;

	console.log(t.data);
	preOrder(t.left);
	preOrder(t.right);
}


var myTree = new BinaryTree(1);
insertBT(myTree, 2);
insertBT(myTree, 3);
insertBT(myTree, 4);
insertBT(myTree, 5);
insertBT(myTree, 6);
insertBT(myTree, 7);
insertBT(myTree, 8);
insertBT(myTree, 9);
insertBT(myTree, 10);
preOrder(myTree);
