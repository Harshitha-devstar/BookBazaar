const slider = document.querySelector('.slider');
const slides = slider.children; // All slide elements
const totalSlides = slides.length;

let currentIndex = 0;

// Function to scroll to the next slide
function nextSlide() {
  currentIndex = (currentIndex + 1) % totalSlides; // Loop back to the first slide
  const scrollPosition = slides[currentIndex].offsetLeft; // Get the position of the next slide
  slider.scrollTo({
    left: scrollPosition,
    behavior: 'smooth'
  });
}

// Auto-slide every 2 seconds
setInterval(nextSlide, 2000);
