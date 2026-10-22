
// // alert("Welcome to JavaScript!");

// document.write("Hello Bhai!"); //html ki tarah msg show hoa


// console.log("My first JavaScript program");



// var name = "Rahul";
// var age = 20;
// document.write("<br>");
// document.write(name);
// document.write("<br>");
// document.write(age);




// var a = 10;
// let b = 20;
// const c = 30;

// a += 15; // Allowed
// b -= 5; // Allowed
// // c = 35; // Error: const cannot be reassigned

// console.log(a, b, c);

function changeText() {
    document.getElementById("heading").innerHTML = "Text Changed!";
}


function showName() {
    let userName = document.getElementById("name").value;

    document.getElementById("result").innerHTML = userName;
}

function changeColor() {
    document.getElementById("page").style.backgroundColor = "lightblue";
}

function singleClick() {
    document.getElementById("result").innerHTML = "Single click detected!";
}

function doubleClick() {
    document.getElementById("result").innerHTML = "Double click detected!";
}

function changecol(){
    document.getElementById("changecol").innerHTML ="now text chnage"
}


function addits10percent(){
    let  num = Number(document.getElementById("num").innerHTML);
    document.getElementById("num").innerHTML = num *1.1;

}

function changeColor(){
    document.getElementById("yellow").style.backgroundColor = "yellow";
    document.getElementById("yellow").style.border = "2px solid black";
}



// function changeColor_onmouseover(){
//     document.getElementById("demo").style.color = "pink";
//     document.getElementById("demo").style.border = "5px dotted yellow";
// }
// function resetColor (){
//         document.getElementById("demo").style.color = "black";

// }
function keyDown() {
    document.getElementById("result").innerHTML =
        "Key pressed!";
}

function keyUp() {
    document.getElementById("result").innerHTML =
        "Key released!";
}

function focusEvent() {
    document.getElementById("result").innerHTML =
        "Input box selected!";
}

function blurEvent() {
    document.getElementById("result").innerHTML =
        "You left the input box!";
}
// // var name = 99;

// let num = 55;

// const pink = 88;

// name += 10;
// num +=10;
// // pink -=10;

// log.console(name,num,pink)

// var name = "shanib";

// document.write("<br>" ,name + " khan")



// console.log(5 == "5");
// console.log(5 === "5");

// console.log(0 == false);
// console.log(0 === false);

// let fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"];

// console.log(fruits[0]);
// console.log(fruits[2]);
// console.log(fruits[4]);
// console.log(fruits.length);

// let name = prompt("Enter your name:");

// alert("Welcome, " + name);

// document.write("Hello, " + name);