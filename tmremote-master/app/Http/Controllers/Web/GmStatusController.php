<?php

namespace Vanguard\Http\Controllers\Web;

use Illuminate\Http\Request;
use Vanguard\GmStatus;
use Vanguard\Http\Controllers\Controller;
use Cache;
use Carbon\Carbon;

class GmStatusController extends Controller
{
    const API_GM_STATUS = 'api_gm_status';

    const WEB_GM_STATUS = 'web_gm_status';

    public function getCachedStatus()
    {
        $cachedStatuses = Cache::rememberForever(self::API_GM_STATUS, function () {
            $worldNames = config('maple.world_names');
            $worldStatusCodes = config('maple.world_status_codes');
            $lastWorldStatusObj = GmStatus::orderBy('created_at', 'desc')->firstOrFail();
            $lastWorldStatus = $lastWorldStatusObj->toArray();
            $worldStatuses = [];

            // Hide certain things from world status
            unset($lastWorldStatus['id'], $lastWorldStatus['updated_at']);

            // Add created_at to returned array & then
            $worldStatuses['created_at'] = $lastWorldStatus['created_at'];
            unset($lastWorldStatus['created_at']);

            //$worldStatuses['created_ago'] = $lastWorldStatusObj->created_at->diffForHumans();
            $worldStatuses['saved'] = Carbon::now()->format('Y-m-d H:i:s');

            foreach ($lastWorldStatus as $worldKey => $status) {
                $worldStatuses['worlds'][$worldKey] = [
                    'status_code' => $status,
                    'name' => $worldNames[$worldKey],
                    'status' => $worldStatusCodes[$status],
                ];
            }

            return $worldStatuses;
        });

        return $cachedStatuses;
    }
}
