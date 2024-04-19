<?php
// Handle form submission and database storage

// Validate and sanitize user input
$portraitType = $_POST['portraitType'];
$userName = $_POST['userName'];
$userNumber = $_POST['userNumber'];
$status = $_POST['status'];

// Process the image (store or further processing)
$userImage = $_FILES['userImage'];
$imagePath = 'uploads/' . $userImage['name'];

// Check if the file is an image (adjust as needed based on acceptable image types)
$allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
if (in_array($userImage['type'], $allowedTypes) && $userImage['error'] === 0) {
    move_uploaded_file($userImage['tmp_name'], $imagePath);

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

    // Use prepared statement to prevent SQL injection
    $sql = $conn->prepare("INSERT INTO artist (portrait_type, user, `number`, `image`, `status`)
                        VALUES (?, ?, ?, ?, ?)");
    $sql->bind_param("sssss", $portraitType, $userName, $userNumber, $imagePath, $status);


    if ($sql->execute()) {
        // Send email notification
        $to = "rohitthorat680@gmail.com";
        $subject = "New Commission Submission";
        $message = "A new commission has been submitted.\n";        
        $headers = "From: adityasuryawanshi4040@gmail.com";
        
        // Send email
        if (mail($to, $subject, $message, $headers)) {
            $response = ['message' => 'Commission submitted successfully. Email notification sent.'];
        } else {
            $response = ['message' => 'Commission submitted successfully, but email notification failed.'];
        }
    } else {
        $response = ['message' => 'Error: ' . $sql->error];
    }

    // Close the database connection
    $sql->close();
    $conn->close();
} else {
    $response = ['message' => 'Invalid file or file type.'];
}

// Send JSON response
header('Content-Type: application/json');
echo json_encode($response);
?>
