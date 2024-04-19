<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="adminCommision.css">
    <!-- Include your CSS stylesheets and JavaScript files here -->
</head>

<body>
    <div id="navigation">
        <div style="display: flex;justify-content: space-between;width: 500px;">
            <a href="homeAdmin.html">Home</a> |
            <a href="adminCommision.php">Manage Commissions</a> |
            <button id="logout"><a href="adminLogin.php">Log out</a></button>
        </div>

        <!-- Add more links as needed -->
    </div>

    <h1>Admin Dashboard</h1>
    <div id="table-div">
        <table border="1">
            <thead>
                <tr>
                    <th>Portrait Type</th>
                    <th>User Name</th>
                    <th>Phone Number</th>
                    <th>Image</th>
                    <th>Approval</th>
                </tr>
            </thead>
            <tbody>
                <?php include 'fetchCommision.php'; ?>
            </tbody>
        </table>
    </div>
</body>

</html>