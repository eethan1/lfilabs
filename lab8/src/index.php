<?php 

if(isset($_GET["page"])) {
  $f = $_GET["page"];
  $c = file_get_contents($f);
  if(!preg_match('/cjiso/', $c)) {
    die("no my signature");
  }
  include($f);
}else{
  include('helloworld.php');
}
