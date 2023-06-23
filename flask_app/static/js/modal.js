console.log("modal.js loaded");
const modal = document.getElementById("modal-name");
const modalBtn = document.getElementById("modal-name-btn");
const closeBtn = document.getElementById("modal-name-close");

// open/display the modal
modalBtn.onclick = function () {
  modal.style.display = "block";
};

// close the modal
closeBtn.onclick = function () {
  modal.style.display = "none";
};

// close the modal if user clicks outside of it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
