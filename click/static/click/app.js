
var canvas = document.getElementById("C");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#000000";
ctx.fillRect(0, 0, canvas.clientHeight, canvas.clientWidth);

function drawSquare(x,y,color) {
	ctx.fillStyle = color;
	ctx.fillRect(x, y, 10, 10);
}

function clicked(){
    var x = event.clientX;
    var y = event.clientY;
    drawSquare(x, y, #FFFFFF)
}