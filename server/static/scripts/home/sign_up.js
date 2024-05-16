// JavaScript code for toggle functionality and form handling

document.addEventListener("DOMContentLoaded", function () {
  const volunteerToggle = document.getElementById("volunteerToggle");
  const organizationToggle = document.getElementById("organizationToggle");
  const volunteerForm = document.getElementById("volunteerForm");
  const organizationForm = document.getElementById("organizationForm");

  // Function to show volunteer form and hide organization form
  volunteerToggle.addEventListener("click", function () {
    volunteerForm.classList.remove("hidden");
    organizationForm.classList.add("hidden");
  });

  // Function to show organization form and hide volunteer form
  organizationToggle.addEventListener("click", function () {
    organizationForm.classList.remove("hidden");
    volunteerForm.classList.add("hidden");
  });
});
