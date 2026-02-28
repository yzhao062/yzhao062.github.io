// Shared Web-Stat loader to avoid duplicating inline tracker code across pages.
(function () {
    var accountId = 1866123;
    var styleId = 5;
    var scriptUrl = "https://app.ardalio.com/wts7.js";
    var spanId = "wts" + accountId;

    if (window.__fortisWebStatInitialized) {
        return;
    }
    window.__fortisWebStatInitialized = true;

    if (!document.getElementById(spanId)) {
        var span = document.createElement("span");
        span.id = spanId;
        if (document.currentScript && document.currentScript.parentNode) {
            document.currentScript.parentNode.insertBefore(span, document.currentScript);
        } else if (document.body) {
            document.body.appendChild(span);
        }
    }

    function initTracker() {
        if (typeof window.wtsl7 === "function") {
            window.wtsl7(accountId, styleId);
        }
    }

    var existing = Array.prototype.find.call(document.scripts, function (s) {
        return s.src === scriptUrl;
    });

    if (existing) {
        if (existing.getAttribute("data-loaded") === "1") {
            initTracker();
        } else {
            existing.addEventListener("load", initTracker, { once: true });
        }
        return;
    }

    var wts = document.createElement("script");
    wts.async = true;
    wts.src = scriptUrl;
    wts.addEventListener("load", function () {
        wts.setAttribute("data-loaded", "1");
        initTracker();
    }, { once: true });
    document.head.appendChild(wts);
})();
