<h5 class="card-title">Active Bots</h5>

@if($bots->count() > 0)
    <div class="table-responsive">
        <table class="table table-sm">
            <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Channel</th>
                <th scope="col">Map</th>
                <th scope="col">Level</th>
                <th scope="col">Mesos</th>
                <th scope="col">Nodes</th>
                <th scope="col">Activity</th>
            </tr>
            </thead>
            <tbody>
            @foreach ($bots as $bot)
                <tr>
                    <td>
                        <div class="small text-muted">
                            <span title="Game Server">GMS</span>
                            @if($bot->world_id)
                                /
                            @endif
                            <span title="World">{{ $bot->world_id }}</span>
                        </div>
                        <div>{{ $bot->char_name }}</div>
                    </td>
                    <td>{{ $bot->channel }}</td>
                    <td>{{ $bot->map_id }}</td>
                    <td>{{ $bot->level }}</td>
                    <td> {{ number_format($bot->mesos) }}</td>
                    <td> {{ number_format($bot->nodes) }}</td>
                    <td>
                        <div>{{ $bot->created_at->diffForHumans() }}</div>
                    </td>
                </tr>
            @endforeach
            </tbody>
        </table>
    </div>
@else
    <div class="alert alert-info">
        Your account has no recent bot activity.
    </div>
@endif


