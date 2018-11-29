<?php

namespace Vanguard\Widgets;

use Arrilot\Widgets\AbstractWidget;
use Cache;
use Vanguard\Http\Controllers\Web\GmStatusController;

class GmStatus extends AbstractWidget
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
    public $reloadTimeout = 10;

    /**
     * Treat this method as a controller action.
     * Return view() or other content to display.
     */
    public function run()
    {
        $GmStatusController = new GmStatusController();
        $worldStatus = $GmStatusController->getCachedStatus();

        return view('widgets.gm_status', [
            'config' => $this->config,
            'worldStatus' => $worldStatus,
        ]);
    }
}
