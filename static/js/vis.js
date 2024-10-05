
const body = document.querySelector("body"),
      nav = document.querySelector("nav"),
      modeToggle = document.querySelector(".dark-light"),
      searchToggle = document.querySelector(".searchToggle"),
      sidebarOpen = document.querySelector(".sidebarOpen"),
      siderbarClose = document.querySelector(".siderbarClose");

      let getMode = localStorage.getItem("mode");
          if(getMode && getMode === "dark-mode"){
            body.classList.add("dark");
          }

// js code to toggle dark and light mode
      modeToggle.addEventListener("click" , () =>{
        modeToggle.classList.toggle("active");
        body.classList.toggle("dark");

        // js code to keep user selected mode even page refresh or file reopen
        if(!body.classList.contains("dark")){
            localStorage.setItem("mode" , "light-mode");
        }else{
            localStorage.setItem("mode" , "dark-mode");
        }
      });

// js code to toggle search box
        searchToggle.addEventListener("click" , () =>{
        searchToggle.classList.toggle("active");
      });
 
      
//   js code to toggle sidebar
sidebarOpen.addEventListener("click" , () =>{
    nav.classList.add("active");
});

body.addEventListener("click" , e =>{
    let clickedElm = e.target;

    if(!clickedElm.classList.contains("sidebarOpen") && !clickedElm.classList.contains("menu")){
        nav.classList.remove("active");
    }
});


let lastScrollTop = 0;
const navbar = document.getElementById('nav');
const header = document.getElementsByClassName('.header');
const headerHeight = header.offsetHeight;

window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 600) {
        if (scrollTop > lastScrollTop) {
            // Scroll down
            navbar.style.top = '-70px'; // Adjust value to hide navbar
        } else {
            // Scroll up
            navbar.style.top = '0';
        }
    } else {
        navbar.style.top = '0';
    }

    lastScrollTop = scrollTop;
});

window.addEventListener('scroll', function() {
    const header = document.querySelector('.header');
    let scrollPosition = window.pageYOffset;
    header.style.backgroundPositionX = -scrollPosition * 0.5 + 'px';
});



document.addEventListener("DOMContentLoaded", function() {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const imageContainer = document.querySelector('.images-container');
    observer.observe(imageContainer);
});

document.addEventListener("DOMContentLoaded", function() {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const imageContainer = document.querySelector('#cartn');
    observer.observe(imageContainer);
});



window.addEventListener('scroll', function() {
    const parallax = document.querySelector('.parallax');
    let scrollPosition = window.pageYOffset;
    parallax.style.backgroundPositionY = scrollPosition * 0.5 + 'px';
});



window.addEventListener('scroll', function() {
    const contents = document.querySelector('.contents');
    let scrollPosition = window.pageYOffset;
    contents.style.backgroundPositionX = scrollPosition * 0.4 + 'px';
});


