<?php

namespace App\Http\Controllers;

class NoticiasController extends Controller
{
    // Webscraping de noticias
    public function educaToleranciaWebscraping(){
        exec('python ../webscraping/EducaTolerancia-Webscraping.py 0 1');

        $noticias = json_decode(file_get_contents("./noticias.json"));

        return response() -> json($noticias);
    }
}
?>