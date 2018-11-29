<?php

namespace Vanguard\Widgets;

use Arrilot\Widgets\AbstractWidget;
use Vanguard\BotLog;
use Auth;
use Carbon\Carbon;

class BotLogs extends AbstractWidget
{
    /**
     * The configuration array.
     *
     * @var array
     */
    protected $config = [];

    /**
     * The number of seconds before each reload.
     *
     * @var int|float
     */
    public $reloadTimeout = 30;

    /**
     * Treat this method as a controller action.
     * Return view() or other content to display.
     */
    public function run()
    {
        $bots = BotLog::where('user_id', '=', Auth::id())
            ->where('created_at', '>=', Carbon::now()->subDay()->toDateTimeString())
            ->orderBy('created_at', 'desc')
            ->get();

        $myBots = $bots->unique('char_id');

        return view('widgets.bot_logs', [
            'config' => $this->config,
            'bots' => $myBots,
        ]);
    }
}
