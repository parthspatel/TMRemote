<?php

namespace Vanguard;

use Illuminate\Database\Eloquent\Model;

class BotLog extends Model
{
    /**
     * The database table used by the model.
     *
     * @var string
     */
    protected $table = 'bot_logs';

    protected $fillable = [
        'char_id',
        'user_id',
        'char_name',
        'world_id',
        'channel',
        'level',
        'mesos',
        'map_id',
        'item_data',
    ];

    protected $casts = [
        'item_data' => 'array',
    ];
}
