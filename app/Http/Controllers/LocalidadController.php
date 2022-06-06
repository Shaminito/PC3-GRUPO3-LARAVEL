<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LocalidadController extends Controller
{
    
    //Webscraping de MiCole para sacar las Ciudades
    public function getCiudades(){
        exec('python ../webscraping/MiCole-Webscraping-Ciudades.py');

        $ciudades = json_decode(file_get_contents("./Ciudades.json"));

        return $ciudades;
    }

    public function getProvincia($ciudad){
        exec('python ../webscraping/MiCole-Webscraping-Provincia.py '.$ciudad);

        $provincias = json_decode(file_get_contents("./provincia.json"));

        return $provincias;
    }
}
