
let products={
    data:[
        {
        CarName: "Toyota Camry",
        Model : 2022,
        Price : "45",
        image: "/static/toyota-camry-2022.png"
    },
    {
        CarName: "Honda Civic",
        Model : 2021,
        Price : "40",
        image: "/static/honda-civic-2021.png"
    },
    {
        CarName: "Ford Escape",
        Model : 2022,
        Price : "50",
        image: "/static/ford-escape-2022.png"
    },
    {
        CarName: "Chevrolet Malibu",
        Model : 2020,
        Price : "45",
        image: "/static/2020-Chevy-Malibu-MLP-Hero.png"
    },
    {
        CarName: "Nissan Altima",
        Model : 2021,
        Price : "42",
        image: "/static/2021-Nissan-Altima-hero.png"
    },
    {
        CarName: "Hyndai Elantra",
        Model : 2022,
        Price : "38",
        image: "/static/hyundai-elantra.png"
    },
    {
        CarName: "Kia Optima",
        Model : 2020,
        Price : "46",
        image: "/static/2020-Kia-Optima-MLP-Hero.png"
    },
    {
        CarName: "Subaru Legacy",
        Model : 2021,
        Price : "48",
        image: "/static/2021SUC010031_1280_01.png"
    },
    {
        CarName: "Volkswagen Jetta",
        Model : 2022,
        Price : "44",
        image: "/static/mlp-img-top-2022-jetta-temp.png"
    },

    {
        CarName: "Mazda Mazda6",
        Model : 2019,
        Price : "47",
        image: "/static/model1.png"
    },
    {
        CarName: "Lamborghini Revuolto",
        Model : 2023,
        Price : "999",
        image: "/static/1686315054737.png"
    }
]
};

let selectedCarIndex = null;
let availability = null;

// function anotherFunction(index) {
//     //console.log("Selected Car Index in Another Function:", index);
//     cindex=index;
//     return cindex;
// }

for (let index = 0; index < products.data.length; index++) {
    let i = products.data[index];
    let card = document.createElement("button");
    card.classList.add("card", i.Model, "hide");

    // Generating ID like "car1", "car2", "car3", ...
    card.id = `car${index + 1}`;

    let imgContainer = document.createElement("div");
    imgContainer.classList.add("image-container");
    let image = document.createElement("img");
    image.setAttribute("src", i.image);
    imgContainer.appendChild(image);
    card.appendChild(imgContainer);

    let container = document.createElement("div");
    container.classList.add("container");
    let name = document.createElement("h5");
    name.classList.add("car-name");
    name.innerText = i.CarName.toUpperCase();
    container.appendChild(name);

    let price = document.createElement("h6");
    price.innerText = "$" + i.Price;
    container.appendChild(price);

    card.appendChild(container);

    card.addEventListener('click', function() {
        // When a card is clicked, find the index of the clicked card
        selectedCarIndex = index;
        console.log(selectedCarIndex);
        // Call the function and pass the selectedCarIndex value
        // anotherFunction(selectedCarIndex);
    });

    document.getElementById("Cars").appendChild(card);
}


// each car (only for car 1)
document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car1'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car2'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car3'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car4'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car5'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car6'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car7'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car8'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car9'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car10'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const car1 = document.getElementById('car11'); // Get the card with ID "car1"
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popupContainer = document.getElementById('popup-container');
    const bookingForm = document.getElementById('bookingForm');

    car1.addEventListener('click', function () {
        // Open the popup when the card with ID "car1" is clicked
        popupContainer.style.display = 'flex';
    });

    closePopupBtn.addEventListener('click', function () {
        // Close the popup
        popupContainer.style.display = 'none';
    });

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Handle form submission logic here (e.g., send data to server)
        //alert('Booking submitted!'); // You can replace this with your actual form submission logic
        // Close the popup after submission
        popupContainer.style.display = 'none';
    });
});


// document.getElementById('bookingForm').addEventListener('submit', function(event) {
//     event.preventDefault();

//     // Get the values from the popup form
//     const name = document.getElementById('name').value;
//     const address = document.getElementById('address').value;
//     const location = document.getElementById('location').value;
//     const phone = document.getElementById('phone').value;
//     const bookingDate = document.getElementById('bookingDate').value;
//     const returnDate = document.getElementById('returnDate').value;

//     const selectedCar = products.data[selectedCarIndex];
//     console.log(selectedCarIndex)
//     const carName = selectedCar.CarName;
//     const carYear = selectedCar.Model;
//     const carPrice = selectedCar.Price;

//     // Do something with the gathered information (e.g., submit to server, process, etc.)

//     // Close the popup
//     document.getElementById('popup-container').style.display = 'none';

//     // Clear the form fields for the next use
//     document.getElementById('name').value = '';
//     document.getElementById('address').value = '';
//     document.getElementById('location').value = '';
//     document.getElementById('phone').value = '';
//     document.getElementById('bookingDate').value = '';
//     document.getElementById('returnDate').value = '';
// });

// // Add an event listener to close the popup when the close button is clicked
// document.getElementById('closePopupBtn').addEventListener('click', function() {
//     document.getElementById('popup-container').style.display = 'none';
// });



