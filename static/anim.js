var loginBtn = document.getElementById('loginBtn');
var signupBtn = document.getElementById('signupBtn');
var loginPopup = document.querySelector(".popup");
var signupPopup = document.querySelector(".popup1");
var signInButton = loginPopup.querySelector("button");
var createAccountButton = signupPopup.querySelector("button");

var activeButton = null;

loginBtn.addEventListener('click', function() {
    if (activeButton !== signupBtn) {
        openPopup(loginPopup);
        activeButton = loginBtn;
    }
});

signupBtn.addEventListener('click', function() {
    if (activeButton !== loginBtn) {
        openPopup(signupPopup);
        activeButton = signupBtn;
    }
});

function openPopup(popup) {
    popup.classList.add("active");
}

document.querySelector(".popup .close-btn").addEventListener("click", function() {
    closePopup(loginPopup);
});

document.querySelector(".popup1 .close-btn").addEventListener("click", function() {
    closePopup(signupPopup);
});

function closePopup(popup) {
    popup.classList.remove("active");
    activeButton = null;
}

signInButton.addEventListener("click", function () {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    //var rememberMe = document.getElementById("remember-me").checked;

    // Now you can use the email, password, and rememberMe values
    console.log("Email:", email);
    console.log("Password:", password);
    //console.log("Remember Me:", rememberMe);

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email: email,
            password: password,
            //rememberMe: rememberMe,
        }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle the response from the server
            if (data.success) {
                if (data.message === "Admin LoggedIn"){
                    window.location.href = "/admin";
                    console.log("Admin IN");
                }
                // Successful login, you may want to redirect or perform other actions
                showSuccessModal1();
                // window.location.href = '/cars';
                console.log("Login successful!");
                
            } else {
                // Handle failed login, display an error message, etc.
                console.log("Login failed:", data.message);
            }
        })
        .catch(error => {
            console.error("Error during fetch:", error);
        });
});

createAccountButton.addEventListener("click", function () {
    var name = document.getElementById("Name").value;
    var email = document.getElementById("email1").value;
    var password = document.getElementById("password1").value;
    var rememberMe = document.getElementById("remember-me").checked;

    // Now you can use the name, email, password, and rememberMe values
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Remember Me:", rememberMe);

    // Add code to send the signup data to your backend (Flask)
    // Example: make an AJAX request to the Flask endpoint
    // Modify the URL and method based on your backend structure
    fetch("/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: name,
            email: email,
            password: password,
            rememberMe: rememberMe,
        }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            showSuccessModal();
            // Handle the response from the server
        })
        .catch(error => {
            console.error("Error:", error);
        });
});

function showSuccessModal() {
    var successModal = document.getElementById('successModal');
    successModal.style.display = 'block';
}

function closeSuccessModal() {
    var successModal = document.getElementById('successModal');
    successModal.style.display = 'none';
    closePopup(signupPopup);
}

function showSuccessModal1() {
    var successModal1 = document.getElementById('successModal1');
    successModal1.style.display = 'block';
}

function closeSuccessModal1() {
    var successModal1 = document.getElementById('successModal1');
    successModal1.style.display = 'none';
    closePopup(loginPopup);
}

