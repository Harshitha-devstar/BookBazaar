document.addEventListener("DOMContentLoaded", function () {
    const profileIcon = document.getElementById("profile-icon");
    const sidebar = document.getElementById("profile-sidebar");
    const closeSidebar = document.getElementById("close-sidebar");

    // Open sidebar when profile icon is clicked
    profileIcon.addEventListener("click", function () {
        sidebar.style.right = "0";
    });

    // Close sidebar when close button is clicked
    closeSidebar.addEventListener("click", function () {
        sidebar.style.right = "-300px";
    });

    // Optional: Close sidebar when clicking outside
    document.addEventListener("click", function (event) {
        if (!sidebar.contains(event.target) && !profileIcon.contains(event.target)) {
            sidebar.style.right = "-300px";
        }
    });
});
