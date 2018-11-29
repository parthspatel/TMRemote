<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateBotLogsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('bot_logs', function (Blueprint $table) {
            $table->increments('id');
            $table->integer('user_id');
            $table->integer('char_id');
            $table->string('char_name')->nullable();
            $table->string('world_id')->nullable();
            $table->string('channel')->nullable();
            $table->string('level')->nullable();
            $table->string('mesos')->nullable();
            $table->string('map_id')->nullable();
            $table->string('nodes')->nullable();
            $table->text('item_data')->nullable();
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
        Schema::dropIfExists('bots_logs');
    }
}
