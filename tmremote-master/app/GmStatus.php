<?php

namespace Vanguard;

use Illuminate\Database\Eloquent\Model;

class GmStatus extends Model
{
    /**
     * The database table used by the model.
     *
     * @var string
     */
    protected $table = 'gm_status';

    protected $fillable = [
        'scania',
        'bera',
        'windia',
        'khroa',
        'grazed',
        'mybckn',
        'rebootna',
        'luna',
        'rebooteu',
    ];
}
