<?php

namespace App\Http\Controllers;

use App\Models\Colegios;
use App\Models\Opiniones;
use Illuminate\Http\Request;

class ColegiosController extends Controller
{
    //Webscraping de Google Maps y devuelve el resultado de la busqueda en json
    public function webscrapingGM(Request $request)
    {

        exec('python ../webscraping/GoogleMaps-Webscraping.py ' . '"Colegio ' . $request->busqueda . '"');

        $colegios = json_decode(file_get_contents("./colegios.json"));

        //Guarda el colegio en la base de datos
        foreach ($colegios as $colegio) {

            if (!(Colegios::where('url_colegio', $colegio->url)->first())) {
                $n = new Colegios();

                $n->nombre_colegio = $colegio->nombre_colegio;
                $n->opinion_media = floatval($colegio->opinion_media);
                $n->comentarios_cant = $colegio->comentarios_cant;
                $n->direccion = $colegio->direccion;
                $n->url_colegio = $colegio->url;

                $n->save();
            }
        }

        return response()->json($colegios);
    }

    public function getColegio($nombre_colegio)
    {

        $colegio = json_decode(Colegios::where('nombre_colegio', $nombre_colegio)->first());

        exec('python ../webscraping/GoogleMaps-Webscraping-Opiniones.py ' . '"' . $colegio->url_colegio . '"');

        $opiniones = json_decode(file_get_contents("./opiniones.json"));

        $colegio->opiniones = $opiniones;

        foreach ($opiniones as $opinion) {

            if (!(Opiniones::where('usuario', $opinion->usuario)->first())) {
                $n = new Opiniones();

                $n->usuario = $opinion->usuario;
                //$n->comentario = $opinion->comentario;
                $n->analisis_sent = floatval($opinion->analisis_sent);
                $n->id_colegio = $colegio->id;

                $n->save();
            }
        }

        return response()->json($colegio);
    }
}
