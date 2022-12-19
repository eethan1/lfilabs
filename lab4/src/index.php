<?php 

if(isset($_GET["page"])) {
 if(preg_match('/:/', $_GET["page"])) {
  die("bad hacker");
 }else{
  include($_GET["page"]);
 }
}else{
  include('helloworld.php');
}

