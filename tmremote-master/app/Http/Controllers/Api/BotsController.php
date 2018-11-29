<?php

namespace Vanguard\Http\Controllers\Api;

use Illuminate\Http\Request;
use Vanguard\BotLog;
use Auth;

class BotsController extends ApiController
{
    public function log(Request $request)
    {
        if (! settings('enable_bots')) {
            return $this->errorNotFound();
        }

        $bots = $request->input('bot_logs');

        if (empty($bots)) {
            return $this->errorWrongArgs();
        }

        try {
            foreach ($bots as $bot) {
                if (isset($bot['char_id'])) {
                    BotLog::create([
                        'user_id' => Auth::id(),
                        'char_id' => $bot['char_id'],
                        'char_name' => $bot['char_name'] ?? null,
                        'world_id' => $bot['world_id'] ?? null,
                        'channel' => $bot['channel'] ?? null,
                        'level' => $bot['level'] ?? null,
                        'mesos' => $bot['mesos'] ?? null,
                        'map_id' => $bot['map_id'] ?? null,
                        'nodes' => $bot['nodes'] ?? null,
                        'item_data' => $bot['item_data'] ?? null,
                    ]);
                }
            }
        } catch (\Exception $e) {
            return $this->respondWithError($e->getMessage());
        }

        return $this->respondWithSuccess();
    }
}
