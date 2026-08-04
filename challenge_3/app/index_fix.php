<?php
$base = realpath(__DIR__ . '/files');
if (!isset($_GET['name'])) {
    echo "<h1>Seznam souborů</h1>";
    echo "<ul>";
    foreach (glob($base . '/*') as $file) {
        $name = basename($file);
        $url = 'index_fix.php?name=' . urlencode($name);
        echo '<li><a href="' . htmlspecialchars($url) . '">'
            . htmlspecialchars($name) . '</a></li>';
    }
    echo "</ul>";
    exit;
}

$name = basename((string)$_GET['name']);
if ($name === '') {
    http_response_code(400);
    echo "Neplatný nebo prázdný název souboru.";
    exit;
}

$path = realpath($base . '/' . $name);
if (!$path || strpos($path, $base) !== 0 || !is_file($path)) {
    http_response_code(403);
    echo "Zakázáno!";
    exit;
}

$content = file_get_contents($path);
echo htmlspecialchars($content);
