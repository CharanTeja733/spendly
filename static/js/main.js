// main.js — students will add JavaScript here as features are built

// Auto-dismiss flash toast notifications after 4 seconds
document.addEventListener("DOMContentLoaded", function () {
    var toasts = document.querySelectorAll(".flash-message");
    toasts.forEach(function (toast) {
        // Click to dismiss immediately
        toast.addEventListener("click", function () {
            dismissToast(toast);
        });

        // Auto-dismiss after 4 seconds
        setTimeout(function () {
            dismissToast(toast);
        }, 4000);
    });
});

function dismissToast(toast) {
    if (toast.classList.contains("is-dismissing")) return;
    toast.classList.add("is-dismissing");
    // Remove from DOM after animation completes
    toast.addEventListener("animationend", function () {
        if (toast.parentNode) {
            toast.remove();
            // Remove the container if empty
            var container = document.querySelector(".flash-messages");
            if (container && container.children.length === 0) {
                container.remove();
            }
        }
    });
}
