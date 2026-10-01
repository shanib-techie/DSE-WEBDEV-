function showProject(projectName) {
    alert("You selected: " + projectName);
}

document.querySelectorAll("nav a").forEach(function(link) {
    link.addEventListener("click", function() {
        console.log("Opening " + link.textContent + " section");
    });
});