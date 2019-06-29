<?php

$servername = 'localhost';
$username = 'root';
//$password = 'C1sco12345';
$password = '';
$db = 'INVOICES';

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error){
  die("Connect failed" . $conn->connect_error);
}

if(isset($_POST["invoice"])) {
  $id = $_POST["invoice"];
  $comment = $_POST["comment"];
  $comment_title = $_POST["title"];

  //$sql="SELECT * from invoices JOIN comments WHERE invoice_number = $id";
  //$sql="SELECT * from invoices WHERE invoice_number = $id";
  $sql="INSERT INTO comments (comment_title, comment, invoice_id) VALUES ('$comment_title','$comment',(select id from invoices where invoice_number = $id));";
  if ($conn->query($sql) === TRUE) {
    echo "Thank you for your entry! Click <a href=invcheck.php?invoice=$id>here</a> to return to your invoice.";
  } else {
      echo($conn->error . " Statement: " . $sql . "<br>");
      print($conn->error . " Statement: " . $sql. "<br>");
  }
  $conn->close();
}
?>


