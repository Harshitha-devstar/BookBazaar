document.addEventListener("DOMContentLoaded", () => {
            let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// Set interval for auto-slide every 60 seconds (60000 milliseconds)
setInterval(() => {
  plusSlides(1);  // Move to the next slide
}, 3000); // 10 sec


document.getElementById("login-link").onclick = function(event) {
        event.preventDefault();
        document.getElementById("login-modal").style.display = "block";
    };

    document.querySelector(".login-close").onclick = function() {
        document.getElementById("login-modal").style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == document.getElementById("login-modal")) {
            document.getElementById("login-modal").style.display = "none";
        }
    };
    document.getElementById("signup-link").onclick = function(event) {
        event.preventDefault();
        document.getElementById("signup-modal").style.display = "block";
    };

    document.querySelector(".signup-close").onclick = function() {
        document.getElementById("signup-modal").style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == document.getElementById("signup-modal")) {
            document.getElementById("signup-modal").style.display = "none";
        }
    };

})


