<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

if(empty($_POST["username"])){
  die("user required")
}

print_r($_POST);
/*
// Database connection details
$servername = "localhost";
$database_name = "SummitSync";
$db_username = "root";
$db_password = "HackerHack2024";

$connect = mysqli_connect($servername, $db_username, $db_password, $database_name);

if(!$connect)
  die("Connection Failed");

echo "Database connected";

mysqli_close($connect);

// Create connection
$con = new mysqli($servername, $db_username, $db_password, $database_name);

// Check connection
if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
}
echo "Connected successfully";

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from POST data
    $input_username = $_POST['username'];
    $input_password = $_POST['password'];

    // Prepare SQL statement to prevent SQL injection
    $sqlQ = $con->prepare("SELECT username, pass_word FROM Users WHERE username = ?");
    $sqlQ->bind_param("s", $input_username);
    $sqlQ->execute();
    $result = $sqlQ->get_result();

    // Check if a user was found
    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $stored_password = $row['pass_word'];

        // Verify the password
        if (password_verify($input_password, $stored_password)) {
            // Password is correct, redirect to index.html
            require './index.html';
            exit;
        } else {
            // Password is incorrect
            echo "Invalid username or password";
        }
    } else {
        // No user found with the given username
        echo "Invalid username or password";
    }
}
// Close the connection
$con->close();
*/
?>
