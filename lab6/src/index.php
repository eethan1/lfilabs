<?php 
session_start();

echo isset($_SESSION["prev"])? "previous page:".$_SESSION["prev"] : "";
if(isset($_GET["page"])) {
  include($_GET["page"]);
  $_SESSION["prev"] = $_GET["page"];
}else{
  include('helloworld.php');
}
