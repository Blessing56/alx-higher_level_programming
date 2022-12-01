#!/usr/bin/node

/*const num_args = process.argv.length;
if (num_args === 0){
	console.log("No argument");
}
else if (num_args === 1){
	console.log("Argument found");
}
else{
	console.log("Arguments found");
}*/

const count = process.argv.length;
if (count > 3) {
  console.log('Arguments found');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
