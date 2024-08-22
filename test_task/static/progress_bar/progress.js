$(document).ready(function() {
    const socket = new WebSocket('ws://' + window.location.host + '/ws/progress/');
    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const taskId = data.task_id;
        const progressElement = document.getElementById('progress-' + taskId);
        if (progressElement) {
            const progress = data.progress + '%';
            progressElement.style.width = progress;
            const resultMessage = document.getElementById('result-' + taskId);
            resultMessage.textContent = progress;
        }
    };

    $('#start-task-btn').click(function() {
        $.ajax({
            url: startTaskUrl,
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            success: function(response) {
                const progressBarHtml = response.progress_bar_template;
                $('#progress-container').append(progressBarHtml);
            },
            error: function(xhr, status, error) {
                console.error('Error starting task:', error);
            }
        });
    });
});