@extends('layouts.app')

@section('page-title', 'Download')
@section('page-heading', 'Download')

@section('breadcrumbs')
    <li class="breadcrumb-item active">
        Download
    </li>
@stop

@section('content')
    @include('partials.messages')

    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h2 class="card-title h5">
                        Terminal Manager Remote Installer
                    </h2>

                    <div class="row">
                        <div class="col-md-9">
                            <div class="list-group">
                                <a href="http://www.mehodin.com/i/TMRInstaller.zip" title="Download Installer" class="list-group-item list-group-item-action" target="_blank">
                                    TMRInstaller.zip (Direct Download)
                                </a>
                            </div>
                        </div>
                        <div class="col-md-3 text-center">
                            <img src='https://maplestory.io/api/character/{"itemId"%3A38580}%2C{"itemId"%3A24116%2C"animationName"%3A"default"}%2C{"itemId"%3A1052587}%2C{"itemId"%3A2000%2C"region"%3A"GMS"%2C"version"%3A"latest"}%2C{"itemId"%3A12000%2C"region"%3A"GMS"%2C"version"%3A"latest"}/stand1/animated?showears=false&showLefEars=false&showHighLefEars=undefined&resize=1&name=&flipX=false&bgColor=0,0,0,0'>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h2 class="card-title h5">
                        Frequently Asked Questions
                    </h2>

                    <h4 class="h6 font-weight-bold">Q: How do I download and use Terminal Manager Remote?</h4>
                    <ol>
                        <li>Download TMRInstaller.zip from the download page.</li>
                        <li>Extract the contents of the zip, executing the installer inside the zip will not work.</li>
                        <li>Right-click TMRInstaller.exe and "Run As Administrator".</li>
                        <li>Select where you would like to install TMRemote <a href="#" data-toggle="modal" data-target="#videoTutorialModal">(video of steps 2-4)</a>.</li>
                        <li>Go into the folder you selected to install TMRemote in (should be called TMRemote).</li>
                        <li>Right-click TMRInstaller.exe and "Run As Administrator".</li>
                        <li>Go to Edit -> Settings and enter your TMRemote username, password.</li>
                        <li>Below username and password, there's a profiles dir and Terminal Manager path selector, profiles are the Terminal XML files,
                            just select the general folder they are in, it will automatically check subfolders.
                        </li>
                        <li>Exit the Settings window and restart TMRemote.exe as in step 6.</li>
                        <li>Launch a Terminal Client and it should have automatically enabled the script.</li>
                    </ol>
                    <p>
                        Enjoy TMRemote, <br>
                        Thank you for purchasing
                    </p>

                    <h4 class="h6 font-weight-bold">Uh oh, my installer is crashing or the installation failed to complete!</h4>
                    <p>
                        If you've run into a technical issue, such as the installer crashing or giving out an indecipherable error code, please join our
                        <a href="https://discord.gg/Evs8UWu" target="_blank">Discord Server</a>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="videoTutorialModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Q: How do I setup TMRemote?</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="embed-responsive embed-responsive-16by9">
                        <video controls class="embed-responsive-item" id="tutorialVideo">
                            <source src="https://mehodin.com/i/TMRInstaller.mp4" type="video/mp4">
                            <p>Your browser doesn't support HTML5 video. Here is
                                a <a href="https://mehodin.com/i/TMRInstaller.mp4" target="_blank">link to the video</a> instead.</p>
                        </video>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
@stop

@section('scripts')
    <script>
        $(function () {
            $('#videoTutorialModal').on('hidden.bs.modal', function (e) {
                $('#tutorialVideo').get(0).pause();
            });
        });
    </script>
@stop
