console.log("modal.js loaded");

// Define all modals and buttons
const modals = {
  name: {
    modal: document.getElementById("modal-name"),
    btn: document.getElementById("modal-name-btn"),
    closeBtn: document.getElementById("modal-name-close"),
  },
  ingredients: {
    modal: document.getElementById("modal-ingredients"),
    btn: document.getElementById("modal-ingredient-btn"),
    closeBtn: document.getElementById("modal-ingredients-close"),
  },
  directions: {
    modal: document.getElementById("modal-directions"),
    btn: document.getElementById("modal-instructions-btn"),
    closeBtn: document.getElementById("modal-directions-close"),
  },
  description: {
    modal: document.getElementById("modal-description"),
    btn: document.getElementById("modal-description-btn"),
    closeBtn: document.getElementById("modal-description-close"),
  },
  login: {
    modal: document.getElementById("modal-login"),
    btn: document.getElementById("modal-login-btn"),
    closeBtn: document.getElementById("modal-login-close"),
  },
};

// Define function to open modal
function openModal(modal) {
  modal.style.display = "block";
}

// Define function to close modal
function closeModal(modal) {
  modal.style.display = "none";
}

// Apply functions to each modal and its buttons
for (const key in modals) {
  if (modals.hasOwnProperty(key)) {
    const element = modals[key];

    element.btn.onclick = function () {
      openModal(element.modal);
    };

    element.closeBtn.onclick = function () {
      closeModal(element.modal);
    };

    window.onclick = function (event) {
      if (event.target == element.modal) {
        closeModal(element.modal);
      }
    };
  }
}
