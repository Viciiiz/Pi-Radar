<?php
echo "Today is " . date('Y-m-d H:i:s');
echo "<hr><h1>Hello World!</h1><br>";

// start button
//echo '
//<html>
//	<form action = "final.php" method = "post">
//		<input type = "submit" name = "on" value = "START"><br>
//	</form>
//</html>
//';
echo "Press button to start";

// activate the program
//if(isset($_POST['on'])){

	echo "<h2>Program is running...</h2>";

	// loop the commands
	//for($i = 0; $i < 10; $i++){

		//activate servo 1  and ultrasonic sensor. If the sensor detects an object, it will return the distance and the servo1Position.
		//take photo and upload it.
		// activate buttons
		//send sms to phone
		// wait for user input
		// if ==SAFE, call the safe.py function (it will wait 5 seconds)
		// if ==FIRE, call the fire.py function (it will fire, then check object, and fire up to 3 times, then rifle)
		// if ==RIFLE, call the rifle.py function (rifle for 5 seconds)
		// loop


		// -----------1-------- ULTRASONIC
		$commandUltrasonic = escapeshellcmd('python ultrasonic_sensor.py');
		$outputUltrasonic = shell_exec($commandUltrasonic);
		$dataUltrasonic = explode(" ", $outputUltrasonic);
		$distance = number_format($dataUltrasonic[0]);
		$servo1Position = number_format($dataUltrasonic[1]);
?>
<?php
		echo "<h3>Object detected at $distance cm.</h3>";
		// ----------2--------- TAKE PHOTO
		$commandPhoto = escapeshellcmd('python captureImage.py');
		$outputPhoto = shell_exec($commandPhoto);
?>
<?php
		// post photo
	//	if(file_exists('comp164/image.jpg')){
		echo '
			<!DOCTYPE html>
			<html>
				<img src="image.jpg" width="640" height="480" title="Motion captured" alt="Motion captured" />
				<bR><hr><br>
			</html>
		';


		//------------3----------BUTTONS
		echo '
			<!DOCTYPE html>
			<html>
				<form action = "final.php" method = "post">
					Safe: <input type = "radio" name = "status" value = "SAFE"><br><br>
					Fire: <input type = "radio" name = "status" value = "FIRE"><br><br>
					Rifle: <input type = "radio" name = "status" value = "RIFLE"><br><br>
					<input type = "submit"><br>
				</form>
			</html>
		';


		//---------4------------SEND SMS
		$commandSMS = escapeshellcmd('python send_sms.py');
		$outputSMS = shell_exec($commandSMS);
?>
<?php
		//---------5------------READ BUTTON VALUES
		$gunStatus = $_POST["status"];

		// ---------6----------SEND STATUS TO gun.py
		$commandToGun = 'python gun.py '.$gunStatus . ' '. $servo1Position;
		$commandGun = escapeshellcmd($commandToGun);
		$outputGun = shell_exec($commandGun);
		// take value back
		$gunResponse = number_format($outputGun);
?>
<?php
		if ($gunResponse == 9){
			echo "<h3>Safe, no need to fire.</h3>";
		} elseif($gunResponse <= 3 && $gunResponse > 0){
			echo "<h3>Safe. It took $gunResponse shoots.</h3>";
		} elseif($gunResponse == 4){
			echo "<h3>Safe, after firing three times, a rifle was needed.</h3>";
		} elseif ($gunResponse == 5){
			echo "<h3>Safe, a rifle was needed.</h3>";
		}

//	} // end of if .jgp file exists
?>
<?php
//	} // end of for loop

//	echo "end";

//} // end of if activate statement

?>
