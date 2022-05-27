<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('noticias', function (Blueprint $table) {
            $table->id('id');
            $table->string('id_article')->unique();
            $table->string('titulo');
            $table->string('fecha');
            $table->string('autor');
            $table->string('descripcion');
            $table->string('url_foto');
            $table->string('url_articulos');
            $table->integer('categoria');
            $table->string('medio');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('noticias');
    }
};
