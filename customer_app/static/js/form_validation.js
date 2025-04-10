document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("support-form");

    form.addEventListener("submit", function (event) {
        let valid = true;
        let errorMessages = [];

        const name = form.querySelector("input[name='full_name']");
        const email = form.querySelector("input[name='email']");
        const category = form.querySelector("select[name='issue_category']");
        const description = form.querySelector("textarea[name='description']");

        if (!name.value.trim()) {
            valid = false;
            errorMessages.push("Full name is required.");
        }

        if (!email.value.trim()) {
            valid = false;
            errorMessages.push("Email is required.");
        } else {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email.value.trim())) {
                valid = false;
                errorMessages.push("Email format is invalid.");
            }
        }

        if (!category.value.trim()) {
            valid = false;
            errorMessages.push("Please select an issue category.");
        }

        if (!description.value.trim()) {
            valid = false;
            errorMessages.push("Description is required.");
        }

        const errorContainer = document.getElementById("form-errors");
        errorContainer.innerHTML = "";

        if (!valid) {
            event.preventDefault();
            errorMessages.forEach(msg => {
                const li = document.createElement("li");
                li.textContent = msg;
                errorContainer.appendChild(li);
            });
        }
    });
});
