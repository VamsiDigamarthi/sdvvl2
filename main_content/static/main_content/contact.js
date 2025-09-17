console.log("ytiuhg;");

document.addEventListener("DOMContentLoaded", function () {
  // Check if the form has any errors
  const form = document.getElementById("contactForm");
  if (form) {
    const errorMessages = form.querySelectorAll(".error-message");
    if (errorMessages.length > 0) {
      // Scroll to the form smoothly if there are error messages
      form.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
});
