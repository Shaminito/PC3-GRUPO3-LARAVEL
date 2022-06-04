<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Colegios extends Model
{
    use HasFactory;

    protected $table = 'colegios';
    protected $fillable = ['nombre_colegio', 'reseña_media', 'comentarios_cant', 'direccion', 'url_colegio'];
}
