// Automatically highlight the current page

document.addEventListener("DOMContentLoaded", function() {

    var currentPage = window.location.pathname
        .split("/")
        .pop()
        .toLowerCase();

    if (currentPage === "" || currentPage === "/") {
        currentPage = "index.html";
    }

    var sidebarLinks = document.querySelectorAll(".sidebar ul li a");

    sidebarLinks.forEach(function(link) {

        var href = link.getAttribute("href");

        if (!href) {
            return;
        }

        var linkPage = href
            .split("/")
            .pop()
            .split("#")[0]
            .toLowerCase();

        link.classList.remove("active");

        if (linkPage === currentPage) {
            link.classList.add("active");
        }

    });

});