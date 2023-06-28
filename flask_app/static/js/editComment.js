document.addEventListener("DOMContentLoaded", (event) => {
  // handle click on any edit button
  document.querySelectorAll(".edit-button").forEach((editButton) => {
    editButton.addEventListener("click", (event) => {
      event.preventDefault();
      // get the comment id from the data attribute
      const commentId = event.target.dataset.commentId;
      // find the corresponding form and show it
      const form = document.querySelector(
        `.comment-update-form[data-comment-id="${commentId}"]`
      );
      form.classList.remove("hidden");
    });
  });

  // handle form submission
  document.querySelectorAll(".comment-update-form").forEach((form) => {
    form.addEventListener("submit", () => {
      // hide the form again after submission
      form.classList.add("hidden");
    });
  });

  // handle click on any cancel button
  document.querySelectorAll(".cancel-button").forEach((cancelButton) => {
    cancelButton.addEventListener("click", (event) => {
      event.preventDefault();
      console.log("Cancel button clicked");
      // get the comment id from the data attribute
      const commentId = event.target.dataset.commentId;
      console.log(`commentId is ${commentId}`);
      // find the corresponding form and hide it
      const form = document.querySelector(
        `.comment-update-form[data-comment-id="${commentId}"]`
      );
      console.log(form);
      form.classList.add("hidden");
    });
  });
});
