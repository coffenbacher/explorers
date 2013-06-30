<?php

//Start session
session_start();

$_SESSION['SESS_USER_NAME'] = 5;



session_write_close();
header("location: index.php");
exit();
?>
