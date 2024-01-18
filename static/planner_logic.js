var day_holder = 'None';
var price_holder = 0;
var monthly_price = 0;

function showUpperPart(element) {
    document.getElementById('upperPart').style.display = 'block';

    var dayID = element.parentNode.id;
    day_holder = dayID;

    console.log("Selected day:", day_holder);
}

//document.addEventListener('DOMContentLoaded', function () {
//    // Add an event listener to the form
//    document.getElementById('optionsForm').addEventListener('change', function (event) {
//        // Prevent the default form submission behavior
//        event.preventDefault();
//
//        // When a radio input changes, trigger the showWindow function
//        const selectedOption = this.querySelector('input[name="options"]:checked').value;
//        showWindow(selectedOption);
//    });
//});

document.addEventListener('DOMContentLoaded', function () {
    // Add an event listener to the form
    document.getElementById('optionsForm').addEventListener('change', function (event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // When a radio input changes, trigger the showWindow function
        const selectedOption = this.querySelector('input[name="options"]:checked');

        if (selectedOption !== null) {
            showWindow(selectedOption.value);
        } else {
            console.error('No option selected.');
        }
    });
});


function showWindow(option) {
    // Hide all windows
    document.querySelectorAll('.window').forEach(window => {
        window.style.display = 'none';
    });

    const selectedWindow = document.getElementById(`window${option}`);
    if (selectedWindow) {
        selectedWindow.style.display = 'block';
        console.log(`Window${option} displayed.`);
    } else {
        console.error('Window not found for option:', option);
    }
}

// event listeners for clicking the Window submit button

//document.addEventListener('DOMContentLoaded', function() {
//        // Get a reference to the "Enter" button inside the windowTPmetro div
//        const enterButton = document.querySelector('#windowTPmetro .enter-button');
//
//        // Add an event listener to the "Enter" button
//        enterButton.addEventListener('click', function() {
//            submitTPmetroform('windowTPmetro');
//        });
//    });


