<?php
	echo "<h1>Hello World!</h1><br><hr><br>";

	if(file_exists('image.jpg')){
		echo '
		<!DOCTYPE html>
		<html>
			<img src="image.jpg" width="640" height="480" title="Motion Captured" alt="Motion captured"/>
			<br><hr><br>
		</html>
		';
	}
?>
