<?php

$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["img"]["name"]);
$extension = end($temp);
if ((($_FILES["img"]["type"] == "image/gif")
|| ($_FILES["img"]["type"] == "image/jpeg")
|| ($_FILES["img"]["type"] == "image/jpg")
|| ($_FILES["img"]["type"] == "image/pjpeg")
|| ($_FILES["img"]["type"] == "image/x-png")
|| ($_FILES["img"]["type"] == "image/png"))
&& ($_FILES["img"]["size"] < 2000000)
&& in_array($extension, $allowedExts))
  {
  if ($_FILES["img"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["img"]["error"] . "<br>";
    }
  else
    {

    $file = generateRandomString(6) . "." . $extension;

	while(file_exists("images/" . $file))
	{
		$file = generateRandomString(6) . "." . $extension;
	}

    move_uploaded_file($_FILES["img"]["tmp_name"], "images/" . $file);
    echo "http://scrni.com/i/" . $file;
    
    }
  }
else
  {
  echo "Upload failed!";
  }

  function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
  }

?>