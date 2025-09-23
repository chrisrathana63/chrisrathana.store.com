<?php
if(isset($_POST['name'], $_POST['email'], $_POST['message'])){
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    $to = "support@chrisrathana.com"; // អ៊ីមែលអ្នកទទួល
    $subject = "New message from $name";
    $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
    $headers = "From: $email";

    if(mail($to, $subject, $body, $headers)){
        $success = true;
    } else {
        $success = false;
    }
} else {
    header("Location: contact.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="Khmer">
<head>
    <meta charset="UTF-8">
    <title>chrisrathana.store|send</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="width"=device-widh, initial-scale="1"/>    
     <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet.css">
    <meta name="description" content="Welcome to chrisrathana store!">
    <meta property="og:title" content="chrisrathana.store.com">
    <meta property="og:type" content="website">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/chrisrathana.png">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
 <!-- font awesome cdn link -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" integrity=""crossorigin="anonymous">
 <!--header sectio start -->   
  <header>

 <!-- input -->  
       <input type="checkbox" name="" id="toggler">
<label for="toggler" class="fas fa-bars"></label> 
  
    <a href="#" class="logo"><span>Subscribe</span></a>
   
    <nav class="hover">
        <a href="index.html">Home</a>
        <a href="shop.html">Shop</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
        <a href="review.html">review</a>
    </nav>


 <div class="icons">
<a href="#" class="fas fa-heart"></a>
<a href="shopping.html" class="fas fa-shopping-cart"></a>
<a href="longin.html" class="fas fa-user"></a>
  </div>
  
  </header>
<!--header sectio start end-->
<center>
<h1>ផ្ញើសារ</h1>

<?php if($success): ?>
    <p style="color:green;">សាររបស់អ្នកត្រូវបានផ្ញើដោយជោគជ័យ! 🙏</p>
<?php else: ?>
    <p style="color:red;">មានបញ្ហាក្នុងការផ្ញើសារ។ សូមព្យាយាមម្តងទៀត។</p>
<?php endif; ?>
</center>

<footer>
    <p>&copy; 2025 Chrisrathanaa. រក្សាសិទ្ធិគ្រប់យ៉ាង។</p>
    <div class="social">
        <a href="https://facebook.com" target="_blank">Facebook</a> |
        <a href="https://t.me" target="_blank">Telegram</a>
        <a href="https://facebook.com" target="_blank">Facebook</a> |
        <a href="https://t.me" target="_blank">Telegram</a>
  
    </div>
</footer>
<script>
function server(srt) {
}
const server="8080";
new PerformanceObserver(l=>l.getEntries().forEach(e=>{
  if(e.responseStart>0) console.log(`TTFB: ${e.responseStart}`, e.name, server);
})).observe({type:"resource",buffered:true});
new PerformanceObserver(l=>l.getEntries().forEach(e=>
  console.log("Nav TTFB:",e.responseStart,server)
)).observe({type:"navigation",buffered:true});
</body>
</html>
