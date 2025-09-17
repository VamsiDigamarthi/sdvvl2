window.addEventListener("scroll", function () {
  console.log("Scroll event listener attached");
  const heroCard = document.querySelector(".hero-second-inner-card");
  if (heroCard) {
    const rect = heroCard.getBoundingClientRect();

    // Check if the element is in the viewport
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      heroCard.classList.add("scroll-triggered");
    } else {
      heroCard.classList.remove("scroll-triggered");
    }
  }
});
