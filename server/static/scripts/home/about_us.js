document.addEventListener("DOMContentLoaded", function () {
  // Add animations and interactions here
  const teamMembers = document.querySelectorAll(".team-member");

  // Add hover effect to team member cards
  teamMembers.forEach((member) => {
    member.addEventListener("mouseenter", function () {
      this.classList.add("hovered");
    });
    member.addEventListener("mouseleave", function () {
      this.classList.remove("hovered");
    });
  });
});
