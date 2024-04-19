<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #78e08f, #0f3443);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #333;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button[type="submit"]:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            text-align: center;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Admin Login</h1>
        <!-- Admin login form -->
        <form action="" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Login</button>
            
            
        </form>

    <form action="index.php">
    <div>
    <br>Member?
        <button id="send-work-btn">Member Login</button>
    </div>
    </form>      


        <?php
        // Check if the form is submitted
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // Get user input from the form
            $username = $_POST['username'];
            $password = $_POST['password'];

            // Validate user credentials (replace with actual validation logic)
            if (validateAdminCredentials($username, $password)) {
                // Redirect to the admin home page if credentials are correct
                header("Location: homeAdmin.html");
                exit();
            } else {
                // Display an error message if credentials are incorrect
                echo "<p class='error-message'>Incorrect username or password. Please try again.</p>";
            }
        }

        // Function to validate admin credentials (replace with actual database validation)
        function validateAdminCredentials($username, $password) {
            // Connect to your database (replace these values with your actual database credentials)
            $servername = "localhost";
            $dbUsername = "root";
            $dbPassword = "iamadam4040";
            $dbName = "canvas";

            // Create a connection to the database
            $conn = new mysqli($servername, $dbUsername, $dbPassword, $dbName);

            // Check the connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Validate credentials against the admin table (replace with actual SQL query)
            $sql = "SELECT * FROM admin WHERE username = '$username' AND password = '$password'";
            $result = $conn->query($sql);

            // Close the database connection
            $conn->close();

            // Return true if credentials are valid, false otherwise
            return ($result && $result->num_rows > 0);
        }
        ?>
    </div>
</body>
</html>
