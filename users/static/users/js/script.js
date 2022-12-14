//let menu = document.querySelector('#menu-icon');
//let navbar = document.querySelector('.navbar');

//menu.onclick = () => {menu.classList.toggle('bx-x'); navbar.classList.toggle('open');}

/*codingmaker_*/
let container = document.querySelector(".container");
let toggleBtn = document.querySelector('.toggle-btn');

dycalendar.draw({
   target:'#dycalendar', 
   dayformat: 'full', 
   type: 'month', 
   monthformat: 'full', 
   highlighttoday: true, 
   prevnextbutton: 'show'
});  

toggleBtn.onclick = () =>{
 container.classList.toggle('dark');
 document.body.classList.toggle('background-dark');
};
