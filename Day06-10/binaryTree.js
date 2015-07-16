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

var heightTree = function(t) {
	if(!t)
		return 0;

	var height = 0;
	return height = Math.max(heightTree(t.left), heightTree(t.right)) + 1;
}

var sizeTree = function(t) {
	if(!t)
		return 0;

	var size = sizeTree(t.left) + 1 + sizeTree(t.right)
	return size;

}

var preOrder = function(t) {
	if(!t)
		return;

	console.log(t.data);
	preOrder(t.left);
	preOrder(t.right);
}

var inOrder = function(t) {
	if(!t)
		return;

	inOrder(t.left);
	console.log(t.data);	
	inOrder(t.right);
}

var postOrder = function(t) {
	if(!t)
		return;

	postOrder(t.left);
	postOrder(t.right);
	console.log(t.data);
}

var levelOrder = function(t) {
	var queue = [];
	queue.push(t);
	while(true) {
		temp = queue.shift();

		if(!temp)
			return;

		console.log(temp.data);

		if(temp.left)
			queue.push(temp.left);
		if(temp.right)
			queue.push(temp.right);
	}
}

var levelOrderSpiral = function(t) {
	var ltr = [], rtl = [], rev = true;

	ltr.push(t);
	while(ltr[0] || rtl[0]) {
		
		while(ltr[0] && rev ) {
			temp = ltr.pop();
			if(!temp)
				return;

			console.log(temp.data);

			if(temp.left)
				rtl.push(temp.left);
			if(temp.right)
				rtl.push(temp.right);
		}
		while(rtl[0] && !rev) {
			temp = rtl.pop();
			if(!temp)
				return;

			console.log(temp.data);

			if(temp.right)
				ltr.push(temp.right);
			if(temp.left)
				ltr.push(temp.left);
		}
		rev = !rev;	

	}
}

var verticalOrder = function(t, hd, hash) {

	if(!t)
		return;

	if(hd in hash)
		hash[hd].push(t.data);
	else
		hash[hd] = [t.data];

	verticalOrder(t.left, hd-1, hash);
	verticalOrder(t.right, hd+1, hash);

}
var verticalOrderPrint = function(hash) {
	var max = Math.max.apply(Math, Object.keys(hash));
	var min = Math.min.apply(Math, Object.keys(hash));

	for(i=min; i<=max; i++){
		console.log(hash[i]);
	}
}

var topView = function(t, hd, hash) {

	if(!t)
		return;
	if(hd in hash)
		hash[hd].push(t.data)
	else
		hash[hd] = [t.data];
	topView(t.left, hd-1, hash);
	topView(t.right, hd+1, hash);

}
var topViewPrint = function(hash) {
	var max = Math.max.apply(Math, Object.keys(hash))
	var min = Math.min.apply(Math, Object.keys(hash));
	for(i = min; i <= max; i++){
		console.log(hash[i][0]);
	}
}

var leftView = function(t, height, hash) {
	var queue1 = [], queue2 = [], level = 0;
	queue1.push(t);
	while(level < height) {
		if(queue1.length) {
			while(queue1.length) {
				temp = queue1.shift();

				if(!temp)
					break;

				if(level in hash)
					hash[level].push(temp.data)
				else
					hash[level] = [temp.data];

				if(temp.left)
					queue2.push(temp.left);
				if(temp.right)
					queue2.push(temp.right);
			}
		} else if(queue2.length) {
			while(queue2.length) {
				temp = queue2.shift();

				if(!temp)
					break;

				if(level in hash)
					hash[level].push(temp.data)
				else
					hash[level] = [temp.data];

				if(temp.left)
					queue1.push(temp.left);
				if(temp.right)
					queue1.push(temp.right);
			}
		}
		level++;
	}
}

var bottomViewPrint = function(hash) {
	var max = Math.max.apply(Math, Object.keys(hash))
	var min = Math.min.apply(Math, Object.keys(hash));
	for(i = min; i <= max; i++){
		console.log(hash[i].pop());
	}
}

var boundaryLeaveView = function(t){
	if(t) {
		boundaryLeaveView(t.left);
		if(!t.left && !t.right) {
			console.log(t.data)
		}
		boundaryLeaveView(t.right);
	}
}
var boundaryLeftView = function(t) {
	if(!t)
		return;

	if(t.left){
		console.log(t.data)
		boundaryLeftView(t.left)
	} else if(t.right) {
		console.log(t.data)
		boundaryLeftView(t.right)
	}
}
var boundaryRightView = function(t) {
	if(!t)
		return;

	if(t.right){
		boundaryRightView(t.right)
		console.log(t.data)
	} else if(t.left) {
		boundaryRightView(t.left)
		console.log(t.data)
	}
}
var boundaryView = function(t) {
	if(!t)
		return;

	console.log(t.data);
	boundaryLeftView(t.left);
	boundaryLeaveView(t.left);
	boundaryLeaveView(t.right);
	boundaryRightView(t.right);
}

var nodeLevel = function(t, node, level){
	 if(!t)
	 	return -1

	 if(t.data == node)
	 	return level

	 var levelLeft = nodeLevel(t.left, node, level + 1)
	 var levelRight = nodeLevel(t.right, node, level + 1)

	 if(levelLeft == -1)
	 	return levelRight
	 else
	 	return levelLeft
}

var rootToLeaf = function(t, ar) {
	if(!t)
		return;

	ar.push(t.data)
	if(!t.left && !t.right) {
		console.log(ar)
	}

	rootToLeaf(t.left, ar)
	rootToLeaf(t.right, ar)
	ar.pop()
}

var diameter = function(t) {
	if(!t)
		return 0;

	var lheight = heightTree(t.left);
	var rheight = heightTree(t.right);

	var ldia = diameter(t.left)
	var rdia = diameter(t.right)

	return Math.max(lheight + rheight + 1, Math.max(ldia, rdia))
}

var mirrorTree = function(t) {
	if(!t)
		return;

	mirrorTree(t.left);
	mirrorTree(t.right);
	var temp = t.left;
	t.left = t.right;
	t.right = temp;
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
// insertBT(myTree, 5);
// insertBT(myTree, 6);
// insertBT(myTree, 7);
// insertBT(myTree, 8);
// insertBT(myTree, 9);
// insertBT(myTree, 10);


// console.log(heightTree(myTree))

// console.log(sizeTree(myTree))


// preOrder(myTree);

// inOrder(myTree);

// postOrder(myTree);

// levelOrder(myTree);

// levelOrderSpiral(myTree)

// var hash = {};
// verticalOrder(myTree, 0, hash);
// verticalOrderPrint(hash);



// var hash = {};
// topView(myTree, 0, hash);
// topViewPrint(hash);

// var hash = {};
// leftView(myTree, heightTree(myTree), hash);
// topViewPrint(hash);

// var hash = {};
// topView(myTree, 0, hash);
// bottomViewPrint(hash);

// boundaryView(myTree);

// console.log(nodeLevel(myTree, 5, 1));

// var ar = [];
// rootToLeaf(myTree, ar)

console.log(diameter(myTree));

// mirrorTree(myTree);
// levelOrder(myTree);


