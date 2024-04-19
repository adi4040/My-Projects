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

// Check if delete button is clicked
if (isset($_POST['delete_id'])) {
    $delete_id = $_POST['delete_id'];
    // Delete the row from the database
    $sql_delete = "DELETE FROM artist WHERE user = '$delete_id'";
    if ($conn->query($sql_delete) === TRUE) {
        echo "Record deleted successfully";
        // Refresh the page after deletion
        echo "<meta http-equiv='refresh' content='0'>";
    } else {
        echo "Error deleting record: " . $conn->error;
    }
}

// Fetch commissions from the artist table
$sql_artist = "SELECT * FROM artist";
$result_artist = $conn->query($sql_artist);

// Fetch approval status from the status table and store it in an associative array
$statusData = [];
$sql_status = "SELECT User, Approval FROM status";
$result_status = $conn->query($sql_status);
if ($result_status->num_rows > 0) {
    while ($row = $result_status->fetch_assoc()) {
        $statusData[$row['User']] = $row['Approval'];
    }
}

// Display commissions
if ($result_artist->num_rows > 0) {
    while ($row_artist = $result_artist->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row_artist['portrait_type'] . "</td>";
        echo "<td>" . $row_artist['user'] . "</td>";
        echo "<td>" . $row_artist['number'] . "</td>";
        echo "<td><img src='" . $row_artist['image'] . "' alt='Commission Image' style='width: 200px; height: 200px;'></td>";
        
        // Display the approval status if available
        echo "<td>";
        if (isset($statusData[$row_artist['user']])) {
            echo $statusData[$row_artist['user']];
        } else {
            echo "Not Approved";
        }
        echo "</td>";
        
        // Add "Delete" button with red color
        echo "<td><form method='post'><input type='hidden' name='delete_id' value='" . $row_artist['user'] . "'><button type='submit' style='background-color: red; color: white;'>Delete</button></form></td>";
        echo "</tr>";
    }
} else {
    echo "<tr><td colspan='6'>No commissions found</td></tr>";
}

// Close the result sets
$result_artist->close();

// Close the database connection
$conn->close();
?>