function filterCar(value){
    let buttons = document.querySelectorAll(".button-value");
    buttons.forEach((button) => {
        if(value.toUpperCase()== button.innerText.toUpperCase()){
            button.classList.add("active1");
        }else {
            button.classList.remove("active1");
        }
    });

    let elements = document.querySelectorAll(".card");
    elements.forEach((element)=>{
        if(value == 'all'){
            element.classList.remove("hide");
        }
        else {
            if(element.classList.contains(value)){
                element.classList.remove("hide");
            }
            else{
                element.classList.add("hide");
            }
        }
    });
}

document.getElementById("search").addEventListener("click",() => {
    let searchInput = document.getElementById("search-input").value;
    let elements = document.querySelectorAll(".car-name");
    let cards = document.querySelectorAll(".card");

    elements.forEach((element, index) => {
        if(element.innerText.includes(searchInput.toUpperCase())){
            cards[index].classList.remove("hide");
        }
        else{
            cards[index].classList.add("hide");
        }
    });
})

document.addEventListener('DOMContentLoaded', function () {
    const priceRangeInput = document.getElementById('price-range');
    const selectedPriceElement = document.getElementById('selected-price');

    priceRangeInput.addEventListener('input', () => {
    const selectedPrice = priceRangeInput.value;
    selectedPriceElement.textContent = `Selected Price: $${selectedPrice}`;
    });
});

// document.addEventListener('DOMContentLoaded', function () {
//     const myButton = document.querySelectorAll(".card");

//     myButton.addEventListener('click', function () {
//       // Access the value or content of the clicked element
//     const buttonValue = myButton.innerText;
//     console.log('Button clicked! Value:', buttonValue);
//     });
// });

// let startDateInput = document.getElementById("bookingDate");
// let endDateInput = document.getElementById("returnDate");
// let placeholder = document.getElementById("payment");
// startDateInput.addEventListener("input", updateDateDifference);
// endDateInput.addEventListener("input", updateDateDifference);

document.getElementById('bt2').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const formData = {
        name: document.getElementById('name').value,
        address: document.getElementById('address').value,
        location: document.getElementById('location').value,
        location_address:document.getElementById('location-address').value,
        phone: document.getElementById('phone').value,
        bookingDate: document.getElementById('bookingDate').value,
        returnDate: document.getElementById('returnDate').value,
        Payment: document.getElementById('payment').value,
        PaymentMethod: document.getElementById('paymentmethod').value
    };

    // var bookingDate = new Date(document.getElementById('bookingDate').value);
    // var returnDate = new Date(document.getElementById('returnDate').value);
    console.log(selectedCarIndex);
    console.log(formData.bookingDate);

    // function updateDateDifference() {
    //     let startDate = new Date(startDateInput.value);
    //     let endDate = new Date(endDateInput.value);

    //     // Calculate the difference in days
    //     let timeDifference = endDate - startDate;
    //     let daysDifference = timeDifference / (1000 * 60 * 60 * 24);
    //     let integerResult = Math.floor(daysDifference);
    //     let pricereq = selectedCar.Price * integerResult;
    //     placeholder.placeholder = pricereq;
    // }

    // // var timeDifference = returnDate - bookingDate;
    // // var daysDifference = timeDifference / (1000 * 60 * 60 * 24);
    // // var integerResult = Math.floor(daysDifference);
    // console.log(integerResult); 
    const selectedCar = products.data[selectedCarIndex];
    console.log("Selected Car:", selectedCar);
    // 
    

    if (selectedCar) {
        const carName = selectedCar.CarName;
        const carYear = selectedCar.Model;
        const carPrice = selectedCar.Price;

        console.log(carName, carYear, carPrice);

        formData.carName = carName;
        formData.carYear = carYear;
        formData.carPrice = carPrice;
        formData.CarID = selectedCarIndex + 1;

        // Make a POST request to the Flask route
        fetch("/cars", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
            .then(response => response.json())
            .then(data => {
                showSuccessModal2();
                if (data.hasOwnProperty('availability')) {
                    let availability = data.availability;
                    console.log(`Availability: ${availability}`);

            if (availability > 0) {
                availability--;
                console.log(availability)
            }
                } else {
                    console.error("Availability data not found in the response.");
                }
            })
            .catch(error => {
                console.error("Error during fetch:", error);
            });
            fetch("/update", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    carID: formData.CarID,
                    availability: availability,
                }),
            })
                .then(response => response.json())
                .then(data => {
                    if (availability === 0) {
                        const cardElement = document.getElementById(`car${selectedCarIndex}`);
                        cardElement.innerHTML += '<span class="out-of-stock">Out of Stock</span>';
                    }
                    // Other actions after updating availability
                })
                .catch(error => {
                    console.error("Error updating availability:", error);
                });    
    } else {
        console.error("Selected car is undefined.");
        console.log(products.data);
        console.log("Selected Car:", selectedCar);
    }
    
});




function showSuccessModal2() {
    var successModal2 = document.getElementById('successModal2');
    successModal2.style.display = 'block';
}

function closeSuccessModal2() {
    var successModal2 = document.getElementById('successModal2');
    successModal2.style.display = 'none';
    // closePopup(loginPopup);
}

window.onload = () => {
    filterProduct('all');
}