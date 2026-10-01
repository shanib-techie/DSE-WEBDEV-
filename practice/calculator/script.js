// function calculate(){
//     let a = Number(document.getElementById("n1").value);
//     let b = Number(document.getElementById("n2").value);
//     let op = document.getElementById("opp").value;
//     let r;

//     if(opp == "+")
//         r = a+b;
//     elseif (opp == "-")
//         r = a-b;
//     elseif(opp == "*")
//         r = a*b;
//     elseif(opp == "/")
//         r = a/b;
// document.getElementById("r").value = r;    
// }

// // function calculate() {
// //      let a = Number(document.getElementById("n1").value);
// //       let b = Number(document.getElementById("n2").value);
// //        let op = document.getElementById("op").value;
// //         let r; if (op == "+") r = a + b;
// //          else if (op == "-") r = a - b;
// //           else if (op == "*") r = a * b;
// //            else if (op == "/") r = b == 0 ? "Cannot divide by zero" : a / b; document.getElementById("result").value = r; }

// // function clearAll()
// //  { document.getElementById("n1").value = ""; 
// //     document.getElementById("n2").value = "";
// //      document.getElementById("op").value = "+";
// //       document.getElementById("result").value = ""; }


function calculate() {
    let a = Number(document.getElementById("n1").value);
    let b = Number(document.getElementById("n2").value);
    let op = document.getElementById("op").value;
    let r;

    if (op == "+")
        r = a + b;
    else if (op == "-")
        r = a - b;
    else if (op == "*")
        r = a * b;
    else if (op == "/")
        r = b == 0 ? "Cannot divide by zero" : a / b;

    document.getElementById("result").value = r;
}

function clearAll() {
    document.getElementById("n1").value = "";
    document.getElementById("n2").value = "";
    document.getElementById("op").value = "+";
    document.getElementById("result").value = "";
}