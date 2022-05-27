<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Noticias extends Model
{
    use HasFactory;
    
    protected $table = 'noticias';
    protected $fillable = ['id_article', 'url_articulos', 'titulo', 'fecha', 'autor', 'descripcion', 'url_foto', 'categoria', 'medio', 'cuerpo'];
}