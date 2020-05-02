<?php
session_start();
header('UserLogin.php');

$conn = mysqli_connect('localhost','root');
if($conn){
    echo "Connected!!";
}else{
    echo "NOT Connected!!";
}

mysqli_select_db($conn,'userlogin');
$Username = $_POST['Username'];
$Password = $_POST['Password'];

$q ="select * from userlogin where Username= '$Username' && Password ='$Password' ";


$result = mysqli_query($conn,$q);

$num = mysqli_num_rows($result);

if($num==1){
    echo "Same Data EXIST!!";

}else{

    $qy = "insert into userlogin(Username , Password) values ('$Username','$Password')";
    mysqli_query($conn,$qy);
    echo "SignUp Successfully!!";
}

?>