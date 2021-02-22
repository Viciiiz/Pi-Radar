<?php
echo "Today is " . date('Y-m-d H:i:s');
echo "<hr><h2>Hello World!</h2><br>";
echo'
<html>
	<!-- start and stop buttons -->
	<form action = "mywebpage.php" method = "post">
		<input type = "submit" name = "on" value = "START"><br>
	</form>
</html>
';

// activate the program
if(isset($_POST['on'])){

	// upload image if it exists
	if(file_exists('image.jpg')){
		echo '
		<!DOCTYPE html>
		<html>
			<!-- upload image -->
			<img src="image.jpg" width="640" height="480" title="Motion captured" alt="Motion captured" />
			<br><hr><br>
		</html>
		';

	// radio button for gun status
	echo '
	<!DOCTYPE html>
	<html>
			<!-- gun status (radio buttons) -->
		<form action = "mywebpage.php" method = "post">
			Safe: <input type = "radio" name = "status" value = "SAFE"><br><br>
		      	Fire: <input type = "radio" name = "status" value = "FIRE"><br><br>
			Gatling gun: <input type = "radio" name = "status" value = "GATLING"><br><br>
			<input type = "submit"><br>
		</form>
	</html>
	'; // end of echo
	} else { // the sensor hasn't detected any object
		echo "<h1>Nothing to report...</h1>;";
	}

	//call a python program
	$status = $_POST["status"];
	$a = 'python cgi-bin/omega.py '.$status;
	//echo $a;
	$command = escapeshellcmd($a); // basically grabs all the commands in $a and puts it on the terminal
	$output = shell_exec($command); // execute command on the terminal
	echo $output;
	// had to close this php program because it won't run after the python program that was called
	?>

	<?php

} else { // if the START button wasn't pressed
	echo "Press START to begin the program";
}
?>
