<?php
$servername = "localhost";
$username = "root";
//$password = "C1sco12345";
$password = "";
$db = "INVOICES";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$db", $username, $password);
    // setting the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "CREATE DATABASE $db";
    // using exec() because no results are returned
    $conn->exec($sql);
    echo "Database created successfully with the name $db";
    }
catch(PDOException $e)
    {
    echo $sql . "
" . $e->getMessage();
    }
$conn = null;

try {
    $conn = new PDO("mysql:host=$servername;dbname=$db", $username, $password);
    $table = "invoices";
    $conn->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
    $sql ="CREATE TABLE IF NOT EXISTS $table ( id INT AUTO_INCREMENT, 
           invoice_number VARCHAR(255) NOT NULL , amount_due VARCHAR(255) NOT NULL, 
           date VARCHAR(255) NOT NULL, firstname VARCHAR(255) NOT NULL, 
           lastname VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, 
           address VARCHAR(255) NOT NULL, cc_num VARCHAR(255) NOT NULL, 
           PRIMARY KEY (id) );" ;
    $conn->exec($sql);
     print("Created $table Table.\n");
 
    $table = "comments";
    $sql ="CREATE TABLE IF NOT EXISTS $table (id INT AUTO_INCREMENT PRIMARY KEY, 
           comment_title VARCHAR(255) NOT NULL, comment VARCHAR(255) NOT NULL, 
           invoice_id INT, FOREIGN KEY (invoice_id) REFERENCES invoices(id) );" ;

    $conn->exec($sql);
    print("Created $table Table.\n");
} catch(PDOException $e) {
    echo $e->getMessage();//Remove or change message in production code
}

try {
    $table = "invoices";
    $sql = "INSERT INTO $table (invoice_number, amount_due, date, 
            firstname, lastname, email, address, cc_num) VALUES 
            ('000000001', '388.00', '5/1/2019', 'DOOGIE', 'HOUSER', 
            'DaMan1990@aol.com', '1428 Elm Street', 
            '5145757998170252');";
    $conn->exec($sql);
    print("Created $table Table.\n");
} catch(PDOException $e) {
    echo $e->getMessage();//Remove or change message in production code
}
?>

