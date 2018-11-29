<h5 class="card-title">
    Ban Detection Status

    <small class="float-right">
        Last Updated: {{ \Carbon\Carbon::createFromTimeStamp(strtotime($worldStatus['created_at']))->diffForHumans() }}
    </small>
</h5>

<table class="table table-sm table-bordered world-status-table">
    <thead>
    <tr>
        <th scope="col"></th>
        <th scope="col">World</th>
        <th scope="col">Status</th>
    </tr>
    </thead>
    <tbody>
    @foreach ($worldStatus['worlds'] as $key => $world)
        <?php
        $statusClass = '';
        switch ($world['status_code']) {
            case 0:
                $statusClass = 'alert-warning';
                break;
            case 1:
                $statusClass = 'alert-light';
                break;
            case 2:
                $statusClass = 'alert-success';
                break;
            default:
                $statusClass = 'alert-warning';
        }
        ?>
        <tr class="<?php echo $statusClass;?>">
            <td style="text-align: center"><img src="{{ url('images/worlds/'.$key.'.png') }}"></td>
            <td>{{ $world['name'] }}</td>
            <td>{{ ucfirst($world['status']) }}</td>
        </tr>
    @endforeach
    </tbody>
</table>

<style>
    .world-status-table tr th:first-child,
    .world-status-table tr td:first-child {
        width: 25px;
        border-right-color: transparent;
    }
</style>
