<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Opiniones extends Model
{
    use HasFactory;

    protected $table = 'opiniones';
    protected $fillable = ['usuario', 'analisis_sent', 'id_colegio'];
}
