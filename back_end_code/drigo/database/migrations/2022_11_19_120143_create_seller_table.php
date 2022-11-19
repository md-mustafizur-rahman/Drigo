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
        Schema::create('seller', function (Blueprint $table) {
            $table->id('seller_id');
            $table->string('name',100);
            $table->string('username',60);
            $table->string('category',100);
            $table->string('shopname',100);
            $table->string('email',100);
            $table->double('latitude',60);
            $table->double('longitude',60);
            $table->string('password');
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
        Schema::dropIfExists('seller');
    }
};
