<?php
session_start();


$conn = mysqli_connect('localhost','root');
if($conn){
    echo "Connected!!";
}else{
    echo "NOT Connected!!";
}

mysqli_select_db($conn,'userlogin');
$Username = $_POST['Username'];
$Password = $_POST['Password'];

$q ="select * from Userlogin where Username= '$Username' && Password ='$Password' ";


$result = mysqli_query($conn,$q);

$num = mysqli_num_rows($result);

if($num==1){
    $_SESSION['samename']=$Username;
    header('location:home.php');

}else{

    $qy = "insert into Userlogin(Username , Password) values ('$Username','$Password')";
    mysqli_query($conn,$qy);
}

?>
