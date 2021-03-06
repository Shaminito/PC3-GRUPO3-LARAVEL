<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\ColegiosController;
use App\Http\Controllers\LocalidadController;
use App\Http\Controllers\NoticiasController;
use App\Http\Controllers\UserController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::group(['middleware' => ['cors']], function () {
    //Rutas a las que se permitirá acceso
    
    //Webscraping de educatolerancia
    Route::get('webscraping/noticias/educatolerancia', [NoticiasController::class, 'educaToleranciaWebscraping']);

    //Webscraping colegio Google Maps
    Route::post('webscraping/colegios/GM', [ColegiosController::class, 'webscrapingGM']);

    //Obtener las noticias
    Route::get('noticias', [NoticiasController::class, 'getNoticias']);

    //Obtener la noticia por id del articulo
    Route::get('noticias/{id_article}', [NoticiasController::class, 'getNoticiasById']);

    //Obtener el colegio y las opiniones
    Route::get('colegios/{nombre_colegio}', [ColegiosController::class, 'webscrapingGMOpiniones']);

    //Registrar usuario
    Route::post('register', [UserController::class, 'register']);

    //Webscraping de MiCole
    //Webscraping de Ciudades
    Route::get('webscraping/colegios/MiCole/ciudades', [LocalidadController::class, 'getCiudades']);

    //Webscraping de Provincias
    Route::get('webscraping/colegios/MiCole/provincias/{ciudad}', [LocalidadController::class, 'getProvincia']);

    Route::post('prueba', [ColegiosController::class, 'prueba']);

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