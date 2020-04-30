<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="UserLogin.css">
    <link rel="stylesheet" href="bootstrap.css" >
    
    <title>UserLogin</title>
  </head>
  <body>
    <form action="success.php" method="POST">
		<div class="containerLogin form-group">
			<h1>Login Page</h1>
		    <label for="">Username: <input type="text" name="Username" required></label>
            <br>
			<label for="">Password: &nbsp;<input type="password" name="Password" required></label>
            <br />
            <button type="submit" class="btn btn-primary" >Login</button>
            
         </div>
    </form>    
    <form action="SignUp.php" method="POST">
         <div class="containerLOGIN form-group">   
         <h1>SignUp Page</h1>
		    <label for="">Username: <input type="text" name="Username" required></label>
            <br>
			<label for="">Password: &nbsp;<input type="password" name="Password" required></label>
            <br />
            <button type="submit" class="btn btn-danger" >Submit</button>
            
         </div>
    </form>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
