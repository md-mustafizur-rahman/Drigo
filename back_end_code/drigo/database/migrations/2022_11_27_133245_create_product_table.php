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
        Schema::create('product', function (Blueprint $table) {
            $table->id('product_id');
            $table->integer('seller_id')->length(255)->unsigned();
            $table->string('product_name', 200);
            $table->string('product_size', 100);
            $table->text('product_details');
            $table->integer('product_price')->length(255)->unsigned();
            $table->string('product_Image', 255);
            $table->string('seller_name', 100);
            $table->string('seller_category', 100);
            $table->string('shopname', 100);
            $table->double('shop_latitude', 60);
            $table->double('shop_longitude', 60);
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
        Schema::dropIfExists('product');
    }
};
