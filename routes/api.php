<?php

use App\Http\Controllers\NoticiasController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::group(['middleware' => ['cors']], function () {
    //Rutas a las que se permitirá acceso
    
    //Webscraping de educatolerancia
    Route::get('webscraping/noticias/educatolerancia', [NoticiasController::class, 'educaToleranciaWebscraping']);

    //Obtener las noticias
    Route::get('noticias', [NoticiasController::class, 'getNoticias']);

    //Obtener la noticia por id del articulo
    Route::get('noticias/{id_article}', [NoticiasController::class, 'getNoticiasById']);
});