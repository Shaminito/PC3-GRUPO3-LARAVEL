<?php

namespace App\Http\Controllers;

use App\Models\Colegios;
use Illuminate\Http\Request;

class ColegiosController extends Controller
{
    //Webscraping de Google Maps
    public function webscrapingGM(Request $request)
    {
        $busqueda = $request->busqueda;
        
        exec('python ../webscraping/GoogleMaps-Webscraping.py '.$busqueda);

        $colegios = json_decode(file_get_contents("./colegios.json"));

        foreach ($colegios as $colegio) {

            if (!(Colegios::where('url_colegio', $colegio->url)->first())){
                $n = new Colegios();

                $n->nombre_colegio = $colegio->nombre_colegio;
                $n->reseña_media = floatval($colegio->reseña_media);
                $n->comentarios_cant = $colegio->comentarios_cant;
                $n->direccion = $colegio->direccion;
                $n->url_colegio = $colegio->url;
                
                $n->save();
            }
        }
    }
}