function submitTPmetroform() {
    // Get selected values within the specified window
    const startStation = document.getElementById('startStation_TPmetro').value;
    const endStation = document.getElementById('endStation_TPmetro').value;
    const isRoundtrip = document.getElementById('is_roundtrip_TPmetro').checked;

    // Prepare data to send to the server
    const formData = {
        startStation: startStation,
        endStation: endStation,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/TPmetro_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "北捷");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitTYmetroform() {
    // Get selected values within the specified window
    const startStation = document.getElementById('startStation_TYmetro').value;
    const endStation = document.getElementById('endStation_TYmetro').value;
    const isRoundtrip = document.getElementById('is_roundtrip_TYmetro').checked;

    // Prepare data to send to the server
    const formData = {
        startStation: startStation,
        endStation: endStation,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/TYmetro_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "機捷");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitDHtramform() {
    // Get selected values within the specified window
    const startStation = document.getElementById('startStation_DHtram').value;
    const endStation = document.getElementById('endStation_DHtram').value;
    const isRoundtrip = document.getElementById('is_roundtrip_DHtram').checked;

    // Prepare data to send to the server
    const formData = {
        startStation: startStation,
        endStation: endStation,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/DHtram_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "淡海輕軌");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitAKtramform() {
    // Get selected values within the specified window
    const startStation = document.getElementById('startStation_AKtram').value;
    const endStation = document.getElementById('endStation_AKtram').value;
    const isRoundtrip = document.getElementById('is_roundtrip_AKtram').checked;

    // Prepare data to send to the server
    const formData = {
        startStation: startStation,
        endStation: endStation,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/AKtram_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "安坑輕軌");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitTrainform() {
    // Get selected values within the specified window
    const startStation = document.getElementById('startStation_Train').value;
    const endStation = document.getElementById('endStation_Train').value;
    const isRoundtrip = document.getElementById('is_roundtrip_Train').checked;

    // Prepare data to send to the server
    const formData = {
        startStation: startStation,
        endStation: endStation,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/Train_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "台鐵");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitTTbusform() {
    // Get selected values within the specified window
    const guest_Type = document.getElementById('TTbus_guest_type').value;
    const sections = document.getElementById('TTbus_sections').value;
    const isRoundtrip = document.getElementById('is_roundtrip_TTbus').checked;

    // Prepare data to send to the server
    const formData = {
        guest_Type: guest_Type,
        sections: sections,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/TT_bus_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "台北新北公車");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitKeelungbusform() {
    // Get selected values within the specified window
    const guest_Type = document.getElementById('Keelungbus_guest_type').value;
    const sections = document.getElementById('Keelungbus_sections').value;
    const keelung_night_mode = document.getElementById('keelung_night_mode').checked;
    const isRoundtrip = document.getElementById('is_roundtrip_Keelungbus').checked;


    // Prepare data to send to the server
    const formData = {
        guest_Type: guest_Type,
        sections: sections,
        keelung_night_mode: keelung_night_mode,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/Keelung_bus_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "基隆公車");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitTYbusform() {
    // Get selected values within the specified window
    const guest_Type = document.getElementById('TYbus_guest_type').value;
    const TYbus_single_trip_cost = document.getElementById('TYbus_single_trip_cost').value;
    const isRoundtrip = document.getElementById('is_roundtrip_TYbus').checked;
    const is_TY_citizen = document.getElementById('is_TY_citizen').checked;

    // Prepare data to send to the server
    const formData = {
        guest_Type: guest_Type,
        TYbus_single_trip_cost: TYbus_single_trip_cost,
        isRoundtrip: isRoundtrip,
        is_TY_citizen: is_TY_citizen,
    };

    // Send data to the Flask route using fetch
    fetch('/TY_bus_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "桃園公車");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function submitLongbusform() {
    // Get selected values within the specified window
    const LongBus_single_trip_cost = document.getElementById('LongBus_single_trip_cost').value;
    const isRoundtrip = document.getElementById('is_roundtrip_LongBus').checked;

    // Prepare data to send to the server
    const formData = {
        LongBus_single_trip_cost: LongBus_single_trip_cost,
        isRoundtrip: isRoundtrip,
    };

    // Send data to the Flask route using fetch
    fetch('/Long_Bus_calculation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        mode: 'cors',
    })
    .then(response => response.json())
    .then(result => {
        // Print the result in the according day's square
        printResult(result, "客運");
    })
    .catch(error => {
        // Log detailed error information
        console.error('Error during fetch:', error);
        // Optionally, you can add more specific error handling here
    });
}

function printResult(result, transport) {

    monthly_price = monthly_price + result.price;
    console.log("Monthly price:", monthly_price);

    const total_sum = document.getElementById("total_sum");
    total_sum.innerHTML = `單月費用總和: ${monthly_price * 4}`;


    if (result && transport) {
        var userBlock = document.createElement("p");
        userBlock.className = "user-block";

        var deleteBtn = document.createElement("span");
        deleteBtn.className = "delete-btn";
        deleteBtn.innerHTML = "&#10006;"; // Cross symbol
        deleteBtn.onclick = function() {
            userBlock.remove();
            monthly_price = monthly_price - result.price;
            const total_sum = document.getElementById("total_sum");
            total_sum.innerHTML = `單月費用總和: ${monthly_price * 4}`;
        };

        userBlock.innerHTML = `${transport}<br>${result.price}`;
        userBlock.appendChild(deleteBtn);

        var container = document.getElementById("userBlocksContainer_" + day_holder);

        // Checking if the container element exists before appending
        if (container) {
            // Appending userBlock to the container element
            container.appendChild(userBlock);
        } else {
            console.error("Container element not found");
        }

        // Clearing input fields after adding userBlock
        document.getElementById("nameInput").value = "";
        document.getElementById("ageInput").value = "";
    }
}

// for Taoyuan bus price limit only
function validateForm() {
    var inputElement = document.getElementById("LongBus_single_trip_cost");
    var inputValue = parseFloat(inputElement.value);

    if (isNaN(inputValue) || inputValue > 60) {
      alert("Please enter a valid number up to 60.");
      return false; // Prevent form submission
    }

    return true; // Allow form submission
  }
