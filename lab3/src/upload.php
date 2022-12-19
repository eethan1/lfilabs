<body>

<form method="POST" enctype="multipart/form-data" target='.'>
  <input name="file" type="file">
  <button type="submit">upload!</button>
</form>

<?php 
if(isset($_FILES["file"])) {
  $file = $_FILES["file"];
  $content = file_get_contents($file['tmp_name']);
  if(!preg_match('/<\?|<%/',$content)){
    move_uploaded_file($file['tmp_name'], './uploads/benign.txt');
    echo 'upload succeed /uploads/benign.txt';
  }else{
    echo 'bad content!';
  }
}
?>

</body>