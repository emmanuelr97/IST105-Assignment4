<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $a = escapeshellarg($_POST['a']);
    $b = escapeshellarg($_POST['b']);
    $c = escapeshellarg($_POST['c']);
    
    $output = shell_exec("/var/www/html/calculate.py $a $b $c 2>&1");
    echo "<html><body>";
    echo $output ?? "No output received";
    echo "</body></html>";
} else {
    header("Location: form.php");
}
?>