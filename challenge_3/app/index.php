<?php
if (!isset($_GET['name'])) {

    $files = glob('files/*');

    echo "<h1>Seznam souborů</h1>";

    echo "<ul>";
    foreach ($files as $file) {
        $name = basename($file);
        $url = 'index.php?name=' . urlencode('files/' . $name);
        echo '<li><a href="' . htmlspecialchars($url) . '">'
            . htmlspecialchars($name) . '</a></li>';
    }
    echo "</ul>";

    exit;
}

$name = $_GET['name'];
$content = file_get_contents($name);
echo htmlspecialchars($content);
