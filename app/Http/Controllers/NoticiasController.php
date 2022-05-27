<?php

namespace App\Http\Controllers;

use App\Models\Noticias;
use Illuminate\Database\QueryException;

class NoticiasController extends Controller
{
    // Webscraping de noticias
    public function educaToleranciaWebscraping()
    {
        exec('python ../webscraping/EducaTolerancia-Webscraping.py 0 1');

        $noticias = json_decode(file_get_contents("./noticias.json"));

        foreach ($noticias as $noticia) {
            $n = new Noticias();

            try {
                $n->id_article = $noticia->id;
                $n->titulo = $noticia->titulo;
                $n->fecha = $noticia->fecha;
                $n->autor = $noticia->autor;
                $n->descripcion = $noticia->descripcion;
                $n->url_articulos = $noticia->url_articulos;
                $n->url_foto = $noticia->url_foto;
                $n->categoria = $noticia->categoria;
                $n->medio = $noticia->medio;
                $n->save();
            } catch (QueryException) {
            }
        }
    }

    // Todas las noticias
    public function getNoticias()
    {
        return response()->json(Noticias::all());
    }

    //Obtener la noticia por id del articulo
    public function getNoticiasById($id_article)
    {
        $article = json_decode(Noticias::where('id_article', $id_article)->get()->first());
        
        exec('python ../webscraping/EducaTolerancia-Webscraping-Articulo.py '.$article->url_articulos);
        
        $cuerpo = file_get_contents("./cuerpo.txt");
        $cuerpo = substr($cuerpo, 1, -1);

        $n = new Noticias();
        $n->titulo = $article->titulo;
        $n->fecha = $article->fecha;
        $n->autor = $article->autor;
        $n->descripcion = $article->descripcion;
        $n->url_foto = $article->url_foto;
        $n->cuerpo = $cuerpo;

        return response()->json($n);
    }
}
