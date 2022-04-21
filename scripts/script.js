// Obtains the first instances toggle buttons and main menu
const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navbarmainmenu = document.getElementsByClassName("main-menu")[0];

// If anywhere else other than the
toggleButton.addEventListener("click", () => {
    navbarmainmenu.classList.toggle("active");
});
