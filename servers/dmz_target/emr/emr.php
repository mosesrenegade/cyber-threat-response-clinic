<?php

  if(empty($_POST['username']))
  {
    $this->HandleError("Username is blank");
    return false;
  }

  if(empty($_POST['password']))
  {
    $this->HandleError("Password is blank");
    return false;
  }

  $username = trim($_POST['username']);
  $password = trim($_POST['password']);

  if ($username === 'lpeterson')
  {
    if ($password === '!!coco92!!')
    {
      sleep(1);
      //echo "You win!";
      echo "<img src='healthcare.jpg'>";
    }
  }

  else
  {
    sleep(1);
    echo "You lose!";
    die();
  }
  
?>