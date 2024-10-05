document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    var errorMessagesContainer = document.getElementById('error-messages');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default submission

        // Clear previous error messages
        errorMessagesContainer.innerHTML = '';
        errorMessagesContainer.style.display = 'none';
        var invalidFields = document.querySelectorAll(".is-invalid");
        invalidFields.forEach(function (field) {
            field.classList.remove("is-invalid");
        });

        var isValid = true;
        var firstInvalidField = null; // Track the first invalid field

        // Validation logic
        const validationMessages = {
            firstName: "Please enter your first name",
            lastName: "Please enter your last name",
            dob: "Please enter your date of birth",
            address: "Please enter your address",
            city: "Please enter your city",
            state: "Please select your state",
            country: "Please select your country",
            postalCode: {
                empty: "Please enter your postal code",
                invalid: "Postal code must be exactly 6 digits"
            },
            bio: "Please limit your input to fewer than 500 characters."
        };

        var firstNameField = document.getElementById("id_first_name");
        if (!firstNameField.value) {
            isValid = showError(firstNameField, validationMessages.firstName);
            if (!firstInvalidField) firstInvalidField = firstNameField; // Set first invalid field
        }

        var lastNameField = document.getElementById("id_last_name");
        if (!lastNameField.value) {
            isValid = showError(lastNameField, validationMessages.lastName);
            if (!firstInvalidField) firstInvalidField = lastNameField;
        }

        var dobField = document.getElementById("id_date_of_birth");
        if (!dobField.value) {
            isValid = showError(dobField, validationMessages.dob);
            if (!firstInvalidField) firstInvalidField = dobField;
        }

        var addressField1 = document.getElementById("id_address_line_1");
        if (!addressField1.value) {
            isValid = showError(addressField1, validationMessages.address);
            if (!firstInvalidField) firstInvalidField = addressField1;
        }

        var cityField = document.getElementById("id_city");
        if (!cityField.value) {
            isValid = showError(cityField, validationMessages.city);
            if (!firstInvalidField) firstInvalidField = cityField;
        }

        var stateField = document.getElementById("id_state");
        if (stateField.value === "") {
            isValid = showError(stateField, validationMessages.state);
            if (!firstInvalidField) firstInvalidField = stateField;
        }

        var countryField = document.getElementById("id_country");
        if (countryField.value === "") {
            isValid = showError(countryField, validationMessages.country);
            if (!firstInvalidField) firstInvalidField = countryField;
        }

        var postalCodeField = document.getElementById("id_postal_code");
        if (!postalCodeField.value) {
            isValid = showError(postalCodeField, validationMessages.postalCode.empty);
            if (!firstInvalidField) firstInvalidField = postalCodeField;
        } else if (!/^\d{6}$/.test(postalCodeField.value)) {
            isValid = showError(postalCodeField, validationMessages.postalCode.invalid);
            if (!firstInvalidField) firstInvalidField = postalCodeField;
        }

        var bioField = document.getElementById("id_bio");
        if (bioField.value.length > 500) {
            isValid = showError(bioField, validationMessages.bio);
            if (!firstInvalidField) firstInvalidField = bioField;
        }

        // If the form is valid, submit the form
        if (isValid) {
            form.submit();
        } else {
            // Scroll to the first invalid field or error messages
            if (firstInvalidField) {
                firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else {
                errorMessagesContainer.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });

    // take error field to screen
    function showError(field, message) {
        field.classList.add("is-invalid");
        var errorMessage = document.createElement('div');
        errorMessage.classList.add("invalid-feedback");
        errorMessage.innerText = message;
        field.insertAdjacentElement('afterend', errorMessage);
        errorMessagesContainer.innerHTML += `<p>${message}</p>`;
        return false; // Form is invalid
    }
});