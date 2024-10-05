// document.addEventListener('DOMContentLoaded', function () {
//     var form = document.querySelector('.needs-validation');

//     form.addEventListener('submit', function (event) {
//         var emailField = document.getElementById('id_email');
//         var mobileField = document.getElementById('id_mobile');
//         var passwordField = document.getElementById('id_password');
//         var confirmPasswordField = document.getElementById('id_confirm_password');
        
// 		if (mobileField.value === "") {
//             mobileField.classList.add('is-invalid');
//             mobileField.nextElementSibling.innerHTML = 'Mobile must be filled out.';
//             event.preventDefault();
//         }else if (mobileField.value.length !== 10) {
// 			mobileField.classList.add('is-invalid');
// 			mobileField.nextElementSibling.innerHTML = 'Mobile number must be 10 digits.';
// 			event.preventDefault();
// 		}
		
//         if (passwordField.value === "") {
//             passwordField.classList.add('is-invalid');
//             passwordField.nextElementSibling.innerHTML = 'Password must be filled out.';
//             event.preventDefault();
//         }

// 		if (confirmPasswordField.value === "") {
//             confirmPasswordField.classList.add('is-invalid');
//             confirmPasswordField.nextElementSibling.innerHTML = 'Confirm password must be filled out.';
//             event.preventDefault();
//         }
// 		if (passwordField.value != "" & confirmPasswordField.value != "" &  passwordField.value != confirmPasswordField.value) {
//             confirmPasswordField.classList.add('is-invalid');
//             confirmPasswordField.nextElementSibling.innerHTML = "Passwords do not match.";
//             event.preventDefault();
//         }
//     });
// });