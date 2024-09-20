// document.addEventListener("DOMContentLoaded", function () {
//   const hamburgerIcon = document.getElementById("hamburger-icon");
//   const crossIcon = document.getElementById("cross-icon");
//   const navLinks = document.getElementById("nav-links");

//   // When the hamburger icon is clicked
//   hamburgerIcon.addEventListener("click", function () {
//     hamburgerIcon.style.display = "none"; // Hide hamburger icon
//     crossIcon.style.display = "block"; // Show cross icon
//     navLinks.classList.add("show"); // Show nav links
//   });

//   // When the cross icon is clicked
//   crossIcon.addEventListener("click", function () {
//     crossIcon.style.display = "none"; // Hide cross icon
//     hamburgerIcon.style.display = "block"; // Show hamburger icon
//     navLinks.classList.remove("show"); // Hide nav links
//   });
// });
const hamburgerIcon = document.getElementById("hamburger-icon");
const crossIcon = document.getElementById("cross-icon");
const navLinks = document.getElementById("nav-links");
console.log("gfxcvbhjkl");
hamburgerIcon.addEventListener("click", function () {
  hamburgerIcon.style.display = "none"; // Hide hamburger icon
  crossIcon.style.display = "block"; // Show cross icon
  navLinks.classList.add("show"); // Show nav links
});

crossIcon.addEventListener("click", function () {
  crossIcon.style.display = "none"; // Hide cross icon
  hamburgerIcon.style.display = "block"; // Show hamburger icon
  navLinks.classList.remove("show"); // Hide nav links
});
