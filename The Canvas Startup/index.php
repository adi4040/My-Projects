<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>Document</title>
</head>
<body>

    <div id="Member-login-heading">
        <h1>logo</h1>
    </div>
    <div id="login-form">
        <form action="" method="post">
            <div id="login-form">
                <table>
                    <tr>
                        <td id="form-heading">
                            <h1>Member Login</h1>
                        <td>
                    </tr>
                    <tr>
                        <td>
                            <input type="text" placeholder="Enter client username" name="username" id="email">
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input type="password" placeholder="Enter client password" name="password" id="password">
                        </td>
                    </tr>
                    <tr>
                        <td style="display: flex;justify-content: center;">
                            <button type="submit" id="member-login-button">MEMBER LOG IN</button>
                        </td>
                    </tr>
                </table>
            </div>
        </form>
    </div>
    <div id="sign-up">
    <div id="sign-up-elements">
        <h1 style="text-align: center;">
            Are you an Admin?
        </h1>
        <h1 style="margin-top:10px;text-align: center;">
            Go to admin login
        </h1>
            <div style="display: flex;justify-content: center;">
                <form action="adminLogin.php" method="get">
                    <button type="submit" id="sign-up-button" name="adminLogin">Admin Login</button>
                </form>
            </div>
        </div>
    </div>

    <div id="footer">
    
        <div id="social-icons">
            <div id="footer-logo">
                <h1 id="footer-paint">Paint</h1>
                <h1 id="footer-star">Star</h1>
             </div>
            <ul>
                <li id="instagram">
                    <a href="instagram.com"><img src="images/instagram.png" alt="instagram"></a>
                </li>
                
                <li id="facebook">
                    <a href="facebook.com"><img src="images/facebook.png" alt="facebook"></a>
                </li>
               
                <li id="twitter">
                    <a href="x.com"><img src="images/twitter.png" alt="twitter"></a>
                </li>
            </ul>
        </div>
    </div>

    <?php
    // Check if the form is submitted
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Get user input from the form
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Validate user credentials (replace with actual validation logic)
        if (validateAdminCredentials($username, $password)) {
            // Redirect to the admin home page if credentials are correct
            header("Location: client.html");
            exit();
        } else {
            // Display an error message if credentials are incorrect
            echo "<script>alert('Invalid credentials. Please try again.');</script>";
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
        $sql = "SELECT * FROM client WHERE username = '$username' AND password = '$password'";
        $result = $conn->query($sql);

        // Close the database connection
        $conn->close();

        // Return true if credentials are valid, false otherwise
        return ($result && $result->num_rows > 0);
    }
    ?>

</body>
</html>
