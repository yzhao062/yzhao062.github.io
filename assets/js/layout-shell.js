// Shared layout loader for navbar, sidebar, and footer includes.
(function () {
    function loadInclude(targetId, url, onLoaded) {
        var target = document.getElementById(targetId);
        if (!target) return;

        fetch(url)
            .then(function (response) {
                if (!response.ok) {
                    throw new Error("Failed to load " + url);
                }
                return response.text();
            })
            .then(function (content) {
                target.innerHTML = content;
                if (typeof onLoaded === "function") {
                    onLoaded(target);
                }
            })
            .catch(function (error) {
                console.error(error);
            });
    }

    document.addEventListener("DOMContentLoaded", function () {
        loadInclude("navbar", "includes/navbar.html");
        loadInclude("sidebar", "includes/sidebar.html", function (sidebar) {
            var emailUser = "yue.z";
            var emailHost = "usc.edu";
            var emailElement = sidebar.querySelector("#email-placeholder");
            if (emailElement) {
                emailElement.innerHTML =
                    '<a href="mailto:' +
                    emailUser +
                    "@" +
                    emailHost +
                    '">' +
                    emailUser +
                    "@" +
                    emailHost +
                    "</a>";
            }
        });
        loadInclude("myFooter", "includes/footer.html");
    });
})();
