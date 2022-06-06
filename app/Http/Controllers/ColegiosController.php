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

        exec('python ../webscraping/GoogleMaps-Webscraping-Colegios.py ' . '"Colegio ' . $request->busqueda . '"');

        $colegios = json_decode(file_get_contents("./colegios.json"));

        //Guarda el colegio en la base de datos
        foreach ($colegios as $colegio) {

            if (!(Colegios::where('nombre_colegio', $colegio->nombre_colegio)->first())) {
                $n = new Colegios();

                $n->nombre_colegio = $colegio->nombre_colegio;
                $n->opinion_media = floatval($colegio->opinion_media);
                $n->comentarios_cant = $colegio->comentarios_cant;
                $n->direccion = $colegio->direccion;

                $n->save();
            }
        }

        return response()->json($colegios);
    }

    public function webscrapingGMOpiniones($nombre_colegio)
    {

        $colegio = Colegios::where('nombre_colegio', $nombre_colegio)->first();

        exec('python ../webscraping/GoogleMaps-Webscraping-Opiniones.py ' . '"' . $nombre_colegio . '"');

        $opiniones = json_decode(file_get_contents("./opiniones.json"));

        $colegio->opiniones = $opiniones;

        foreach ($opiniones as $opinion) {

            if (!(Opiniones::where('usuario', $opinion->usuario)->where('id_colegio', $colegio->id)->first())) {
                $n = new Opiniones();

                $n->usuario = $opinion->usuario;
                $n->analisis_sent = floatval($opinion->analisis_sent);
                $n->id_colegio = $colegio->id;

                $n->save();
            }
        }

        return response()->json($colegio);
    }

    public function prueba(Request $request){

        $ciudad = $request->ciudad;
        $provincia = $request->provincia;

        exec('python ../webscraping/MiCole-Webscraping-Colegio.py '.$ciudad.' '.$provincia);
        
        $colegio =  file_get_contents("./nombre.txt");
        $colegio =  substr($colegio, 1, -1);
        
        return response()->json(
            [
                'colegio'=> $colegio
            ]
        );
    }
}
