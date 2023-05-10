<?php
$frutas = array(
    "vermelhas" => array(
        "melancia",
        "cereja",
        "framboesa",
        "morango"
    ),

    "citricas" => array(
        "laranja",
        "limao",
        "abacaxi",
        "mexerica"
    ),
    "tropicais" => array(
        'banana',
        'manga',
        'coco',
        'caju',
        'goiaba',
    )
);
foreach ($frutas as $fruta) {
    print_r($fruta);
}