document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();

    let username = document.querySelector("input[type='text']").value;
    let password = document.querySelector("input[type='password']").value;

    if (username === "" || password === "") {
        alert("Please enter username and password");
    } else {
        alert("Login successful!");
    }
});