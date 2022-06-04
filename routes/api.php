<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\ColegiosController;
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

    //Webscraping colegio Google Maps
    Route::post('webscraping/colegios/GM', [ColegiosController::class, 'webscrapingGM']);

    //Registrar usuario
    Route::post('register', [NoticiasController::class, 'register']);

    //Grupo de autenticación
    Route::group([

        'prefix' => 'auth'
    
    ], function () {
        // Iniciar sesión
        Route::post('login', [AuthController::class, 'login']);
        // Cerrar sesión
        Route::post('logout', [AuthController::class, 'logout']);

        //Route::post('refresh', [AuthController::class, 'refresh']);

        //Obtener los datos del usuario autenticado - endpoint privado
        Route::post('me', [AuthController::class, 'me']);
    
    });
});