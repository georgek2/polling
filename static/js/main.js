
// Grab the HTML elements

const hamburger = document.getElementById('hamburger');
const nav = document.getElementById('navigation')


hamburger.addEventListener('click', menu);


function menu(){
    hamburger.classList.toggle('active');
    nav.classList.toggle('active');
};







