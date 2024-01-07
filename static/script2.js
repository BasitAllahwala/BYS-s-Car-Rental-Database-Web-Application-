var current_table= null ;
document.addEventListener('DOMContentLoaded', function() {
    // Set the default table name (change this to your default table name)
    var defaultTableName = "Cars";

    // Call redirectToTable with the default table name
    redirectToTable(defaultTableName);

    // Attach click event listeners to all buttons with the 'table-button' class
    var buttons = document.querySelectorAll('.table-button');
    console.log(buttons);

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var tableName = button.textContent;
            redirectToTable(tableName);
        });
    });
});



function redirectToTable(tableName) {
    // Send an AJAX request to the Flask backend with the table name
    fetch("/admin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ tableName: tableName }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response from the server

        // Update the HTML table with the received data
        updateTable(data);
    })
    .catch(error => {
        console.error("Error during fetch:", error);
    });
}

function updateTable(data) {
    console.log("Received data:", data);

    if (data && data.success) {
        // Extract the nested 'data' object
        var nestedData = data.data || {};

        // Get the table element and tbody
        var table = document.getElementById("data-table");
        var tbody = table.querySelector("tbody");

        // Clear existing rows from tbody
        tbody.innerHTML = "";

        if (nestedData.column_names && nestedData.rows) {
            console.log("Updating table with data:", nestedData);

            // Add headers to the table
            var thead = table.querySelector("thead");
            thead.innerHTML = "<tr>" + nestedData.column_names.map(name => `<th>${name}</th>`).join("") + "</tr>";

            // Add rows to the table
            nestedData.rows.forEach(row => {
                tbody.innerHTML += "<tr>" + nestedData.column_names.map(name => `<td>${row[name]}</td>`).join("") + "</tr>";
            });
        } else {
            console.error("Invalid data structure received from the server:", nestedData);
        }
    } else {
        console.error("Invalid data received from the server:", data);
    }
}


document.getElementById('bt1').addEventListener('click', function () { {
    var searchColumn = document.getElementById('search-column').value;
    var searchRow = document.getElementById('search-row').value;
    
    var searchData = {
        searchColumn: searchColumn,
        searchRow: searchRow
    };

    console.log(searchData)
    
    // Make a POST request to the Flask route
    fetch("/Search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(searchData),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle the response from the server
            // You may perform additional actions based on the server's response
            // updateTable(data);
        })
        .catch(error => {
            console.error("Error during fetch:", error);
        });
}});

document.getElementById('add-button').addEventListener('click', function () {
    document.getElementById('pcontainer').style.display = 'flex';
});

document.getElementById('cpopup').addEventListener('click', function () {
    document.getElementById('pcontainer').style.display = 'none';
    document.getElementById('pcontainer1').style.display = 'none';
});

document.getElementById('okButton').addEventListener('click', function () {
    const addrow = {
        cid: document.getElementById('cid').value,
        make: document.getElementById('make').value,
        model: document.getElementById('model').value,
        year: document.getElementById('year').value,
        license_plate: document.getElementById('lplate').value,
        RentalPricePerday: document.getElementById('RPP').value,
        availability: document.getElementById('availability').value,
    };

    fetch("/add_admin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(addrow),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById('pcontainer').style.display = 'none';
    });
});

document.getElementById('cpopup1').addEventListener('click', function () {
    document.getElementById('pcontainer1').style.display = 'none';
});

function promptForCarId() {
    // Prompt the user for the car ID
    const carIdToDelete = prompt("Enter the Car ID to delete:");

    // Check if the user entered a value
    if (carIdToDelete !== null) {
        // Send the car ID to the Flask backend for deletion
        deleteCar(carIdToDelete);
    }
}

document.getElementById('Del-button').addEventListener('click', function () {
    document.getElementById('pcontainer1').style.display = 'flex';
});

document.getElementById('okButton1').addEventListener('click', function () {
    carId = document.getElementById('car_id').value
    fetch('/delete_admin', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            car_id: carId,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            alert(data.message); // Display a success message
        } else {
            alert(`Error: ${data.message}`); // Display an error message
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing your request.');
    });
});




