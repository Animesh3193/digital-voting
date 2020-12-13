<script type="text/javascript">
    var video = document.querySelector("#video");

    // Basic settings for the video to get from Webcam
    const constraints = {
        audio: false,
        video: {
            width: 475, height: 475
        }
    };

    // This condition will ask permission to user for Webcam access
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia(constraints)
            .then(function (stream) {
                video.srcObject = stream;
            })
            .catch(function (err0r) {
                console.log("Something went wrong!");
            });
    }

    function stop(e) {
        var stream = video.srcObject;
        var tracks = stream.getTracks();

        for (var i = 0; i < tracks.length; i++) {
            var track = tracks[i];
            track.stop();
        }
        video.srcObject = null;
    }
</script>

<script type="text/javascript">
    // Below code to capture image from Video tag (Webcam streaming)
    $("#btnCapture").click(function () {
        var canvas = document.getElementById('canvas');
        var context = canvas.getContext('2d');

        // Capture the image into canvas from Webcam streaming Video element
        context.drawImage(video, 0, 0);
    });

    // Upload image to server - ajax call - with the help of base64 data as a parameter
    $("#btnSave").click(function () {

        // Below new canvas to generate flip/mirron image from existing canvas
        var destinationCanvas = document.createElement("canvas");
        var destCtx = destinationCanvas.getContext('2d');


        destinationCanvas.height = 500;
        destinationCanvas.width = 500;

        destCtx.translate(video.videoWidth, 0);
        destCtx.scale(-1, 1);
        destCtx.drawImage(document.getElementById("canvas"), 0, 0);

        // Get base64 data to send to server for upload
        var imagebase64data = destinationCanvas.toDataURL("image/png");
        imagebase64data = imagebase64data.replace('data:image/png;base64,', '');
        $.ajax({
            type: 'POST',
            url: 'capture_image',
            data: '{ "imageData" : "' + imagebase64data + '" }',
            contentType: 'application/json; charset=utf-8',
            dataType: 'text',
            success: function (out) {
                alert('Image uploaded successfully..');
            }
        });
    });
</script>
