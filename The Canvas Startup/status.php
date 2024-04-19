<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portrait Commission</title>
    <style>
        /* Gradient background */
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom right, #4CAF50, #008CBA);
            font-family: Arial, sans-serif;
        }

        /* Navigation bar */
        #navigation {
            background-color: rgba(255, 255, 255, 0.8); /* Transparent white background */
            padding: 10px;
            text-align: center;
        }

        #navigation a {
            color: #333;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        #navigation a:hover {
            background-color: rgba(0, 0, 0, 0.1); /* Light grey on hover */
        }

        /* Table styling */
        table {
            width: 90%;
            margin: 20px auto;
            border-collapse: separate;
            border-spacing: 0;
            border: 3px solid rgba(0, 0, 0, 0.5); /* Darker border */
            background-color: rgba(255, 255, 255, 0.8); /* Transparent white background */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Box shadow */
            border-radius: 10px;
        }

        th, td {
            border: 1px solid rgba(0, 0, 0, 0.5); /* Darker border */
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: rgba(0, 0, 0, 0.1); /* Light grey background */
            color: #333;
            text-transform: uppercase;
        }

        /* Completed button */
        .completed-button, .delete-button {
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .completed-button {
            background-color: #4CAF50; /* Green */
            color: white;
        }

        .delete-button {
            background-color: #f44336; /* Red */
            color: white;
        }

        .completed-button:hover, .delete-button:hover {
            background-color: rgba(0, 0, 0, 0.8); /* Darken on hover */
        }
    </style>
</head>
<body>

<div id="navigation">
    <a href="client.html">Home</a>
    <a href="status.php">View Commission Status</a>
    <a href="index.php">Log Out</a>
</div>

<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "iamadam4040";
$dbname = "canvas";

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted and the completed_id is set
if (isset($_POST['completed_id'])) {
    // Get the user ID from the form
    $userId = $_POST['completed_id'];
    
    // Update the Approval column in the Status table
    $sql = "UPDATE status SET Approval='Approved' WHERE User='$userId'";
    
    if ($conn->query($sql) === TRUE) {
        echo "<div class='popup'>Commission Approved!</div>";
        echo "<script>setTimeout(function() { document.querySelector('.popup').style.display = 'none'; }, 3000);</script>";
    } else {
        echo "Error updating record: " . $conn->error;
    }
}

// Check if the form is submitted and the rejected_id is set
if (isset($_POST['rejected_id'])) {
    // Get the user ID from the form
    $userId = $_POST['rejected_id'];
    
    // Update the Approval column in the Status table
    $sql = "UPDATE status SET Approval='Rejected' WHERE User='$userId'";
    
    if ($conn->query($sql) === TRUE) {
        echo "<div class='popup'>Commission Rejected!</div>";
        echo "<script>setTimeout(function() { document.querySelector('.popup').style.display = 'none'; }, 3000);</script>";
    } else {
        echo "Error updating record: " . $conn->error;
    }
}

// Check if the form is submitted and the delete_id is set
if (isset($_POST['delete_id'])) {
    // Get the user ID from the form
    $userId = $_POST['delete_id'];
    
    // Delete the row from the Status table
    $sql = "DELETE FROM status WHERE User='$userId'";
    
    if ($conn->query($sql) === TRUE) {
        echo "<div class='popup'>Commission Deleted!</div>";
        echo "<script>setTimeout(function() { document.querySelector('.popup').style.display = 'none'; }, 3000);</script>";
    } else {
        echo "Error deleting record: " . $conn->error;
    }
}

// Fetch commissions from the database
$sql = "SELECT * FROM status";
$result = $conn->query($sql);

// Start the table
echo "<table>";
echo "<tr>";
echo "<th>User</th>";
echo "<th>Image</th>";
echo "<th>Status</th>";
echo "<th>Action</th>";
echo "</tr>";

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row['User'] . "</td>";
        // Increase the size of each row for proper image display
        echo "<td><img src='" . $row['Preview Image'] . "' alt='Commission Image' style='width: 200px; height: 200px;'></td>";
        // Display status
        echo "<td>" . $row['Status'] . "</td>";
        // Add "Approve" and ""Reject" button 
        echo "<td><form method='post'><input type='hidden' name='completed_id' value='" . $row['User'] . "'><button class='completed-button' type='submit'>Approve</button></form> 
        <form method='post'><input type='hidden' name='rejected_id' value='" . $row['User'] . "'><button class='delete-button' type='submit'>Reject</button></form></td>";

        // Add "Delete" button with red color
        echo "<td><form method='post'><input type='hidden' name='delete_id' value='" . $row['User'] . "'><button class='delete-button' type='submit'>Delete</button></form></td>";
        echo "</tr>";
    }
} else {
    echo "<tr><td colspan='6'>No commissions found</td></tr>";
}

// End the table
echo "</table>";

// Close the database connection
$conn->close();
?>
