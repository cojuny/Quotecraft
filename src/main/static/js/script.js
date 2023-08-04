const navBar = document.querySelector("nav"),
       menuBtns = document.querySelectorAll(".menu-icon"),
       overlay = document.querySelector(".overlay");

     menuBtns.forEach((menuBtn) => {
       menuBtn.addEventListener("click", () => {
         navBar.classList.toggle("open");
       });
     });

     overlay.addEventListener("click", () => {
       navBar.classList.remove("open");
     });

const container = document.querySelector('.quote-container');
const items = document.querySelectorAll('.quote-wrapper');

container.addEventListener('wheel', (event) => {
  event.preventDefault();
  const delta = event.deltaY;

  container.scrollBy({
    top: delta,
    behavior: 'smooth'
  });
});




const sort_latest = document.getElementById('sort_latest');
const sort_oldest = document.getElementById('sort_oldest');
const sort_random = document.getElementById('sort_random');

function updateSelectedButton(selectedBtn) {
  // Remove 'selected' class from all buttons
  sort_latest.classList.remove('selected');
  sort_oldest.classList.remove('selected');
  sort_random.classList.remove('selected');

  // Add 'selected' class to the selected button
  selectedBtn.classList.add('selected');
}

sort_latest.addEventListener('click', () => {
  updateSelectedButton(sort_latest);
  // Add your logic for handling the 'Latest' button click here
});

sort_oldest.addEventListener('click', () => {
  updateSelectedButton(sort_oldest);
  // Add your logic for handling the 'Oldest' button click here
});

sort_random.addEventListener('click', () => {
  updateSelectedButton(sort_random);
  // Add your logic for handling the 'Random' button click here
});



