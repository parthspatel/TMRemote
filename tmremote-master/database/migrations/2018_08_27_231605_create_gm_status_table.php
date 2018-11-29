<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateGmStatusTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        /*
         * GM Status Config:
         * 0 - maintenance
         * 1 - offline
         * 2 - online
         */
        Schema::create('gm_status', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('scania')->default(0);
            $table->integer('bera')->default(0);
            $table->integer('windia')->default(0);
            $table->integer('khroa')->default(0);
            $table->integer('grazed')->default(0);
            $table->integer('mybckn')->default(0);
            $table->integer('rebootna')->default(0);
            $table->integer('luna')->default(0);
            $table->integer('rebooteu')->default(0);
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
        Schema::dropIfExists('gm_status');
    }
}
