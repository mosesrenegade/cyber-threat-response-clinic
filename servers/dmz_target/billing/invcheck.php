<html>
  <head>
    <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="icon" href="img/favicon.png" type="image/png">
    <!-- css area -->
      <link rel="stylesheet" href="css/bootstrap.css">
      <link rel="stylesheet" href="vendors/linericon/style.css">
      <link rel="stylesheet" href="css/font-awesome.min.css">
      <link rel="stylesheet" href="vendors/owl-carousel/owl.carousel.min.css">
      <link rel="stylesheet" href="vendors/lightbox/simpleLightbox.css">
      <link rel="stylesheet" href="vendors/nice-select/css/nice-select.css">
      <link rel="stylesheet" href="vendors/animate-css/animate.css">
    <!-- main css -->
      <link rel="stylesheet" href="css/style.css">
  </head>

<body>
    <section class="banner_area">
        <div class="banner_inner d-flex align-items-center">
            <div class="overlay bg-parallax"></div>
            <div class="container">
                <div class="banner_content text-center">
                    <div class="page_link">
		        <a href="/">HackMDS Home</a>
                        <a href="/billing/index.php">Billing</a>
                    </div>
                    <h2>Invoices</h2>
                </div>
            </div>
        </div>
 <section class="contact_area section_gap">
        <div class="container">
<?php

$servername = 'localhost';
$username = 'root';
$password = '';
$db = 'INVOICES';

// Create the Connection

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error){
  die("Connect failed" . $conn->connect_error);
}

if(isset($_GET["invoice"])) {
  $id = $_GET["invoice"];
  $sql="SELECT * from invoices WHERE invoice_number = $id";
  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
      // output data of each row
      while($row = $result->fetch_assoc()) {
          echo "Invoice Number: " . $row["invoice_number"]. " - Date: " .$row["date"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
          echo "Amount Due: " . $row["amount_due"] . "<br>";
          echo "Credit Card Number: " . $row["cc_num"] . "<br>";
	  echo "Email: " . $row["email"]. "<br>";
          echo "Address: " . $row["address"]. "<br>";
	  }
       } else {
      echo($id . " Not Found <br>");
      echo($conn->error . "<br>");
      print($conn->error . "<br>");
  }
  $conn->close();
  } else {
  echo "You didn't provide an invoice number!";
}
?>
      </div>
    </section>
</body>
</html>

