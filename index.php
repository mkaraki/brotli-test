<?php
if (!isset($_GET['path']))
{
    http_response_code(400);
    die('Path parameter is required');
}

$path = $_GET['path'];
$actual_path = __DIR__ . '/dest-img/' . $path . '.br';

if (file_exists($actual_path)) {
    $path_case = strtolower($actual_path);
    switch (true) {
        case str_ends_with($path_case, '.jpg.br'):
        case str_ends_with($path_case, '.jpeg.br'):
            header('Content-Type: image/jpeg');
            break;
        case str_ends_with($path_case, '.png.br'):
            header('Content-Type: image/png');
            break;
        case str_ends_with($path_case, '.webp.br'):
            header('Content-Type: image/webp');
            break;
        default:
        http_response_code(500);
            echo 'Unsupported file type';
            exit;
    }
    header('Content-Encoding: br');
    echo file_get_contents($actual_path);
} else {
    http_response_code(404);
    echo 'File not found';
}