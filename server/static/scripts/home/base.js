tailwind.config = {};
function toggleMindStudio() {
  var container = document.getElementById("mindstudioContainer");
  container.classList.toggle("hidden");
}
// Event listener for button click to toggle MindStudio AI frame
document
  .getElementById("openMindStudio")
  .addEventListener("click", function () {
    toggleMindStudio();
  });
